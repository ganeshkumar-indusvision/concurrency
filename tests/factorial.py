import math
import time
from decimal import Decimal, localcontext
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import current_thread


def factorial_default(n):
    result = Decimal(1)

    for i in range(2, n + 1):
        result *= Decimal(i)

    return result


def factorial_local(n):
    with localcontext() as ctx:
        ctx.prec = 1_000_000

        result = Decimal(1)

        for i in range(2, n + 1):
            result *= Decimal(i)

        return result


def test_worker(n):
    expected = Decimal(math.factorial(n))

    start = time.perf_counter()
    default_result = factorial_default(n)
    default_time = time.perf_counter() - start

    start = time.perf_counter()
    local_result = factorial_local(n)
    local_time = time.perf_counter() - start

    return {
        "thread": current_thread().name,
        "n": n,
        "default_exact": default_result == expected,
        "local_exact": local_result == expected,
        "default_time": default_time,
        "local_time": local_time,
        "digits": len(str(expected)),
    }


def main():
    test_values = [100, 500, 1000, 5000]

    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [
            executor.submit(test_worker, n)
            for n in test_values
        ]

        for future in as_completed(futures):
            result = future.result()

            print(f"\n{result['thread']} | n={result['n']}")
            print(f"Digits: {result['digits']}")
            print(f"Default: {result['default_time']:.4f}s | Exact: {result['default_exact']}")
            print(f"Local:   {result['local_time']:.4f}s | Exact: {result['local_exact']}")


if __name__ == "__main__":
    main()