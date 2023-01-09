import pyautogui as inpu
import keyboard
import random
import time
import sys
a=["a","s","d","w"]

while True:
    if(keyboard.read_key("'a")):
        while True:
            if (keyboard.is_pressed("+")):
                sys.exit(0)
            else:
                b=random.choice(a)
                inpu.keyDown(b)
                time.sleep(0.01)
                inpu.keyUp(b)
                time.sleep(5)
            
                
            
            
