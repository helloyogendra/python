### Example Code

import time
import random

class CircuitBreaker:
    def __init__(self, failure_threshold: int, recovery_time: int):

        self.failure_threshold = failure_threshold
        self.recovery_time = recovery_time
        self.fail_count = 0
        self.last_failed_time = 0
        self.state = "CLOSED"


    def call(self, func, *args, **kwargs):
        """Executes the service call and implements circuit breaker logic."""

        if self.state == "OPEN":
            if (time.time() - self.last_failed_time) >= self.recovery_time:
                self.state = "HALF-OPEN"
            else:
                print("Circuit open! Call blocked.")
                return None

        try:
            result = func(*args, **kwargs)
            self.reset()    # Reset fail count if call succeeds
            return result
        except Exception as e:
            self.record_failure()
            print(f"Call failed: {e}")
            if self.fail_count >= self.failure_threshold:
                self.trip()
            return None


    def record_failure(self):
        self.fail_count += 1
        self.last_failed_time = time.time()


    def trip(self):
        self.state = "OPEN"
        print("Circuit tripped to OPEN! Blocking further calls.")


    def reset(self):
        self.state = "CLOSED"
        self.fail_count = 0


# Mock service to simulate success and failure
def unreliable_service():
    if random.choice([True, False, False]):  # Simulate 33% chance of success
        return "Service response"
    else:
        raise Exception("Service failure")


# Usage
circuit_breaker = CircuitBreaker(failure_threshold=3, recovery_time=10)


for i in range(10):
    print(f"Attempt {i+1}:")
    response = circuit_breaker.call(unreliable_service)
    if response:
        print(f"Received response: {response}")
    time.sleep(2)

