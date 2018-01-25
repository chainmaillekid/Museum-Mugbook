from time import sleep
import RPi.GPIO as GPIO
import subprocess
import mercury

#initialize thingmagic reader
reader = mercury.Reader("tmr:///dev/ttyS0", baudrate=115200)
reader.set_region("NA2")
reader.set_read_plan([1], "GEN2", read_power=1600)

GPIO.setmode(GPIO.BCM)

#maps rfid tag count to appropriate GPIO pin
gpio_output_list = [21, 5, 6, 19, 13, 26]  
  
#loop through pins and set mode and state to 'low'  
for i in gpio_output_list:   
  GPIO.setup(i, GPIO.OUT)   
  GPIO.output(i, GPIO.HIGH)  

def main():
    previous_tag_count=(len(reader.read(timeout=100)))
    print (previous_tag_count)

    sleep(.7)

    current_tag_count=(len(reader.read(timeout=100)))
    print (current_tag_count)

    if current_tag_count==previous_tag_count:
        print("\033[0;37;40m No Change Detected")
    else:
        print("\033[1;31;40m Change Detected")

        #protect against count outside range of list
        if current_tag_count > 5:
            current_tag_count = 5
            print("Set tags to 5 \033[0;37;40m")
            
        GPIO.output(gpio_output_list[current_tag_count],False)
        sleep(.1)
        GPIO.output(gpio_output_list[current_tag_count],True)

while True:
   main()