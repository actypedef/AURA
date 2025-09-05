#include <torch/extension.h>
#include <iostream>

// Include all files
#include "nvfp4.h"
#include "reorder.cuh"

inline size_t get_sfa_buffer_size_in_bytes(int num_rows, int K_dim) {
    auto layout = filter_zeros(nvfp4::get_layoutSFA(num_rows, K_dim));
    size_t num_elements = cute::size(layout);
    // return num_elements * sizeof(cutlass::float_ue4m3_t);
    return (num_rows / 128 + 1) * 128 * K_dim / 16;
}

inline size_t get_sfb_buffer_size_in_bytes(int num_rows, int K_dim) {
    auto layout = filter_zeros(nvfp4::get_layoutSFB(num_rows, K_dim));
    size_t num_elements = cute::size(layout);
    // return num_elements * sizeof(cutlass::float_ue4m3_t);
    return (num_rows / 128 + 1) * 128 * K_dim / 16;
}



torch::Tensor matmul(
        const torch::Tensor &A,
        const torch::Tensor &B,
        const torch::Tensor &SFA,
        const torch::Tensor &SFB
)
{
    uint32_t M = A.size(0);
    uint32_t N = B.size(0);
    uint32_t K = A.size(1) * 2;  // 4bit packing is on the columns
    auto C = torch::empty({M, N}, torch::dtype(torch::kBFloat16).device(A.device()));

    matmul_host_nvfp4_bf16(
        reinterpret_cast<cutlass::float_e2m1_t *>(A.data_ptr<uint8_t>()), reinterpret_cast<cutlass::float_e2m1_t *>(B.data_ptr<uint8_t>()),
        M, N, K,
        (cutlass::bfloat16_t *)C.data_ptr<at::BFloat16>(), (cutlass::bfloat16_t *)C.data_ptr<at::BFloat16>(),
        reinterpret_cast<cutlass::float_ue4m3_t *>(SFA.data_ptr<uint8_t>()), reinterpret_cast<cutlass::float_ue4m3_t *>(SFB.data_ptr<uint8_t>())
    );
    return C;
}

