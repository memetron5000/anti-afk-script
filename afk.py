import pyautogui as inpu
import keyboard
import random
import time
import sys
a=["a","s","d","w"]
c=True
while True:
    if(keyboard.read_key("-")):
        while c==True:
            if (keyboard.is_pressed("+")):
                sys.exit(0)
            else:
                b=random.choice(a)
                inpu.keyDown(b)
                time.sleep(1)
                inpu.keyUp(b)
            
                
            
            
