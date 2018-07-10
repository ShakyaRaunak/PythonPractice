import time

# time() -> to get current time
t = time.time()
print(t)

localtime1 = time.localtime(time.time())
print("Current Time is :", localtime1)

# Formatted Time
localtime2 = time.asctime(time.localtime(time.time()))
print("Formatted time :", localtime2)  # Formatted time : Tue Mar  6 21:07:14 2018

# asctime(time) -> to return 24 character Date Time string.
t = time.localtime()
print(time.asctime(t))  # Tue Mar  6 21:10:42 2018

# sleep(time) -> to stop the execution of script for the given interval of time.
localtime3 = time.asctime(time.localtime(time.time()))
print(localtime3)
time.sleep(10)
localtime4 = time.asctime(time.localtime(time.time()))
print(localtime4)

# strptime(String str,format f) -> returns an tuple with 9 time's attributes. It receives an String of date and a format.
timerequired = time.strptime("26 Jun 14", "%d %b %y")
print(timerequired)

# gtime() -> returns struct_time which contains 9 time attributes.
# In case, seconds are not specified it takes current second from epoch.
print(time.gmtime())

# mktime() -> returns second in floating point since epoch.
t = (2014, 2, 17, 17, 3, 38, 1, 48, 0)
second = time.mktime(t)
print(second)

# strftime() -> returns time in particular format. If time is not given, current time in seconds is fetched..
t = (2014, 6, 26, 17, 3, 38, 1, 48, 0)
t = time.mktime(t)
print(time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t)))  # Jun 26 2014 11:18:38
