import datetime, pytz
from event import event
from utils import *

events = list()
current_event = event
tz = pytz.timezone('America/Los_Angeles')
now = datetime.datetime.now(tz)

def main():
	# Read all events from their files
	events = read_events(tz)

	# Program loop
	while True:

		if (len(events) == 0):
			break
		# Sets current event to front of the queue
		current_event = events[0]

		# Checks current time against event time.
		# If it's event time, call event action and remove event from list
		while (True):
			now = datetime.datetime.now(tz)
			if (current_event.compare_time(now) != 1):
				current_event.call_act()
				events.remove(current_event)
				break

		# Checks if event list is empty. If so, terminate program.
		if (len(events) == 0):
			break

	print("Fin.")

if __name__=='__main__':
	main()