cmake_minimum_required(VERSION 3.18)
project(MixedGemm LANGUAGES CXX CUDA)

set(CMAKE_PREFIX_PATH "/root/miniconda3/envs/micromix/lib/python3.10/site-packages/torch")
find_package(Torch REQUIRED)

# 查找 CUDA Toolkit
find_package(CUDAToolkit REQUIRED)
find_package(Python3 REQUIRED COMPONENTS Development)
include_directories(${Python3_INCLUDE_DIRS})
find_package(pybind11 CONFIG REQUIRED)
find_library(TORCH_PYTHON_LIBRARY torch_python PATHS /root/miniconda3/envs/micromix/lib/python3.10/site-packages/torch/lib NO_DEFAULT_PATH)

# 设置 CUTLASS 根目录
set(CUTLASS_ROOT ../third-party/cutlass)

# 包含 CUTLASS 头文件
include_directories(./include)
include_directories(/usr/local/cuda/include)
include_directories(${PYTHON_ROOT})
link_directories(${PYTHON_ROOT}/site-packages/torch/lib)
include_directories(${PYTHON_ROOT}/site-packages/torch/include)
include_directories(${PYTHON_ROOT}/site-packages/torch/include/torch/csrc/api/include)
include_directories(${CUTLASS_ROOT}/include)
include_directories(${CUTLASS_ROOT}/include)
include_directories(${CUTLASS_ROOT}/tools/util/include)
include_directories(${CUTLASS_ROOT}/examples/common)

# 设置 CMake CUDA 架构目标
set(CMAKE_CUDA_ARCHITECTURES 120a)

add_compile_options(-w)
add_compile_options(-fpermissive)

add_library(gemm_objs OBJECT src/nvfp4.cu src/reorder.cu)


# 创建目标可执行文件

add_executable(bench_nvfp4 benchmark/bench_nvfp4.cu
$<TARGET_OBJECTS:gemm_objs>)


add_library(agemm MODULE src/bindings.cpp $<TARGET_OBJECTS:gemm_objs>)
set_source_files_properties(src/bindings.cpp PROPERTIES LANGUAGE CUDA)
target_link_libraries(agemm PRIVATE pybind11::module "${TORCH_LIBRARIES}" "${TORCH_PYTHON_LIBRARY}" CUDA::cudart)

# 设置 CUDA 编译选项（允许宽松 constexpr）
target_compile_options(bench_nvfp4 PRIVATE $<$<COMPILE_LANGUAGE:CUDA>:--expt-relaxed-constexpr>)
target_compile_options(gemm_objs PRIVATE $<$<COMPILE_LANGUAGE:CUDA>:-Xcompiler=-fPIC>)
target_compile_options(agemm PRIVATE $<$<COMPILE_LANGUAGE:CUDA>:--expt-relaxed-constexpr>)

# 添加 CUTLASS 的架构宏定义（确保针对 SM120 架构）
target_compile_definitions(bench_nvfp4 PRIVATE CUTLASS_ARCH_SM120_SUPPORTED)
target_compile_definitions(agemm PRIVATE CUTLASS_ARCH_SM120_SUPPORTED)

set_property(TARGET agemm PROPERTY CXX_STANDARD 17)
set_target_properties(agemm PROPERTIES PREFIX "")
add_definitions(-DTORCH_EXTENSION_NAME=agemm)

