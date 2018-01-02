from time import sleep
import RPi.GPIO as GPIO
import subprocess
import mercury

reader = mercury.Reader("tmr:///dev/ttyS0", baudrate=115200)
reader.set_region("NA2")
reader.set_read_plan([1], "GEN2", read_power=2100)

GPIO.setmode(GPIO.BCM)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)

#maps rfid count to appropiate GPIO pin
gpio_output_list = [5, 6, 13, 19, 26, 26, 26, 26, 26, 26, 26, 26, 26, 26]


## Everythin in main to be looped.
def main():

    previous_tag_count=(len(reader.read(timeout=50)))    
    print (previous_tag_count)

    sleep(.7)

    current_tag_count=(len(reader.read(timeout=50)))
    print (current_tag_count)

    if current_tag_count==previous_tag_count:
        print("No change detected")
    else:
        print("Change Detected")       
        GPIO.output(gpio_output_list[previous_tag_count],True)
        sleep(.1)
        GPIO.output(gpio_output_list[previous_tag_count],False)

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





while verifyreader()==True:
    main()

        


