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

#maps rfid tag count to appropiate GPIO pin
gpio_output_list = [5, 6, 13, 19, 26]

def main():

    previous_tag_count=(len(reader.read(timeout=50)))    
    print (previous_tag_count)

    sleep(.7)

    current_tag_count=(len(reader.read(timeout=50)))
    print (current_tag_count)

    if current_tag_count==previous_tag_count:
        print("No Change Detected")

    #protect against count outside range of list
    if current_tag_count > 4:
        current_tag_count = 4
    else:
        print("Change Detected")       
        GPIO.output(gpio_output_list[current_tag_count],True)
        sleep(.1)
        GPIO.output(gpio_output_list[current_tag_count],False)


while True==True:
    main()