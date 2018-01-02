from __future__ import print_function
from time import sleep
import RPi.GPIO as GPIO
import subprocess
import mercury

reader = mercury.Reader("tmr:///dev/ttyS0", baudrate=115200)


## Everythin in main to be looped.
def main():
    previous_tag_count=current_tag_count()
    sleep(.4)
    if current_tag_count()==previous_tag_count:
        print("Detected tags was:",previous_tag_count)
        print("No change")
        print("testing list output, expecting 26")
        print (gpio_output[previous_tag_count])

        GPIO.output(gpio_output[previous_tag_count],True)
        sleep(.1)
        GPIO.output(gpio_output[previous_tag_count],False)
        


    else:
        previous_tag_count=current_tag_count()

        print("Change Detected")
        print("Detected tags was:",previous_tag_count)
        print("Is now:",current_tag_count())
        GPIO.output(gpio_output[previous_tag_count],True)
        sleep(.1)
        GPIO.output(gpio_output[previous_tag_count],False)
        



    
def initialize_reader():
	reader.set_region("NA2")
	reader.set_read_plan([1], "GEN2", read_power=1900)


def verifyreader():
    #To determine if rfid reader is responding correctly.
    readermodel = (reader.get_model())
    if (readermodel=="M6e Nano"):
        print ("Found M6e Nano")
        return True
    else:
        #reboots rasbperry pi which also reboots the reader.
        print ("-Unable to detect 'M6e Nano' rfid reader.")
        sleep(2)
        print ("-Rebooting Rasberry Pi.")
        sleep(5)
        subprocess.Popen(["sudo", "reboot"])

def current_tag_count():
    detectedtags = reader.read(timeout=200)
    return (len(detectedtags))


GPIO.setmode(GPIO.BCM)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)

gpio_output = [5, 6, 13, 19, 26, 26]


initialize_reader()


if verifyreader()==True:
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    main()
    GPIO.cleanup()
        


