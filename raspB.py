#author : Kunchala Anil(anilkunchalaece@gmail.com)
#Purpose : for Fiverr Gig
#Date : March 16 2016

import RPi.GPIO as GPIO #import the python Raspberry pi GPIO library
import time #import the python time library
import sys 

GPIO.setmode (GPIO.BOARD) # use the Board Numbers as GPIO numbers
GPIO.setwarnings(False) # Off the GPIO Warnings

#assign the pin Numbers to the Leds
GREEN_PIN = 3 
RED_PIN = 5
YELLOW_PIN = 7

#delayTime is the delay between On and Off of the Each LED
delayTime = 1
#intervalTime is the interval Between Two Led's
intervalTime = 1.5

while True : 
	GPIO.setup(GREEN_PIN,GPIO.OUT)#set the Theree GPIO pins as Output Ports
	GPIO.setup(RED_PIN,GPIO.OUT)
	GPIO.setup(YELLOW_PIN,GPIO.OUT)
	
	
	GPIO.output(GREEN_PIN,True)#On the  Green led
	time.sleep(delayTime) #wait for Some time
	GPIO.output(GREEN_PIN,False)#Off the led
	
	time.sleep(intervalTime)#wait for some time
	
	GPIO.output(RED_PIN,True)
	time.sleep(delayTime)
	GPIO.output(RED_PIN,False)
	
	time.sleep(intervalTime)
	
	GPIO.output(YELLOW_PIN,True)
	time.sleep(delayTime)
	GPIO.output(YELLOW_PIN,False)
	
	time.sleep(intervalTime)
