import time, sqlite3
from subprocess import call

from DatabaseActions import DatabaseActions

class Monitor:
	def __init__(self):
		self.running = True;
		self.database = sqlite3.connect('monitor.db')
		self.databaseActions = DatabaseActions(self.database)

	def run(self):
		while self.running:
			print self.databaseActions.getUserByUserName("bobbydilley")
			schedule = self.databaseActions.getSchedules()
			for i in range(0, len(schedule)):
				(scheduleID, deviceName, monitorName, monitorCommand) = schedule[i]
				print scheduleID, " ", deviceName, " ", monitorName, " ", monitorCommand
				params = self.databaseActions.getParametersByDeviceName(deviceName)
				for j in range(0, len(params)):
					(key, value) = params[j]
					monitorCommand = monitorCommand.replace("$" + key, value)

				print "Running monitor command: ", monitorCommand
				response = call(monitorCommand, shell=True)
				print "Response: ", response
			time.sleep(5)


