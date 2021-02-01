import datetime, time, sched

def make_time(hour, minute):
	now = datetime.datetime.now()
	mke = "{}-{}-{} {}:{}:{}".format(now.month, now.day, now.year, hour, minute, 0)
	obj = time.strptime(mke, "%m-%d-%Y %H:%M:%S")
	return obj

