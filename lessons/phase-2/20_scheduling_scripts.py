import schedule
import datetime
import time

# Countdown Logger
counter = 0

def log_message():
    global counter
    now = datetime.datetime.now()
    formatted_time = now.strftime("%H:%M:%S")
    print(f"Still running at {formatted_time}")
    counter += 1

schedule.every(3).seconds.do(log_message)

while counter < 5:
    schedule.run_pending()
    time.sleep(1)

print("Done")

# Interval Job Runner

counter_2 = 0
counter_3 = 0

def check_status():
    global counter_2
    now = datetime.datetime.now()
    formatted_time = now.strftime("%H:%M:%S")
    print(f"Checking status at {formatted_time}")
    counter_2 += 1

def send_heartbeat():
    global counter_3
    now = datetime.datetime.now()
    formatted_time = now.strftime("%H:%M:%S")
    print(f"Heartbeat sent at {formatted_time}")
    counter_3 += 1

schedule.every(2).seconds.do(check_status)
schedule.every(5).seconds.do(send_heartbeat)

while counter_3 < 3:
    schedule.run_pending()
    time.sleep(1)

print(f"Done. check_status ran {counter_2} times and send_heartbeat ran {counter_3} times")
