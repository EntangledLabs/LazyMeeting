import os, configparser, webbrowser
from event import event

def open_link(link):
	webbrowser.open_new_tab(link)

def open_program(path):
	os.system(path)

def test_action(text):
	print(text)

# Returns true if event1 happens sooner than event2
def greater(event1, event2):
	ct = event1.compare_event(event2)
	if (ct == 1):
		return True
	return False

# Finds all event files and returns an ordered list (first to last) of events
def read_events(tz):
	# Locates files from the './events/' directory and stores to a list
	file_list = list()
	with os.scandir('./events/') as files:
		for file in files:
			file_list.append(file.name)

	# For each file, read time, action type, and action parameters, then make event and add to list
	event_list = list()
	config = configparser.ConfigParser()
	for path in file_list:
		config.read("./events/{}".format(path))
		if (config.get('event','action_type') == "link"):
			event_list.append(event(path,config.get('event','time'),open_link,tz,config.get('event','uri')))
		elif (config.get('event','action_type') == "program"):
			event_list.append(event(path,config.get('event','time'),open_program,tz,config.get('event','uri')))
		elif (config.get('event','action_type') == "test"):
			event_list.append(event(path,config.get('event','time'),test_action,tz,config.get('event','test')))

	# Sort the event list
	for i in range(0, len(event_list)):
		s = i
		for j in range(i, len(event_list)):
			if (greater(event_list[s], event_list[j])):
				s = j
		if (s != i):
			temp = event_list[s]
			event_list[s] = event_list[i]

	# Return the sorted event list
	return event_list