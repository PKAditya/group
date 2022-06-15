
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

p1 = GPIO.PWM(en,1000)
p2 = GPIO.PWM(en1,1000)

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

p1.start(25)
p2.start(25)
print("working")

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
GPIO.output(in2,GPIO.LOW)
try:
	while True:
		char = screen.getch()
		if char == curses.KEY_UP:
			print("MOVING FORWARD")
			GPIO.output(in1,GPIO.HIGH)
			GPIO.output(in2,GPIO.LOW)
			GPIO.output(in3,GPIO.HIGH)
			GPIO.output(in4,GPIO.LOW)
			char2 = screen.getch()
			if char2 == curses.KEY_DOWN:
				print("STOPPED FBACK")
				GPIO.output(in1,GPIO.LOW)
				GPIO.output(in2,GPIO.LOW)
				GPIO.output(in3,GPIO.LOW)
				GPIO.output(in4,GPIO.LOW)

		if char == curses.KEY_DOWN:
			print("MOVING BACKWARD")
			GPIO.output(in1,GPIO.LOW)
			GPIO.output(in2,GPIO.HIGH)
			GPIO.output(in3,GPIO.LOW)
			GPIO.output(in4,GPIO.HIGH)
			char3 = screen.getch()
			if char3 == curses.KEY_UP:
				print("STOPPED")
				GPIO.output(in1,GPIO.LOW)
				GPIO.output(in2,GPIO.LOW)
				GPIO.output(in3,GPIO.LOW)
				GPIO.output(in4,GPIO.LOW)
			if char3 == curses.KEY_RIGHT:
				print("MOVING BACK RIGHT")
				GPIO.output(in1,GPIO.LOW)
				GPIO.output(in2,GPIO.LOW)
				GPIO.output(in3,GPIO.LOW)
				GPIO.output(in4,GPIO.HIGH)
			if char3 == curses.KEY_LEFT:
				print("MOVING BACK LEFT")
				GPIO.output(in1,GPIO.LOW)
				GPIO.output(in2,GPIO.HIGH)
				GPIO.output(in3,GPIO.LOW)
				GPIO.output(in4,GPIO.LOW)
		if char == curses.KEY_RIGHT:
			print("MOVING RIGHT")
			GPIO.output(in1,GPIO.HIGH)
			GPIO.output(in2,GPIO.LOW)
			GPIO.output(in3,GPIO.LOW)
			GPIO.output(in4,GPIO.LOW)
			char4 = screen.getch()
			if char4 == curses.KEY_LEFT:
				print("STOPPED")
				GPIO.output(in1,GPIO.LOW)
				GPIO.output(in2,GPIO.LOW)
				GPIO.output(in3,GPIO.LOW)
				GPIO.output(in4,GPIO.LOW)
		if char == ord(' '):
			print("BRAKE")
			GPIO.output(in1,GPIO.LOW)
			GPIO.output(in2,GPIO.LOW)
			GPIO.output(in3,GPIO.LOW)
			GPIO.output(in4,GPIO.LOW)
		if char == curses.KEY_LEFT:
			print("MOVING LEFT")
			GPIO.output(in1,GPIO.LOW)
			GPIO.output(in2,GPIO.LOW)
			GPIO.output(in3,GPIO.HIGH)
			GPIO.output(in4,GPIO.LOW)
			char5 = screen.getch()
			if char5 == curses.KEY_RIGHT:
				print("STOPPED")
				GPIO.output(in1,GPIO.LOW)
				GPIO.output(in2,GPIO.LOW)
				GPIO.output(in3,GPIO.LOW)
				GPIO.output(in4,GPIO.LOW)

		if char == ord('q'):
			GPIO.cleanup()
			break
finally:
		curses.nocbreak();screen.keypad(0);curses.echo()
		curses.endwin()
