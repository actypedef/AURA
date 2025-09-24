import sys
sys.path.append('build/')
import torch
import torch.nn.functional as F
import time
import agemm  
step = 512
M, N, K = 1, 5120, 27648
for i in range(K // step + 1):
    group = 16
    KE = step * i
    KN, KS, KO = K - 512, 512-128, 128
    torch.manual_seed(45510)
    signs = (torch.randint(0, 2, (M, K), device='cuda', dtype=torch.bfloat16) * 2 - 1)
    X = torch.rand(M, K, dtype=torch.bfloat16, device='cuda') * 3
    X[:, -KS:] = torch.rand(M, KS, dtype=torch.bfloat16, device='cuda') * 3 + 3
    X[:, -KO:] = torch.rand(M, KO, dtype=torch.bfloat16, device='cuda') * 8 + 8
    X[:, -16:] = torch.rand(M, 16, dtype=torch.bfloat16, device='cuda') * 16 + 16
    X = X * signs
    W = torch.rand(N, K, dtype=torch.bfloat16, device='cuda') * 3
    # W = torch.eye(K, dtype=torch.bfloat16, device='cuda')
    reorder_index = torch.arange(K, dtype=torch.int16, device='cuda') 

    A, SFA = agemm.reorder_quantize_x(X, reorder_index, KE)
    B, SFB = agemm.reorder_quantize_w(W, reorder_index, KE)
    torch.cuda.synchronize()

    C = agemm.matmul(A, B, SFA, SFB)
    torch.cuda.synchronize()

    D = F.linear(X, W)

    mean_value = torch.mean(C)

    variance_value = torch.var(C)

    mean_valued = torch.mean(D)

    variance_valued = torch.var(D)

    mse = F.mse_loss(D, C).item()
    print(f"MSE(k={KE:<4}): {mse:<15.8e}")
    # print(f"finish {i}")
    time.sleep(1)