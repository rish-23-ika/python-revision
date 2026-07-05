#10. Exponential Backoff
#Problem:
#Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.

#bro its used in many places like otp sending, password reset etc.

import time

wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print("Attempt", attempts + 1, "- wait time", wait_time)

    time.sleep(wait_time)

    wait_time *= 2
    attempts += 1

#here:

#time.sleep(wait_time) → pauses the program for wait_time seconds.
#wait_time *= 2 → doubles the waiting time after every retry.
#attempts += 1 → moves to the next attempt.
#while attempts < max_retries → stops after 5 retries.