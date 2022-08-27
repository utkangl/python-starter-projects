import datetime
import time
import winsound

wake_time = input ("set the alarm time, the form is: hh-mm-ss. exp -> 11-24-32")
def alarm(wake_time):
    
    while True:
        time.sleep(1)
        now = datetime.datetime.now().strftime("%H-%M-%S") # datetime.datetime returns y,m,d,h,m,s ; we are choosing only hour minute and second from it
        if now == wake_time:
            winsound.PlaySound("alarm.wav")
            break

alarm(wake_time)