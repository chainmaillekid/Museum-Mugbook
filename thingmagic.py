from __future__ import print_function
from time import sleep
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
    else:
        print("Change Detected")
        print("Detected tags was:",previous_tag_count)
        print("Is now:",current_tag_count())
        previous_tag_count=current_tag_count()
    
def initializereader():
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

initializereader()


while verifyreader()==True:
    main()


