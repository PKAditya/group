import RPi.GPIO as GPIO
import curses
import time
import rospy
from time import sleep
from std_msgs.msg import String

pub=rospy.Publisher('talker',String,queue_size=20)
rospy.init_node('talker',anonymous=True)

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
k='working'
rospy.loginfo(k)
pub.publish(k)

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
GPIO.output(in2,GPIO.LOW)

def forward():
    f1='UP ARROW KEY IS PRESSED'
    f2='MOVING FORWARD'
    rospy.loginfo(f1)
    pub.publish(f1)
    rospy.loginfo(f2)
    pub.publish(f2)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)

def backward():
    b1='DOWN ARROW KEY IS PRESSED'
    b2='MOVING BACKWARD'
    rospy.loginfo(b1)
    pub.publish(b1)
    rospy.loginfo(b2)
    pub.publish(b2)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
def right():
    r1='RIGHT ARROW KEY IS PRESSED'
    r2='TURNING RIGHT'
    rospy.loginfo(r1)
    pub.publish(r1)
    rospy.loginfo(r2)
    pub.publish(r2)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
def left():
    l1='LEFT ARROW KEY IS PRESSED'
    l2='TURNING LEFT'
    rospy.loginfo(l1)
    pub.publish(l1)
    rospy.loginfo(l2)
    pub.publish(l2)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
def back_right():
    br1='RIGHT ARROW KEY IS PRESSED'
    br2='TURNING RIGHT BACKWARDS'
    rospy.loginfo(br1)
    pub.publish(br1)
    rospy.loginfo(br2)
    pub.publish(br2)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)

def back_left():
    bl1='LEFT ARROW KEY IS PRESSED'
    bl2='TURNING LEFT BACKWARDS'
    rospy.loginfo(bl1)
    pub.publish(bl1)
    rospy.loginfo(bl2)
    pub.publish(bl2)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
def brake():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)

