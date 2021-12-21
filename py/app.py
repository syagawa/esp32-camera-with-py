#!/usr/bin/python3

import asyncio
from interface.key import start_standby, key_names
from interface.terminal import start_terminal
from interface.screen import make_screen
from controller import connect

screen = None

states = {
  "in": False,
  "out": False,
  "waiting": False,
}

def get_state():
  key = None
  for k, v in states:
    if v == True:
      key = k
      break
  return key

def set_state(key, b):
  _bool = bool(b)
  if key in states:
    states[key] = _bool


def key_callback(pin, state):
  name = key_names[pin]
  screen.add("%s, %s, %s" % (name, pin, state))

def main():
  global screen
  screen = make_screen()
  screen.add("start app!")
  loop = asyncio.get_event_loop()
  loop.run_until_complete(start_standby(None, key_callback))
  loop.run_until_complete(connect())

if __name__ == "__main__":
  main()