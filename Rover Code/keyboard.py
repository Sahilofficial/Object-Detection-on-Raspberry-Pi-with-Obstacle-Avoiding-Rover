# import curses and GPIO
import curses
import RPi.GPIO as GPIO

#set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)

try:
        while True:   
            char = screen.getch()
            if char == ord('q'):
                break
            elif char == curses.KEY_DOWN:
                GPIO.output(17,False)
                GPIO.output(27,True)
                GPIO.output(23,False)
                GPIO.output(24,True)
            elif char == curses.KEY_UP:
                GPIO.output(17,True)
                GPIO.output(27,False)
                GPIO.output(23,True)
                GPIO.output(24,False)
            elif char == curses.KEY_RIGHT:
                GPIO.output(17,False)
                GPIO.output(27,False)
                GPIO.output(23,True)
                GPIO.output(24,False)
            elif char == curses.KEY_LEFT:
                GPIO.output(17,True)
                GPIO.output(27,False)
                GPIO.output(23,False)
                GPIO.output(24,False)
            elif char == ord(' '):
                GPIO.output(17,False)
                GPIO.output(27,False)
                GPIO.output(23,False)
                GPIO.output(24,False) 
             
finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