try:
    while True:
        char = screen.getch()
        stop='STOPPED'
        if char == ord('s'):
            S = 'Starting Star Shape'
            rospy.loginfo(S)
            pub.publish(S)
            right()
            sleep(0.3)
            brake()
            sleep(0.5)
            forward()
            sleep(1.5)
            brake()
            sleep(0.5)
            back_left()
            sleep(0.4)
            brake()
            sleep(0.5)
            backward()
            sleep(1.5)
            brake()
            sleep(0.5)
            left()
            sleep(0.4)
            brake()
            sleep(0.5)
            forward()
            sleep(1.5)
            brake()
            sleep(0.5)
            back_left()
            sleep(0.4)
            brake()
            sleep(0.5)
            backward()
            sleep(1.5)
            brake()
            sleep(0.5)
            left()
            sleep(0.4)
            brake()
            sleep(0.5)
            forward()
            sleep(1.5)
            brake()
            sleep(0.5)
        if char == ord('t'):
            T = 'Starting Triangle Shape'
            rospy.loginfo(T)
            pub.publish(T)
            right()
            sleep(0.3)
            brake()
            sleep(0.5)
            forward()
            sleep(1.5)
            brake()
            sleep(0.5)
            back_left()
            sleep(0.6)
            brake()
            sleep(0.5)
            backward()
            sleep(1.5)
            brake()
            sleep(0.5)
            left()
            sleep(0.6)
            brake()
            sleep(0.5)
            forward()
            sleep(1.5)
            brake()
        if char == ord('r'):
            R = 'Drawing Triangle Shape'
            rospy.loginfo(R)
            pub.publish(R)
            forward()
            sleep(1.25)
            brake()
            sleep(0.5)
            right()
            sleep(1)
            brake()
            sleep(0.5)
            forward()
            sleep(2)
            right()
            sleep(1)
            brake()
            sleep(0.5)
            forward()
            sleep(1.25)
            brake()
            sleep(0.5)
            right()
            sleep(1)
            brake()
            sleep(0.5)
            forward()
            sleep(2)
            brake()
        if char == ord('a'):
            A = 'Drawing Square shape'
            rospy.loginfo(A)
            pub.publish(A)
            forward()
            sleep(1.5)
            brake()
            sleep(0.5)
            right()
            sleep(1)
            brake()
            sleep(0.5)
            forward()
            sleep(1.5)
            brake()
            sleep(0.5)
            right()
            sleep(1)
            brake()
            sleep(0.5)
            forward()
            sleep(1.5)
            brake()
            sleep(0.5)
            right()
            sleep(1)
            brake()
            sleep(0.5)
            forward()
            sleep(1.5)
            brake()
            sleep(0.5)
        if char == ord('h'):
            forward()
            sleep(1)
            brake()
            sleep(0.5)
            back_left()
            sleep(1.3)
            brake()
            sleep(0.5)
            backward()
            sleep(1)
            brake()
            sleep(0.5)
            left()
            sleep(1.3)
            brake()
            sleep(0.5)
            forward()
            sleep(1)
            brake()
            sleep(0.5)
            back_left()
            sleep(1.3)
            brake()
            sleep(0.5)
            backward()
            sleep(1)
            brake()
            sleep(0.5)
            left()
            sleep(1.3)
            brake()
            sleep(0.5)
            forward()
            sleep(1)
            brake()
            sleep(0.5)
            back_left()
            sleep(1.3)
            brake()
            sleep(0.5)
            backward()
            sleep(1)
            brake()
            sleep(0.5)
        if char == curses.KEY_UP:
       	    forward()
            char2 = screen.getch()
            if char2 == curses.KEY_DOWN:
                brake()
                sleep(0.5)
                backward()
                char3 = screen.getch()
                if char3 == ord(' '):
                    brake()
                    rospy.loginfo(stop)
                    pub.publish(stop)
            if char2 == curses.KEY_RIGHT:
                brake()
                sleep(0.5)
                right()
                char4 = screen.getch()
                if char4 == ord(' '):
                    brake()
                    rospy.loginfo(stop)
                    pub.publish(stop)
            if char2 == curses.KEY_LEFT:
                brake()
                sleep(0.5)
                left()
                char5 = screen.getch()
                if char5 == ord(' '):
                    brake()
                    rospy.loginfo(stop)
                    pub.publish(stop)
            if char2 == ord(' '):
                brake()
                rospy.loginfo(stop)
                pub.publish(stop)
        if char == curses.KEY_RIGHT:
            right()
            char6 = screen.getch()
            if char6 == curses.KEY_UP:
                brake()
                sleep(0.5)
                forward()
                char7 = screen.getch()
                if char7 == ord(' '):
                    brake()
                    rospy.loginfo(stop)
                    pub.publish(stop)
            if char6 == curses.KEY_DOWN:
                brake()
                sleep(0.5)
                backward()
                char8 = screen.getch()
                if char8 == ord(' '):
                    brake()
                    rospy.loginfo(stop)
                    pub.publish(stop)
            if char6 == curses.KEY_LEFT:
                brake()
                sleep(0.5)
                left()
                char9 = screen.getch()
                if char9 == ord(' '):
                    brake()
                    rospy.loginfo(stop)
                    pub.publish(stop)
            if char6 == ord(' '):
                brake()
                rospy.loginfo(stop)
                pub.publish(stop)
        if char == curses.KEY_LEFT:
            left()
            char10 = screen.getch()
            if char10 == curses.KEY_UP:
                brake()
                sleep(0.5)
                forward()
                char11 = screen.getch()
                if char11 == ord(' '):
                    brake()
                    rospy.loginfo(stop)
                    pub.publish(stop)
            if char10 == curses.KEY_DOWN:
                brake()
                sleep(0.5)
                backward()
                char12 = screen.getch()
                if char12 == ord(' '):
                    brake()
                    rospy.loginfo(stop)
                    pub.publish(stop)
            if char10 == curses.KEY_RIGHT:
                brake()
                sleep(0.5)
                right()
                char13 = screen.getch()
                if char13 == ord(' '):
                    brake()
                    rospy.loginfo(stop)
                    pub.publish(stop)
            if char10 == ord(' '):
                brake()
                rospy.loginfo(stop)
                pub.publish(stop)
        if char == curses.KEY_DOWN:
            backward()
            char14 = screen.getch()
            if char14 == curses.KEY_UP:
                brake()
                sleep(0.5)
                forward()
                char15 = screen.getch()
                if char15 == ord(' '):
                    brake()
                    rospy.loginfo(stop)
                    pub.publish(stop)
            if char14 == curses.KEY_RIGHT:
                brake()
                sleep(0.5)
                back_right()
                char16 = screen.getch()
                if char16 == curses.KEY_LEFT:
                    brake()
                    sleep(0.5)
                    back_left()
                    char17 = screen.getch()
                    if char17 == ord(' '):
                        brake()
                        rospy.loginfo(stop)
                        pub.publish(stop)
                if char16 == ord(' '):
                    brake()
                    rospy.loginfo(stop)
                    pub.publish(stop)
            if char14 == curses.KEY_LEFT:
                brake()
                sleep(0.5)
                back_left()
                char17 = screen.getch()
                if char17 == curses.KEY_RIGHT:
                    brake()
                    sleep(0.5)
                    back_right()
                    char18 = screen.getch()
                    if char18 == ord(' '):
                        brake()
                        rospy.loginfo(stop)
                        pub.publish(stop)
                if char17 == ord(' '):
                    brake()
                    rospy.loginfo(stop)
                    pub.publish(stop)
            if char14 == ord(' '):
                brake()
                rospy.loginfo(stop)
                pub.publish(stop)
finally:
    curses.nocbreak();screen.keypad(0);curses.echo()
    curses.endwin()
    GPIO.cleanup()

