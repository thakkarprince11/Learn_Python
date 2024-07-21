
# Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.

# importing time
import time


wait_time = 1
max_retries = 5
attempst = 0

while attempst < max_retries:
    print("Attempt ", attempst + 1, " - wait time ", wait_time)
    time.sleep(wait_time)           # system will sleep for given seconds
    wait_time = wait_time * 2
    attempst = attempst + 1

