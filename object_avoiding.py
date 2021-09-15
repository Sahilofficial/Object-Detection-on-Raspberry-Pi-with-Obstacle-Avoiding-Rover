import time
import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

TRIG=26
ECHO=16

def init():
    gpio.setup(17, gpio.OUT)
    gpio.setup(27, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)

print("Distance Measurement...")
gpio.setup(TRIG,gpio.OUT)
gpio.setup(ECHO,gpio.IN)
gpio.output(TRIG, False)

def measure():
    time.sleep(0.333)
    gpio.output(TRIG, True)
    time.sleep(0.00001)
    gpio.output(TRIG, False)
    while gpio.input(ECHO)==0:
      pulse_start = time.time()

    while gpio.input(ECHO)==1:
      pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    return distance

def f():
    init()
    gpio.output(17,True)
    gpio.output(27,False)
    gpio.output(23,True)
    gpio.output(24,False)

def r():
    init()
    gpio.output(17, False)
    gpio.output(27, False)
    gpio.output(23, True)
    gpio.output(24, False)

def l():
    init()
    gpio.output(17, True)
    gpio.output(27, False)
    gpio.output(23, False)
    gpio.output(24, False)

def s():
    init()
    gpio.output(17, False)
    gpio.output(27, False)
    gpio.output(23, False)
    gpio.output(24, False)
    
def b():
    init()
    gpio.output(17, False)
    gpio.output(27, True)
    gpio.output(23, False)
    gpio.output(24, True)
    
    
try:
    while True:
        distance=measure()
        print("Distance : %.lf cm" % distance)
        time.sleep(0.3)
        if distance >=15:
            f()
        else:
            s()
            t=input("\nEnter Direction:")
            if t=='left':
                l()
            elif t=='right':
                r()
            elif t=='back':
                b()
            elif t=='kill':
                break;
            else:
                print("Enter correct keyword")
    gpio.cleanup()
        
except KeyboardInterrupt:
    gpio.cleanup()
