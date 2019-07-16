import time
from apscheduler.schedulers.blocking import BlockingScheduler
import run

def my_job():
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


sched = BlockingScheduler()
sched.add_job(run, 'interval', seconds=10)
sched.start()