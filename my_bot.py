from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *

class coordinates:
    replay_btn = (341,415)
    dino_head = (162,423)


def restart():
    pyautogui.click(coordinates.replay_btn)
    pyautogui.keyDown('down')

def jump():
    pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    print("       it jumped  hurray")
    time.sleep(0.18)
    pyautogui.keyUp('space')
    pyautogui.keyDown('down')

def Grab():
    im = ImageGrab.grab(bbox=(225,400,290,465))
    # im.show()
    grayImage = ImageOps.grayscale(im)
    a = array(grayImage.getcolors())
    print(a.sum())
    return a.sum()


def main():
    restart()
    while True:
        if (Grab() != 4555):
            jump()
            # time.sleep(0.1)

main()
