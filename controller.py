
import RPi.GPIO as GPIO
import curses
from time import sleep 

en = 25
in1 = 23
in2 = 24
en1 = 17
in3 = 22
in4 = 27
temp1 = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)

GPIO.setup(en1,GPIO.OUT)
GPIO.setup(in1,GPIO.LOW)
GPIO.setup(in2,GPIO.LOW)
GPIO.setup(in3,GPIO.LOW)
GPIO.setup(in4,GPIO.LOW)

p1 = GPIO.PWM(en,1)
p2 = GPIO.PWM(en1,1)

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

p1.start(100)
p2.start(100)
print("working")

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
GPIO.output(in2,GPIO.LOW)

def brake():
	GPIO.output(in1,GPIO.LOW)
	GPIO.output(in2,GPIO.LOW)
	GPIO.output(in3,GPIO.LOW)
	GPIO.output(in4,GPIO.LOW)
try:
	while True:
		char = screen.getch()
		if char == curses.KEY_UP:
			brake()
			sleep(0.3)
			print("FORWARD")
			GPIO.output(in1,GPIO.HIGH)
			GPIO.output(in2,GPIO.LOW)
			GPIO.output(in3,GPIO.HIGH)
			GPIO.output(in4,GPIO.LOW)
		if char == curses.KEY_DOWN:
			brake()
			sleep(0.3)
			print("BACKWARD")
			GPIO.output(in1,GPIO.LOW)
			GPIO.output(in2,GPIO.HIGH)
			GPIO.output(in3,GPIO.LOW)
			GPIO.output(in4,GPIO.HIGH)
		if char == curses.KEY_LEFT:
			brake()
			sleep(0.3)
			print("LEFT")
			GPIO.output(in3,GPIO.HIGH)
			GPIO.output(in2,GPIO.LOW)
			GPIO.output(in1,GPIO.LOW)
			GPIO.output(in4,GPIO.LOW)
		if char == curses.KEY_RIGHT:
			brake()
			sleep(0.3)
			print("RIGHT")
			GPIO.output(in3,GPIO.LOW)
			GPIO.output(in2,GPIO.LOW)
			GPIO.output(in1,GPIO.HIGH)
			GPIO.output(in4,GPIO.LOW)
		if char == ord(' '):
			brake()
			print("STOPPED")		
		if char == ord('q'):
			GPIO.cleanup()
			break
finally:
		curses.nocbreak();screen.keypad(0);curses.echo()
		curses.endwin()
