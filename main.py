from pynotifier import Notification #pip install py-notifier
import psutil #pip install psutil

#Getting the Username
user= psutil.users()[0].name
UserName= user.capitalize()

#Getting the Current Battery Percentage
batteryPercent= psutil.sensors_battery() 

#Only using the Battery Percentage value
percentage= batteryPercent.percent

#Creating A Notification for 10 secs(duration=10)
Notification(str(UserName),f"You have {percentage}% battery remaining", duration=7).send() #Notification(Title, Description,Duration).send()