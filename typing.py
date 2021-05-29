import pyautogui
import random
import time

def tinySleep():
  time.sleep(random.uniform(0.005, 0.009))


def doubleHit(key1, key2):
  """
  Sometimes press two keys down at the same time and randomize the 
  order of the corresponding key up events to resemble 
  human typign closer.
  """
  pyautogui.keyDown(key1)
  tinySleep()
  pyautogui.keyDown(key2)
  tinySleep()
  if random.random() > 0.5:
    pyautogui.keyUp(key1)
    tinySleep()
    pyautogui.keyUp(key2)
  else:
    pyautogui.keyUp(key2)
    tinySleep()
    pyautogui.keyUp(key1)


def humanTyping(text, speed=(0.007, 0.01), doubleHit=True):
  """
  Mostly the keydown/keyup pairs are in order, but
  sometimes we want two keydown's at the same time.

  text: the text to be written in a human fashion.

  speed: the gap between key presses in seconds. Random number between
    (low, high)
  """
  i = 0
  while i <= len(text):
    if speed:
      time.sleep(random.uniform(*speed))
    if doubleHit is True and random.random() < .3 and i+1 < len(text):
      doubleHit(text[i], text[i+1])
      i += 2
    else:
      pyautogui.keyDown(text[i])
      tinySleep()
      pyautogui.keyUp(text[i])
      i += 1

    if i >= len(text):
      break