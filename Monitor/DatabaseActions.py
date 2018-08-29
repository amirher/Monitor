class DatabaseActions:
    def __init__(self, database):
        self.database = database
        self.databaseCursor = self.database.cursor()
        print "Database actions constructed"

    def getUserByUserName(self, username):
        query = "SELECT * FROM Users WHERE Users.UserName = ?"
        parameters = (username,)
        self.databaseCursor.execute(query, parameters)
        return self.databaseCursor.fetchone()

    def getParametersByDeviceName(self, devicename):
        query = "SELECT * FROM DeviceParameters WHERE DeviceName = ?"
        parameters = (devicename,)
        self.databaseCursor.execute(query, parameters)
        database_parameters = self.databaseCursor.fetchall()
        parameters = []
        for i in range(0, len(database_parameters)):
            parameters.append((database_parameters[i][0], database_parameters[i][2]))
        return parameters

    def getSchedules(self):
        query = "SELECT Schedules.ScheduleID, Schedules.DeviceName, Schedules.MonitorName, Monitors.MonitorCommand FROM Schedules, Devices, Monitors WHERE Monitors.MonitorName = Schedules.MonitorName"
        self.databaseCursor.execute(query)
        database_parameters = self.databaseCursor.fetchall()
        parameters = []
        for i in range(0, len(database_parameters)):
            parameters.append((database_parameters[i][0], database_parameters[i][1], database_parameters[i][2], database_parameters[i][3]))
        return parameters

    def addResponse(self, scheduleID, deviceName, monitorName, responseCode, responseText):
        query = "SELECT Schedules.ScheduleID, Schedules.DeviceName, Schedules.MonitorName, Monitors.MonitorCommand FROM Schedules, Devices, Monitors WHERE Monitors.MonitorName = Schedules.MonitorName"
        self.databaseCursor.execute(query)
        database_parameters = self.databaseCursor.fetchall()
        parameters = []
        for i in range(0, len(database_parameters)):
            parameters.append((database_parameters[i][0], database_parameters[i][1], database_parameters[i][2], database_parameters[i][3]))
        return parameters
