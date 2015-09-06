import time
import requests
import datetime
import random
from constants import *
from secrets import access_token, device
domain = "https://api.particle.io/v1/devices/{0}/{1}"

def main():
  i = 0
  clear_strip()
  while True:
    colors = [orange, blue, black, orange, blue]
    if i % 2 == 0:
      illinois_forwards()
    else:
      illinois_backwards()
    i = i + 1

def illinois_forwards():
  return light_strip_forwards(illinois, 30)

def illinois_backwards():
  return light_strip_backwards(illinois, 30)

def light_strip(colors):
  return send_request(colors, "color")

def clear_strip():
  return send_request([black], "color")

def light_strip_forwards(colors, delay):
    return send_request([str(delay)] + colors, "forwards")  

def light_strip_backwards(colors, delay):
    return send_request([str(delay)] + colors, "backwards")

def send_request(colors, endpoint):
  payload = {'access_token' : access_token, 'args' : ",".join(colors)}
  response = requests.post(get_url(endpoint), data = payload)
  print str(datetime.datetime.now()) + "\t : \t" + str(payload)
  print str(datetime.datetime.now()) + "\t : \t" + response.text


def get_url(endpoint):
  if endpoint not in ['color', 'forwards', 'backwards']:
    raise NameError(str(endpoint) + " is not a valid endpoint")
  return domain.format(device, endpoint);

if __name__ == '__main__':
  main()