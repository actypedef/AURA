#include "reorder.cuh"

#include "cutlass/numeric_conversion.h"

/////////////////////////////////////////////////////////////////////////////////////////////////
/// GEMM kernel configurations
/////////////////////////////////////////////////////////////////////////////////////////////////

// A matrix configuration
using         ElementA    = cutlass::nv_float4_t<cutlass::float_e2m1_t>;    // Element type for A matrix operand

// B matrix configuration
using         ElementB    = cutlass::nv_float4_t<cutlass::float_e2m1_t>;    // Element type for B matrix operand

using         ElementD    = cutlass::bfloat16_t;                            // Element type for D matrix operand
using         ElementC    = cutlass::bfloat16_t;                            // Element type for C matrix operand

int main() {
    
    const int M = 128;
    const int N = 4096;
    const int K = 4096;
    const int block_size = 16; 
    
    ElementA::DataType *A;
    ElementB::DataType *B;
    ElementC *X;
    ElementD *W;
    A = new ElementA::DataType[M * K];
    B = new ElementB::DataType[N * K];
    X = new ElementC[M * K];
    W = new ElementD[N * K];
    
    // 创建 scale 数组（每 block_size 个元素对应一个缩放因子）
    int szA = ((M * K + block_size - 1) / block_size);
    ElementA::ScaleFactorType *scaleA = new ElementA::ScaleFactorType[((M * K + block_size - 1) / block_size)];
    int szB = ((N * K + block_size - 1) / block_size);
    ElementB::ScaleFactorType *scaleB = new ElementB::ScaleFactorType[((N * K + block_size - 1) / block_size)];
    
    std::srand(static_cast<unsigned int>(std::time(0)));
    cutlass::NumericConverter<ElementC, float, cutlass::FloatRoundStyle::round_to_nearest> converterX;
    cutlass::NumericConverter<ElementD, float, cutlass::FloatRoundStyle::round_to_nearest> converterW;
    
    for (int i = 0; i < M * K; ++i) {
        // 模拟浮点值
        float f = static_cast<float>(std::rand()) / RAND_MAX * 2000000000.0f - 1000000000.0f;
        
        X[i] = converterX(f);
    }
    for (int i = 0; i < N * K; ++i) {
        // 模拟浮点值
        float f = static_cast<float>(std::rand()) / RAND_MAX * 2000000000.0f - 1000000000.0f;
        
        W[i] = converterW(f);
    }
    int16_t *reorder_index = new int16_t[K];
    for(int i = 0; i < K; i++) {
        reorder_index[i] = i;
    }
    std::random_shuffle(reorder_index, reorder_index + K);
    ElementA::DataType *A_d;
    ElementB::DataType *B_d;
    ElementC *X_d;
    ElementD *W_d;    
    int16_t *reorder_index_d;
    ElementA::ScaleFactorType *SFA_d;
    ElementB::ScaleFactorType *SFB_d;

    cudaMalloc((void**)&A_d, M * K * sizeof(ElementA::DataType));
    cudaMalloc((void**)&B_d, N * K * sizeof(ElementB::DataType));
    cudaMalloc((void**)&X_d, M * K * sizeof(ElementC));
    cudaMalloc((void**)&W_d, N * K * sizeof(ElementD));
    cudaMalloc((void**)&reorder_index_d, K * sizeof(int16_t));
    cudaMalloc((void**)&SFA_d, szA * sizeof(ElementA::ScaleFactorType));
    cudaMalloc((void**)&SFB_d, szB * sizeof(ElementB::ScaleFactorType));
    cudaMemcpy(X_d, X, M * K * sizeof(ElementC), cudaMemcpyHostToDevice);
    cudaMemcpy(W_d, W, N * K * sizeof(ElementD), cudaMemcpyHostToDevice);
    cudaMemcpy(reorder_index_d, reorder_index, K * sizeof(int16_t), cudaMemcpyHostToDevice);

    // Timing using CUDA events
    cudaEvent_t start, stop;
    CHECK_CUDA(cudaEventCreate(&start));
    CHECK_CUDA(cudaEventCreate(&stop));
    
    for (int it = 0; it < 200; it ++) {
        run_reorder_bf16_mixed<32, K>(
            X_d, M, reorder_index_d, 
            reinterpret_cast<uint8_t*>(AN_d), reinterpret_cast<uint8_t*>(AS_d), reinterpret_cast<uint8_t*>(AO_d), 
            SFAN_d, SFAS_d, SFAO_d, KN, KS, KO
        );
        run_reorder_bf16_mixed<32, K>(
            W_d, N, reorder_index_d, 
            reinterpret_cast<uint8_t*>(BN_d), reinterpret_cast<uint8_t*>(BS_d), reinterpret_cast<uint8_t*>(BO_d), 
            SFBN_d, SFBS_d, SFBO_d, KN, KS, KO
        );
        // matmul_host(AN_d, BN_d, AS_d, BS_d, AO_d, BO_d, M, N, KN, KS, KO, C_d, D_d, SFAN_d, SFBN_d, SFAS_d, SFBS_d, SFAO_d, SFBO_d);
    }
    CHECK_CUDA(cudaEventRecord(start));
    for (int it = 0; it < 400; it ++) {
        run_reorder_bf16_mixed<32, K>(
            X_d, M, reorder_index_d, 
            reinterpret_cast<uint8_t*>(AN_d), reinterpret_cast<uint8_t*>(AS_d), reinterpret_cast<uint8_t*>(AO_d), 
            SFAN_d, SFAS_d, SFAO_d, KN, KS, KO
        );
        // run_reorder_bf16_mixed<32, K>(
        //     W_d, N, reorder_index_d, 
        //     reinterpret_cast<uint8_t*>(BN_d), reinterpret_cast<uint8_t*>(BS_d), reinterpret_cast<uint8_t*>(BO_d), 
        //     SFBN_d, SFBS_d, SFBO_d, KN, KS, KO
        // );
        // matmul_host(AN_d, BN_d, AS_d, BS_d, AO_d, BO_d, M, N, KN, KS, KO, C_d, D_d, SFAN_d, SFBN_d, SFAS_d, SFBS_d, SFAO_d, SFBO_d);
    }
    CHECK_CUDA(cudaEventRecord(stop));
    CHECK_CUDA(cudaEventSynchronize(stop));
    float milliseconds = 0;
    CHECK_CUDA(cudaEventElapsedTime(&milliseconds, start, stop));
    // CRITICAL: Synchronize and check for errors immediately after kernel launch
    cudaError_t kernel_err = cudaGetLastError(); // Check for asynchronous errors from the kernel
    if (kernel_err != cudaSuccess) {
        std::cerr << "CUDA error after launching: "
                << cudaGetErrorString(kernel_err) << std::endl;
        // Optionally, throw an exception to propagate the error to Python
        throw std::runtime_error(std::string("CUDA error in : ") + cudaGetErrorString(kernel_err));
    }

    cudaError_t sync_err = cudaDeviceSynchronize(); // Wait for the kernel to complete and check for runtime errors
    if (sync_err != cudaSuccess) {
        std::cerr << "CUDA error during/after kernel synchronization: "
                << cudaGetErrorString(sync_err) << std::endl;
        throw std::runtime_error(std::string("CUDA sync error in kernel: ") + cudaGetErrorString(sync_err));
    }
    std::cout << "kernel finished and synced successfully." << std::endl; std::cout.flush();

    std::printf("REORDER kernel completed in %.3f ms\n", milliseconds / 400);
    std::cout << "reorder finished." << std::endl;
    cudaFree(AN_d);
    cudaFree(BN_d);
    cudaFree(AS_d);
    cudaFree(BS_d);
    cudaFree(AO_d);
    cudaFree(BO_d);
    cudaFree(X_d);
    cudaFree(W_d);
    cudaFree(SFAN_d);
    cudaFree(SFBN_d);
    cudaFree(SFAS_d);
    cudaFree(SFBS_d);
    cudaFree(SFAO_d);
    cudaFree(SFBO_d);
    return 0; 
}