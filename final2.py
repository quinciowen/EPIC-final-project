import RPi.GPIO as GPIO
import pygame
from pygame import mixer
import time
import random
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setwarnings(GPIO.BOARD)# this makes all of the setups for warnings and all of the imports oragnized at the top of the screen


GPIO.setup(5, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # sets up the GPIO pin that the touch sensor is connected to


songlist = ['song1.mp3', 'song2.mp3', 'song3.mp3', 'song4.mp3'] # list of the songs that I chose

q = len(songlist)
a = random.randint(0, q) # this is the random song generator, it chooses one from the list at random
m = songlist[a]
if m == 'song1.mp3':
    i = 380
if m == 'song2.mp3': # these are the lengths of the songs in seconds so it plays the whole song
    i = 240
if m == 'song3.mp3':
    i = 30
if m == 'song4.mp3':
    i = 224

while True:
    if GPIO.input(5) == GPIO.HIGH: #starts the song when the touch sensor is pushed
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(m)
        pygame.mixer.music.play()
        time.sleep(i) # i is the number of seconds the song is before it turns off
        print('song is over')
        exit() # exits out of pygame

    

      
