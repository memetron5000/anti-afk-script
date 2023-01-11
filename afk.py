import pyautogui as inpu
import keyboard
import random
import time
import sys
import _thread 
import threading
a=["a","s","d","w"]


def breakout():
    while True:
        if (keyboard.is_pressed("+")):
            sys.exit(randomizer) #parte a remplazar que rompa la funcion
def randomizer():
    while True:
        if(keyboard.read_key("-")):
            while True:
                b=random.choice(a)
                inpu.keyDown(b)
                time.sleep(random.randrange(2,5))
                inpu.keyUp(b)


p1 = threading.Thread(target=randomizer)
p2 = threading.Thread(target=breakout)

p1.start()
p2.start()
            
                
            
            
