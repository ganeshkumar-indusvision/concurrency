import time

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result


if __name__ == "__main__":
    start = time.perf_counter()
    return_value = factorial(20000)
    end = time.perf_counter()
    print(f"Total runtime of the program in worker is {end - start} seconds")