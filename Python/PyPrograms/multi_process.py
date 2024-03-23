import multiprocessing
import time

start_time = time.perf_counter()

def my_function(x):
    return x*x

if __name__ == '__main__':
    # Limiting the number of processes to 4
    pool = multiprocessing.Pool()

    list1 = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000]
    # Your tasks
    results = pool.map(my_function, list1)

    pool.close()
    pool.join()

    print(results)

print("time is = ", time.perf_counter() - start_time)