from multiprocessing import Process

def your_function(parameter):
    # Your function logic here
    print(f"Executing with parameter: {parameter}")

if __name__ == "__main__":
    parameters = [1, 2, 3, 4]  # Adjust this list based on your needs

    processes = []

    for parameter in parameters:
        process = Process(target=your_function, args=(parameter,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
