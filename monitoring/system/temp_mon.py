import os
import time
import datetime
def measure_temp():
        temp = os.popen("vcgencmd measure_temp").readline()
        return (temp.replace("temp=",""))

while True:
        now = datetime.datetime.now()
        print(now.strftime('%c') +' ' + measure_temp())
        time.sleep(60)