std::tuple<torch::Tensor, torch::Tensor> reorder_quantize_x(
        const torch::Tensor &X,
        const torch::Tensor &reorder_index,
        const int KE
)
{
    int M = X.size(0);
    int KQ = X.size(1);
    int K = KQ + KE;
    auto QX = torch::empty({M, K / 2}, torch::dtype(torch::kUInt8).device(X.device()));
    auto SFX = torch::empty({(int)get_sfa_buffer_size_in_bytes(M, K)}, torch::dtype(torch::kUInt8).device(X.device()));
    if (KQ == 4096) { // Llama
        run_reorder_x_bf16_nvfp4<16, 4096>(
            (cutlass::bfloat16_t *)X.data_ptr<at::BFloat16>(), M, reorder_index.data_ptr<int16_t>(), 
            QX.data_ptr<uint8_t>(), reinterpret_cast<cutlass::float_ue4m3_t *>(SFX.data_ptr<uint8_t>()), 
            KQ, KE
        );
    }
    else if (KQ == 8192) { // Llama
        run_reorder_x_bf16_nvfp4<16, 8192>(
            (cutlass::bfloat16_t *)X.data_ptr<at::BFloat16>(), M, reorder_index.data_ptr<int16_t>(), 
            QX.data_ptr<uint8_t>(), reinterpret_cast<cutlass::float_ue4m3_t *>(SFX.data_ptr<uint8_t>()), 
            KQ, KE
        );
    }
    else if (KQ == 14336) {
        run_reorder_x_bf16_nvfp4<16, 14336>(
            (cutlass::bfloat16_t *)X.data_ptr<at::BFloat16>(), M, reorder_index.data_ptr<int16_t>(), 
            QX.data_ptr<uint8_t>(), reinterpret_cast<cutlass::float_ue4m3_t *>(SFX.data_ptr<uint8_t>()), 
            KQ, KE
        );
    }
    else if (KQ == 11008) {
        run_reorder_x_bf16_nvfp4<16, 11008>(
            (cutlass::bfloat16_t *)X.data_ptr<at::BFloat16>(), M, reorder_index.data_ptr<int16_t>(), 
            QX.data_ptr<uint8_t>(), reinterpret_cast<cutlass::float_ue4m3_t *>(SFX.data_ptr<uint8_t>()), 
            KQ, KE
        );
    }
    else if (KQ == 5120) { // Qwen
        run_reorder_x_bf16_nvfp4<16, 5120>(
            (cutlass::bfloat16_t *)X.data_ptr<at::BFloat16>(), M, reorder_index.data_ptr<int16_t>(), 
            QX.data_ptr<uint8_t>(), reinterpret_cast<cutlass::float_ue4m3_t *>(SFX.data_ptr<uint8_t>()), 
            KQ, KE
        );
    }
    else if (KQ == 13824) {
        run_reorder_x_bf16_nvfp4<16, 13824>(
            (cutlass::bfloat16_t *)X.data_ptr<at::BFloat16>(), M, reorder_index.data_ptr<int16_t>(), 
            QX.data_ptr<uint8_t>(), reinterpret_cast<cutlass::float_ue4m3_t *>(SFX.data_ptr<uint8_t>()), 
            KQ, KE
        );
    }
    else if (KQ == 3584) { // Qwen
        run_reorder32_x_bf16_nvfp4<32, 3584>(
            (cutlass::bfloat16_t *)X.data_ptr<at::BFloat16>(), M, reorder_index.data_ptr<int16_t>(), 
            QX.data_ptr<uint8_t>(), reinterpret_cast<cutlass::float_ue4m3_t *>(SFX.data_ptr<uint8_t>()), 
            KQ, KE
        );
    }
    else if (KQ == 18944) {
        run_reorder32_x_bf16_nvfp4<32, 18944>(
            (cutlass::bfloat16_t *)X.data_ptr<at::BFloat16>(), M, reorder_index.data_ptr<int16_t>(), 
            QX.data_ptr<uint8_t>(), reinterpret_cast<cutlass::float_ue4m3_t *>(SFX.data_ptr<uint8_t>()), 
            KQ, KE
        );
    }
    else if (KQ == 27648) {
        run_down32_x_bf16_nvfp4<32, 27648>(
            (cutlass::bfloat16_t *)(torch::index_select(X, 1, reorder_index.to(torch::kInt32))).data_ptr<at::BFloat16>(), M, 
            QX.data_ptr<uint8_t>(), reinterpret_cast<cutlass::float_ue4m3_t *>(SFX.data_ptr<uint8_t>()), 
            KQ, KE
        );
    }
    else if (KQ == 28672) {
        run_down32_x_bf16_nvfp4<32, 28672>(
            (cutlass::bfloat16_t *)(torch::index_select(X, 1, reorder_index.to(torch::kInt32))).data_ptr<at::BFloat16>(), M, 
            QX.data_ptr<uint8_t>(), reinterpret_cast<cutlass::float_ue4m3_t *>(SFX.data_ptr<uint8_t>()), 
            KQ, KE
        );
    }
    else {
        std::cerr << "K value is not valid !" << std::endl;
        throw std::runtime_error(std::string("Value error in run_reorder_x_bf16_nvfp4 "));
    }
    return std::make_tuple(QX, SFX);
}

