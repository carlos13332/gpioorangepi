import OPi.GPIO as GPIO
#sudo pip3 install OrangePi.GPIO

GPIO.setboard(GPIO.ZERO)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

servo = GPIO.PWM(7, 50)
servo.start(0)

while True:
    duty = int(input("Enter a value from 2 to 12: "))
    servo.ChangeDutyCycle(duty)
