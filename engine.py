import optparse
import time
import requests
import datetime
import random
from constants import *
from secrets import access_token, device
domain = "https://api.particle.io/v1/devices/{0}/{1}"


#get command line args
def args(i):

#instantiate parser
    parser=optparse.OptionParser()
#Add additional arguments following the structure of the line below
    parser.add_option('--illini',action="store",dest="i",help="0=illini forward, 1=illini backward, 2=Blue",default="0")
#send args to variables
    options, args=parser.parse_args()
    i=int(options.i)
    return i

def main():
#define globals for args
  i=0
#get command line args
  i=args(i)
  print "debug i after args()",i
  clear_strip()
  while True:
    colors = [orange, blue, black, orange, blue]
    if i == 0:
      illinois_forwards()
    if i == 1:
      illinois_backwards()
      i = i + 1
    if(i == 2):
      colors=[blue]
      light_strip_forwards(colors,30)


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