std::tuple<torch::Tensor, torch::Tensor> reorder_quantize_w(
        const torch::Tensor &W,
        const torch::Tensor &reorder_index,
        const int KE
)
{
    int N = W.size(0);
    int KQ = W.size(1);
    int K = KQ + KE;
    auto QW = torch::empty({N, K / 2}, torch::dtype(torch::kUInt8).device(W.device()));
    auto SFW = torch::empty({(int)get_sfb_buffer_size_in_bytes(N, K)}, torch::dtype(torch::kUInt8).device(W.device()));
    if (KQ == 4096) { //Llama
        run_reorder_w_bf16_nvfp4<16, 4096>(
            (cutlass::bfloat16_t *)W.data_ptr<at::BFloat16>(), N, reorder_index.data_ptr<int16_t>(), 
            QW.data_ptr<uint8_t>(), reinterpret_cast<cutlass::float_ue4m3_t *>(SFW.data_ptr<uint8_t>()), 
            KQ, KE
        );
    }
    else if (KQ == 8192) { //Llama
        run_reorder_w_bf16_nvfp4<16, 4096>(
            (cutlass::bfloat16_t *)W.data_ptr<at::BFloat16>(), N, reorder_index.data_ptr<int16_t>(), 
            QW.data_ptr<uint8_t>(), reinterpret_cast<cutlass::float_ue4m3_t *>(SFW.data_ptr<uint8_t>()), 
            KQ, KE
        );
    }
    else if (KQ == 14336) {
        run_reorder_w_bf16_nvfp4<16, 14336>(
            (cutlass::bfloat16_t *)W.data_ptr<at::BFloat16>(), N, reorder_index.data_ptr<int16_t>(), 
            QW.data_ptr<uint8_t>(), reinterpret_cast<cutlass::float_ue4m3_t *>(SFW.data_ptr<uint8_t>()), 
            KQ, KE
        );
    }
    else if (KQ == 11008) {
        run_reorder_w_bf16_nvfp4<16, 11008>(
            (cutlass::bfloat16_t *)W.data_ptr<at::BFloat16>(), N, reorder_index.data_ptr<int16_t>(), 
            QW.data_ptr<uint8_t>(), reinterpret_cast<cutlass::float_ue4m3_t *>(SFW.data_ptr<uint8_t>()), 
            KQ, KE
        );
    }
    else if (KQ == 5120) { //Qwen
        run_reorder_w_bf16_nvfp4<16, 5120>(
            (cutlass::bfloat16_t *)W.data_ptr<at::BFloat16>(), N, reorder_index.data_ptr<int16_t>(), 
            QW.data_ptr<uint8_t>(), reinterpret_cast<cutlass::float_ue4m3_t *>(SFW.data_ptr<uint8_t>()), 
            KQ, KE
        );
    }
    else if (KQ == 13824) {
        run_reorder_w_bf16_nvfp4<16, 13824>(
            (cutlass::bfloat16_t *)W.data_ptr<at::BFloat16>(), N, reorder_index.data_ptr<int16_t>(), 
            QW.data_ptr<uint8_t>(), reinterpret_cast<cutlass::float_ue4m3_t *>(SFW.data_ptr<uint8_t>()), 
            KQ, KE
        );
    }
    else if (KQ == 3584) { //Qwen
        run_reorder32_w_bf16_nvfp4<32, 3584>(
            (cutlass::bfloat16_t *)W.data_ptr<at::BFloat16>(), N, reorder_index.data_ptr<int16_t>(), 
            QW.data_ptr<uint8_t>(), reinterpret_cast<cutlass::float_ue4m3_t *>(SFW.data_ptr<uint8_t>()), 
            KQ, KE
        );
    }
    else if (KQ == 18944) {
        run_reorder32_w_bf16_nvfp4<32, 18944>(
            (cutlass::bfloat16_t *)W.data_ptr<at::BFloat16>(), N, reorder_index.data_ptr<int16_t>(), 
            QW.data_ptr<uint8_t>(), reinterpret_cast<cutlass::float_ue4m3_t *>(SFW.data_ptr<uint8_t>()), 
            KQ, KE
        );
    }
    else if (KQ == 27648) {
        run_down32_w_bf16_nvfp4<32, 27648>(
            (cutlass::bfloat16_t *)(torch::index_select(W, 1, reorder_index.to(torch::kInt32))).data_ptr<at::BFloat16>(), N, 
            QW.data_ptr<uint8_t>(), reinterpret_cast<cutlass::float_ue4m3_t *>(SFW.data_ptr<uint8_t>()), 
            KQ, KE
        );
    }
    else if (KQ == 28672) {
        run_down32_w_bf16_nvfp4<32, 28672>(
            (cutlass::bfloat16_t *)(torch::index_select(W, 1, reorder_index.to(torch::kInt32))).data_ptr<at::BFloat16>(), N, 
            QW.data_ptr<uint8_t>(), reinterpret_cast<cutlass::float_ue4m3_t *>(SFW.data_ptr<uint8_t>()), 
            KQ, KE
        );
    }
    else {
        std::cerr << "K value is not valid !" << std::endl;
        throw std::runtime_error(std::string("Value error in run_reorder_w_bf16_nvfp4 "));
    }
    return std::make_tuple(QW, SFW);
}

