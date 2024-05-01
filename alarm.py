#import stuff needed
import time
import datetime; import datetime
import time
from plyer import notification 
import pygame 

#Main
def set_alarm(hour, minute):
    now = datetime.time()
    alarm_time = datetime(now.year, now.month, now.day, hour, minute)

    #Need to calculate the time difference until the alarm
    Timediff = alarm_time - now 

    #The alarm should wait till its time
    time.sleep(Timediff.total_seconds())


    #Notification part 
    def play_sound():
        pygame.mixer.init()
        pygame.mixer.music.load("sounds_eat")  
        pygame.mixer.music.play()

# Calling the function to play the sound
    play_sound()

#Taking users input
hour = int(input("Enter the hour (0-23): "))
minute = int(input("Enter the minute (0-59): "))

set_alarm(hour, minute)



