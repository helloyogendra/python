# collecting result from thread example
import threading

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
for i in range(1, 5):
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