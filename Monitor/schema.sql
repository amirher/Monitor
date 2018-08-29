CREATE TABLE Devices (
	DeviceName varchar(255) PRIMARY KEY
);

CREATE TABLE DeviceParameters (
	ParameterName varchar(255) NOT NULL,
	DeviceName varchar(255) NOT NULL,
	ParameterValue varchar(255),
	FOREIGN KEY(DeviceName) REFERENCES Devices(DeviceName),
	PRIMARY KEY (ParameterName, DeviceName)
);

CREATE TABLE Monitors (
	MonitorName varchar(255) PRIMARY KEY,
	MonitorCommand varchar(512)
);

CREATE TABLE Schedules (
	ScheduleID INTEGER PRIMARY KEY AUTOINCREMENT,
	DeviceName varchar(255) NOT NULL,
	MonitorName varchar(255) NOT NULL,
	FOREIGN KEY(DeviceName) REFERENCES Devices(DeviceName),
	FOREIGN KEY(MonitorName) REFERENCES Monitors(MonitorName)
);

CREATE TABLE Results (
	DeviceName varchar(255) NOT NULL,
	MonitorName varchar(255) NOT NULL,
	ScheduleID int NOT NULL,
	ResultCode int NOT NULL,
	Message varchar(255),
	PRIMARY KEY (DeviceName, MonitorName, ScheduleID)
);

CREATE TABLE Users (
	UserName varchar(255) PRIMARY KEY
);

CREATE TABLE UserParameters (
	ParameterName varchar(255) NOT NULL,
	UserName varchar(255) NOT NULL,
	ParameterValue varchar(255),
	FOREIGN Key(UserName) REFERENCES Users(UserName),
	PRIMARY KEY (ParameterName, UserName)
);
