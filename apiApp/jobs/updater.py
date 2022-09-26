from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from apiApp.jobs.jobs import working_days

def start():
	scheduler = BackgroundScheduler()
	scheduler.add_job(working_days, 'cron',hour=14, minute=2)
	scheduler.start()