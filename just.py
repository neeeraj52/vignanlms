import pywhatkit as kit
import pyautogui as pg


def sendmsg(hour, minut):
  kit.sendwhatmsg("+919866375031", "hello ma (sent from python)", hour, minut)
  pg.press("enter")
