import threading
import time

# A simple function that simulates a time-consuming task
def thread_task(name, delay):
    print(f"Thread {name}: starting")
    time.sleep(delay)
    print(f"Thread {name}: finishing")

# Create two threads
thread1 = threading.Thread(target=thread_task, args=("One", 2))
thread2 = threading.Thread(target=thread_task, args=("Two", 2))

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to complete
thread1.join()
thread2.join()

print("Both threads have finished")


# collecting result from thread example
print("\nExample : Collect result from a thread\n")

GREEN = "\033[0;32m"
YELLOW = "\033[1;33m"
RESET = "\033[1;37m"

# Shared list to store results
results = []

# Lock to ensure thread-safe access to the shared list
lock = threading.Lock()

def get_square(name, number):
    # Calculate some result
    result = f"{GREEN}Result from {name}: {number ** 2}{RESET}"
    
    # Append result to the shared list
    with lock:
        results.append(result)

# Create and start threads
threads = []
for i in range(1, 9, 2):
    thread = threading.Thread(target=get_square, args=(f"Thread-{i}", i))
    threads.append(thread)
    thread.start()

# Join threads to ensure all threads finish execution
for thread in threads:
    thread.join()

# Print collected results
print("Collected results:")
for result in results:
    print(f'{YELLOW} Fetching Result- {RESET}')
    print(f'{YELLOW} {result} {RESET}')

