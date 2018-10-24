import sys
import webbrowser
#import colorama
from datetime import datetime
from time import sleep
#from colorama import Fore
#from colorama import Style



print("Welcome to the Sky News alarm.")
print("Please enter a time in minutes to set the alarm for:")
n = input()                           #User inputs a command line arugment with minutes until Alarm goes off.

try:
    minutes = int(n)

except ValueError:                            #User enters an incorrect value as an input.
    print("This isn't an integer. Please try again")
    print("Please enter a time in minutes to set the alarm for:")
    n = input()
if minutes < 0:                               #We could take seconds in and use these with sleep but I dont think theres much need to do this.
    print("The time you enter must be at least one minute")
    sys.exit(1)

sleep_secs = minutes * 60                     #Amount of time we have to sleep.
try:
    if minutes >= 0:                          #=0 for testing purposes.0
        print("We will wake you up in " + str(minutes) + "mins, Enjoy your sleep")
        sleep(sleep_secs)
    print("Good Morning Sunshine")
    webbrowser.open("https://www.youtube.com/watch?v=AwSra5p8MDw") #Opens Robin Williams Good Morning Vietnam.
    sleep(6)                                                       #Sleep for six seconds because the length of video.
                                                                   #Pausing the first acts as the button of the alarm.
    webbrowser.open("https://www.youtube.com/watch?v=XOacA3RYrXk") #Open Sky news which is played constantly on youtube.
    sleep(1)
finally:
    sys.exit(1)                                    #Close the program.
