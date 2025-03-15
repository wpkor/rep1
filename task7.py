import time
import threading

def formula_1(x):
    return x ** 2 - x ** 2 + x ** 4 - x ** 5 + x + x


def formula_2(x):
    return x + x


def compute_iterations(start, end, formula, results, index):
    result = 0
    for x in range(start, end):
        result += formula(x)
    results[index] = result


def run_task(iterations):
    results = [0, 0]
    threads = []
    start_time_1 = time.time()
    thread_1 = threading.Thread(target=compute_iterations, args=(0, iterations // 2, formula_1, results, 0))
    thread_2 = threading.Thread(target=compute_iterations, args=(iterations // 2, iterations, formula_1, results, 0))
    threads.append(thread_1)
    threads.append(thread_2)
    thread_1.start()
    thread_2.start()

    for thread in threads:
        thread.join()

    end_time_1 = time.time()

    start_time_2 = time.time()
    thread_3 = threading.Thread(target=compute_iterations, args=(0, iterations // 2, formula_2, results, 1))
    thread_4 = threading.Thread(target=compute_iterations, args=(iterations // 2, iterations, formula_2, results, 1))
    threads = [thread_3, thread_4]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    end_time_2 = time.time()
    result_3 = results[0] + results[1]
    end_time_3 = time.time()

    print(f"Для {iterations} итераций:")
    print(f"Время для формулы 1: {end_time_1 - start_time_1} сек")
    print(f"Время для формулы 2: {end_time_2 - start_time_2} сек")
    print(f"Время для формулы 3: {end_time_3 - end_time_2} сек")
    print(f"Итоговый результат (формула 1 + формула 2): {result_3}\n")

run_task(10000)
run_task(100000)
