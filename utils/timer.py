import time


def benchmark(func, input_data: str, label: str = None) -> tuple[float, str]:
    """
    Benchmarks a function with the given input data.

    Args:
        func (callable): The function to run.
        input_data (str): The input string to pass to the function.
        label (str): Optional label to display. Defaults to func.__name__.

    Returns:
        tuple: (elapsed_time_in_seconds, function_output)
    """
    label = label or func.__name__

    start = time.perf_counter()
    result = func(input_data)
    end = time.perf_counter()

    elapsed = end - start
    print(f"⏱ {label}: {elapsed * 1000:.3f} ms ({elapsed:.6f} s)")
    return elapsed, result


def compare(func1, func2, input_data: str) -> None:
    """
    Compares the execution time and output of two functions on the same input.

    Args:
        func1, func2 (callable): Functions to compare.
        input_data (str): The input string to test them with.
        :param input_data:
        :param func2:
        :param func1:
    """
    time1, result1 = benchmark(func1, input_data, label=func1.__name__)
    time2, result2 = benchmark(func2, input_data, label=func2.__name__)

    if result1 != result2:
        print("❌ Results differ!")
        return

    print("✅ Results match.")

    if time1 < time2:
        faster, slower = func1, func2
        t_fast, t_slow = time1, time2
    else:
        faster, slower = func2, func1
        t_fast, t_slow = time2, time1

    speedup_ratio = t_slow / t_fast if t_fast > 0 else float('inf')
    percent_faster = ((t_slow - t_fast) / t_slow * 100) if t_slow > 0 else 0

    print(f"⚡ {faster.__name__} is faster than {slower.__name__}")
    print(f"   → Speedup: {speedup_ratio:.2f}× ({percent_faster:.2f}% faster)")
