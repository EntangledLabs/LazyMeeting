import datetime

class event():

	def __init__(self, ident, time, action, tz, *args):
		self.ident = ident
		self.tz = tz
		self.time = self.make_time(time)
		self.action = action
		self.args = args[0]
		# print("Event object created with time {}".format(self.time))

	# Takes in an hour and a minute and returns a time object with the current date and specified time
	def make_time(self, str):
		parts = str.split(':')
		now = datetime.datetime.now(self.tz)
		mke = "{}-{}-{} {}:{}:{}".format(now.month, now.day, now.year, parts[0], parts[1], 0)
		obj = datetime.datetime.strptime(mke, "%m-%d-%Y %H:%M:%S")
		return obj

	def get_time(self):
		return self.time

	def call_act(self):
		self.action(self.args)

	def compare_time(self, time):
		if (self.time.hour > time.hour):
			return 1
		elif (self.time.hour < time.hour):
			return -1
		else:
			if (self.time.minute > time.minute):
				return 1
			elif (self.time.minute < time.minute):
				return -1
			else:
				return 0

	def compare_event(self, event):
		return self.compare_time(event.get_time())