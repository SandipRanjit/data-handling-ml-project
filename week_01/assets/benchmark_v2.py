
import torch
import time

def benchmark_matmul(n=4000, sync=True):

    if not torch.cuda.is_available():
        raise RuntimeError("CUDA is not available. Enable a GPU runtime first.")

    print(f"Matrix size: {n} x {n}")
    print(f"GPU: {torch.cuda.get_device_name(0)}")

    # -------------------------
    # CPU
    # -------------------------
    a_cpu = torch.randn(n, n, dtype=torch.float32)
    b_cpu = torch.randn(n, n, dtype=torch.float32)

    # Warm up CPU execution
    _ = torch.matmul(a_cpu, b_cpu)

    start_cpu = time.perf_counter()
    c_cpu = torch.matmul(a_cpu, b_cpu)
    cpu_time = time.perf_counter() - start_cpu

    # -------------------------
    # GPU
    # -------------------------
    a_gpu = a_cpu.to("cuda")
    b_gpu = b_cpu.to("cuda")

    # Warm up GPU
    _ = torch.matmul(a_gpu, b_gpu)
    if sync:
        torch.cuda.synchronize()

    start_gpu = time.perf_counter()
    c_gpu = torch.matmul(a_gpu, b_gpu)

    if sync:
        torch.cuda.synchronize() # Wait for GPU to finish

    gpu_time = time.perf_counter() - start_gpu

    speedup = cpu_time / gpu_time if gpu_time > 0 else 0.0

    return cpu_time, gpu_time, speedup
