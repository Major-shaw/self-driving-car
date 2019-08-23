import Rpi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

TRIG = 17
ECHO = 27
led = 22

m11 = 16
m12 = 12
m21 = 21
m22 = 20

en1 = 2
en2 = 3

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(m11, GPIO.OUT)
GPIO.setup(m12, GPIO.OUT)
GPIO.setup(m22, GPIO.OUT)
GPIO.setup(en1, GPIO.OUT)
GPIO.setup(en2, GPIO.OUT)

p1 = GPIO.PWM(en1, 100)
p2 = GPIO.PWM(en2, 100)

GPIO.output(led, 1)

time.sleep(5)

p1.start(100)
p2.start(100)

def stop :
    print('STOP')
    GPIO.output(m11, 0)
    GPIO.output(m12, 0)
    GPIO.output(m21, 0)
    GPIO.output(m22, 0)

def forward :
    print('FORWARD')
    GPIO.output(m11,1)
    GPIO.output(m12,0)
    GPIO.output(m21,1)
    GPIO.output(m22,0)

def back :
    print('BACK')
    GPIO.output(m11,0)
    GPIO.output(m12,1)
    GPIO.output(m21,0)
    GPIO.output(m22,1)

def right :
    print('RIGHT')
    p1.ChangeDutyCycle(50)
    p2.ChangeDutyCycle(50)
    GPIO.output(m11,1)
    GPIO.output(m12,0)
    GPIO.output(m21,0)
    GPIO.output(m22,0)


def left :
    print('LEFT')
    p2.ChangeDutyCycle(50)
    p2.ChangeDutyCycle(50)
    GPIO.output(m11,0)
    GPIO.output(m12,0)
    GPIO.output(m21,1)
    GPIO.output(m22,0)

stop()
count = 0

while True :
    GPIO.output(TRIG, False)
    time.sleep(0.1)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO) == 0 :
        GPIO.output(led, False)
    duration_start = time.time()

    while GPIO.input(ECHO) == 1 :
        GPIO.output(led, 1)

    duration_end = time.time()
    duration = duration_end - duration_start
    distance = duration * 17150

    print(distance)
    flag = 0

    if distance < 40 :
        count = count + 1
        stop()
        time.sleep(1)
        back()
        time.sleep(1.5)

        if (count % 3 == 1) and (flag == 0) :
            right()
            flag = 1

        else :
            left()
            flag = 0

        time.sleep(1.5)
        stop()
        time.sleep(1)

    else :
        forward()
        flag = 0

p1.stop()
p2.stop()
