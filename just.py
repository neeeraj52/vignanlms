import pywhatkit as kit
import pyautogui as pg
import os


def sendmsg(hour, minut):
  kit.sendwhatmsg("+919866375031", "hello ma (sent from python)", hour, minut)
  pg.press("enter")
  os.system("Xyfb :1 -screen 0 720X20X16 &")
  os.environ["DISPLAY"] = ":1.0"
