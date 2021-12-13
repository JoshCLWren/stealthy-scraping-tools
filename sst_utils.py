import time
import os
import random
import json
import subprocess
from mouse import humanMove
from typing import humanTyping

def getPageSource():
  cmd = f'/usr/bin/node page_source.js'
  ps = subprocess.check_output(cmd, shell=True)
  return ps


def getCoords(selector, randomize_within_bcr=True):
  """
  Example: `node coords.js "li:nth-of-type(3) a"`
  """
  cmd = f'/usr/bin/node coords.js "{selector}"'
  coords = subprocess.check_output(cmd, shell=True)
  parsed = json.loads(coords)

  x = parsed['x']
  y = parsed['y']

  if randomize_within_bcr:
    x += random.randrange(0, int(parsed['width']))
    y += random.randrange(0, int(parsed['height']))

  return x, y


def startBrowser(address_bar):
  os.system('google-chrome --remote-debugging-port=9222 --start-maximized --disable-notifications &')
  time.sleep(4)

  # visit https://bot.incolumitas.com/#botChallenge
  humanMove(168, 79)
  time.sleep(random.uniform(0.5, 1.5))
  humanTyping(address_bar, speed=(0.005, 0.008))
  time.sleep(random.uniform(1.5, 2.5))