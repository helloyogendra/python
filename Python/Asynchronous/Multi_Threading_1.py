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




