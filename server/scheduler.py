import schedule
import time

import threading


def add_schedule_everyday(time, action):
    return schedule.every().day.at(time).do(action)


def run_scheduler(interval):
    def start_schedule():
        print("Start your scheduling, press CTR+C to quit")
        while True:
            schedule.run_pending()
            time.sleep(interval)

    thread = threading.Thread(target=start_schedule)
    thread.start()


def stop_scheduler(job):
    schedule.cancel_job(job)
