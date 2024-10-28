import multiprocessing


def get_square(name, number, shared_results):
    result = f"Result from {name}: {number ** 2}"
    shared_results.append(result)


if __name__ == '__main__':
    # Shared list using Manager
    with multiprocessing.Manager() as manager:
        square_results = manager.list()  # Shared list across processes

        process_list = []

        for i in range(1, 4):
            process = multiprocessing.Process(target=get_square, args=(f"Process-{i}", i, square_results))
            process_list.append(process)
            process.start()

        for process in process_list:
            process.join()

        # Print collected results
        print("Collected results:")
        for result in square_results:
            print(result)
