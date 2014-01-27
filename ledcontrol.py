import sys

# Function to turn off all leds
def switchoff():
   l1 = open("/sys/class/leds/green:ph07:led4/brightness","w")
   l2 = open("/sys/class/leds/blue:ph21:led1/brightness","w")
   l3 = open("/sys/class/leds/orange:ph20:led2/brightness","w")
   l4 = open("/sys/class/leds/white:ph11:led3/brightness","w")
   l1.write("0")
   l2.write("0")
   l3.write("0")
   l4.write("0")
   l1.close()
   l2.close()
   l3.close()
   l4.close()

# Function to turn on all leds
def switchon():
   l1 = open("/sys/class/leds/green:ph07:led4/brightness","w")
   l2 = open("/sys/class/leds/blue:ph21:led1/brightness","w")
   l3 = open("/sys/class/leds/orange:ph20:led2/brightness","w")
   l4 = open("/sys/class/leds/white:ph11:led3/brightness","w")
   l1.write("1")
   l2.write("1")
   l3.write("1")
   l4.write("1")
   l1.close()
   l2.close()
   l3.close()
   l4.close()

# Function to turn on a specific led
def active(file):
   f = open(file,"w")
   f.write("1")
   f.close()

# Function to turn off a specific led
def deactive(file):
   f = open(file,"w")
   f.write("0")
   f.close()

# Body of programm
def client():
   green = "/sys/class/leds/green:ph07:led4/brightness"
   blue = "/sys/class/leds/blue:ph21:led1/brightness"
   orange = "/sys/class/leds/orange:ph20:led2/brightness"
   white = "/sys/class/leds/white:ph11:led3/brightness"
   leds = {'-B':blue,'-O':orange,'-W':white,'-G':green}
   
   # Print the help messages
   if (len(sys.argv)<2) or (sys.argv[1] == '-h') or (sys.argv[1] == '--help'):
      print ("USAGE:  python3 ledcontrol.py [ first option ] [ led ] [ on/off]\n")
      print ("FIRST OPTION:")
      print ("-i         __Turn on all leds")
      print ("-o         __Turn off all leds")
      print ("-l         __Turn [led] [ on/off]")
      print ("-h --help  __Print this help message")
      print ("\nLEDS:")
      print ("-B   __Blue")
      print ("-O   __Orange")
      print ("-W   __White")
      print ("-G   __Green")
      print ("\nON/OFF")
      print ("-on  __ON")
      print ("-off __OFF")

   # Turn on all leds
   elif (len(sys.argv)<2) or (sys.argv[1] == '-i'):
      switchon()
   
   # Turn off all leds
   elif (len(sys.argv)<2) or (sys.argv[1] == '-o'):
      switchoff()
   
   # Turn On/Off the specificated led
   elif (len(sys.argv)<2) or (sys.argv[1] == '-l'):
      t = sys.argv[2]
      l = leds[t]
      if sys.argv[3] == '-on':
         active(l)
      elif sys.argv[3] == '-off':
         deactive(l)
      else:
         print ("No ON/OFF option selected")

   else:
     print ("No option selected")


def main():
  client()
  exit()

if __name__ == '__main__':
  main()
