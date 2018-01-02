from __future__ import print_function
import time
import subprocess
import mercury

reader = mercury.Reader("tmr:///dev/ttyS0", baudrate=115200)
readermodel = (reader.get_model())


def main():
	initializereader()
	verifyreader()
	
	if verifyreader()==False:
		print ("do main loop")


def initializereader():
	#reader = mercury.Reader("tmr:///dev/ttyS0", baudrate=115200)
	reader.set_region("NA2")
	reader.set_read_plan([1], "GEN2", read_power=1900)



def verifyreader():
    #To determine that rfid reader is responding correctly.
	if (readermodel=="M6e Nano"):
		print ("Detected M6e Nano")
		return True
	else:
        #reboots rasbperry pi which also reboots the reader.
		print ("-Unable to detect 'M6e Nano' rfid reader.")
		time.sleep (2)
		print ("-Rebooting Rasberry Pi.")
		time.sleep (5)
		subprocess.Popen(["sudo", "reboot"])

main()


#readermodel = (reader.get_model())

#detectedtags = reader.read(timeout=1000)

#print (detectedtags)
#print (len(detectedtags))

