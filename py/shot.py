from time import sleep
import urllib.request
from datetime import datetime
import os

def shot(ip, dir):
  print("shot")
  # 1920 x 1080
  # framesize_params = {
  #   "var": "framesize",
  #   "val": "14"
  # }
  # quality_params = {
  #   "var": "quality",
  #   "val": "30"
  # }

  # 1280 x 720
  # framesize_params = {
  #   "var": "framesize",
  #   "val": "11"
  # }

  # 1600 x 1200
  # framesize_params = {
  #   "var": "framesize",
  #   "val": "10"
  # }

  params = {
    "fs": "1",
    "q": "4"
  }

  capture_url = f"http://{ip}/cap"
  status_url = f"http://{ip}/status"

  req_status = urllib.request.Request(status_url)
  print(req_status.full_url)

  # check status
  with urllib.request.urlopen(req_status) as res_status:
    status = res_status.read()
    print(status)

  req = urllib.request.Request('{}?{}'.format(capture_url, urllib.parse.urlencode(params)))

  # shot
  with urllib.request.urlopen(req) as res:
    body = res.read()
    t = datetime.now().isoformat()
    filename = "{0}/{1}.jpg".format(dir, t)
    with open(filename, mode='wb') as f:
      f.write(body)


def shots(count, interval, ip):
    t = datetime.now().isoformat()
    dir = "./images/{0}".format(t)
    os.makedirs(dir, exist_ok=True)
    print(f"Image Directory: {dir}")
    for i in range(count):
        shot(ip, dir)
        sleep(interval)