std::tuple<torch::Tensor, torch::Tensor> rmsnorm_quantize_x(
        const torch::Tensor &X,
        const torch::Tensor &W,
        const float eps,
        const torch::Tensor &reorder_index,
        const int KE
)
{
    int M = X.size(0);
    int KQ = X.size(1);
    int K = KQ + KE;
    auto QX = torch::empty({M, K / 2}, torch::dtype(torch::kUInt8).device(X.device()));
    auto SFX = torch::empty({(int)get_sfa_buffer_size_in_bytes(M, K)}, torch::dtype(torch::kUInt8).device(X.device()));
    if (KQ == 4096) { // Llama
        run_rmsnorm_x_bf16_nvfp4<16, 4096>(
            (cutlass::bfloat16_t *)X.data_ptr<at::BFloat16>(), (cutlass::bfloat16_t *)W.data_ptr<at::BFloat16>(), eps, 
            M, reorder_index.data_ptr<int16_t>(), 
            QX.data_ptr<uint8_t>(), reinterpret_cast<cutlass::float_ue4m3_t *>(SFX.data_ptr<uint8_t>()), 
            KQ, KE
        );
    }
    else if (KQ == 8192) { // Llama
        run_rmsnorm_x_bf16_nvfp4<16, 8192>(
            (cutlass::bfloat16_t *)X.data_ptr<at::BFloat16>(), (cutlass::bfloat16_t *)W.data_ptr<at::BFloat16>(), eps, 
            M, reorder_index.data_ptr<int16_t>(), 
            QX.data_ptr<uint8_t>(), reinterpret_cast<cutlass::float_ue4m3_t *>(SFX.data_ptr<uint8_t>()), 
            KQ, KE
        );
    }
    else if (KQ == 5120) { // Qwen
        run_rmsnorm_x_bf16_nvfp4<16, 5120>(
            (cutlass::bfloat16_t *)X.data_ptr<at::BFloat16>(), (cutlass::bfloat16_t *)W.data_ptr<at::BFloat16>(), eps, 
            M, reorder_index.data_ptr<int16_t>(), 
            QX.data_ptr<uint8_t>(), reinterpret_cast<cutlass::float_ue4m3_t *>(SFX.data_ptr<uint8_t>()), 
            KQ, KE
        );
    }
    else if (KQ == 3584) { // Qwen
        run_rmsnorm_x_bf16_nvfp4<16, 3584>(
            (cutlass::bfloat16_t *)X.data_ptr<at::BFloat16>(), (cutlass::bfloat16_t *)W.data_ptr<at::BFloat16>(), eps, 
            M, reorder_index.data_ptr<int16_t>(), 
            QX.data_ptr<uint8_t>(), reinterpret_cast<cutlass::float_ue4m3_t *>(SFX.data_ptr<uint8_t>()), 
            KQ, KE
        );
    }
    else {
        std::cerr << "K value is not valid !" << std::endl;
        throw std::runtime_error(std::string("Value error in run_rmsnorm_x_bf16_nvfp4 "));
    }
    return std::make_tuple(QX, SFX);
}

//====== pybind ======

#define DEFINE_pybind(name) m.def(#name, &name, #name);

PYBIND11_MODULE(TORCH_EXTENSION_NAME, m
)
{

    m.def("matmul", &matmul,
          "nvfp4 matmul, return bfloat16 tensor", 
          py::arg("A"), py::arg("B"),
          py::arg("SFA"), py::arg("SFB")
        );
    m.def("reorder_quantize_x", &reorder_quantize_x,
          "Reorder and quantize activation, return K + KE channels",
          py::arg("X"), py::arg("reorder_index"),
          py::arg("KE")
        );
    m.def("reorder_quantize_w", &reorder_quantize_w,
          "Reorder and quantize weight, return K + KE channels",
          py::arg("W"), py::arg("reorder_index"),
          py::arg("KE")
        );
    m.def("rmsnorm_quantize_x", &rmsnorm_quantize_x,
          "Rmsnorm and quantize activation, return K + KE channels",
          py::arg("X"), py::arg("W"), py::arg("eps"), 
          py::arg("reorder_index"),
          py::arg("KE")
        );
}