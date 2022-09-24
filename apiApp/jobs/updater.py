from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from apiApp.jobs.jobs import schedule_api,on_leave

def start():
	scheduler = BackgroundScheduler()
	scheduler.add_job(schedule_api, 'cron',hour=10, minute=17,day_of_week= 'mon-fri')
	scheduler.add_job(schedule_api, 'cron',hour=10, minute=17,day= '2nd sat,4th sat')
	scheduler.add_job(on_leave, 'cron',hour=10, minute=17,day= '1st sat,3rd sat,5th sat')
	scheduler.add_job(on_leave, 'cron',hour=10, minute=17,day_of_week='sun')
	scheduler.start()