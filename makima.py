#!/usr/bin/env python3
import os

name = r"""
  __  __           _      _                         ______   _   _            __  __
 |  \/  |         | |    (_)                       |  ____| (_) | |          |  \/  |
 | \  / |   __ _  | | __  _   _ __ ___     __ _    | |__     _  | |   ___    | \  / |   __ _   _ __     __ _    __ _    ___   _ __
 | |\/| |  / _` | | |/ / | | | '_ ` _ \   / _` |   |  __|   | | | |  / _ \   | |\/| |  / _` | | '_ \   / _` |  / _` |  / _ \ | '__|
 | |  | | | (_| | |   <  | | | | | | | | | (_| |   | |      | | | | |  __/   | |  | | | (_| | | | | | | (_| | | (_| | |  __/ | |
 |_|  |_|  \__,_| |_|\_\ |_| |_| |_| |_|  \__,_|   |_|      |_| |_|  \___|   |_|  |_|  \__,_| |_| |_|  \__,_|  \__, |  \___| |_|
                                                                                                                __/ |
                                                                                                               |___/
                                                                                                               """


def hl():
    # Header
    print(f'       {ver}'.ljust(50), end='')
    print(f'{auth}')
    print()
    # Synopsis

    # Description
    pass
auth = 'AJIBOLA ONAOPEMIPO'
ver = 'Makima FM version 0.0.0'
Info = f'{ver}. Type "help" for more information'
print(''.ljust(135, '-'))
print(''.ljust(135, '*'))
print(name)
print(''.ljust(135, '*'))
print(''.ljust(135, '-'))
print(Info)
print()

x = None
while True:
      print(os.getcwd() + ' >>  ', end = '')
      x = input().split()
      print(''.ljust(len(os.getcwd()),'~'))


      if x == []:
          break
      elif x[0] == 'ls' :
          if '-s' in x :
            for i in os.listdir() :
              print(i.ljust(55), end = '')
              print(str(os.path.getsize(os.path.join(os.getcwd(), i))) + ' Bytes')
          else:
              for i in os.listdir() :
                  print(i.ljust(10), end = '')
          print()
      elif x[0] == 'cd':
          try:
              for i in x[1:]:
                  new = os.path.join(os.getcwd(), i)
                  os.chdir(new)
          except :
              print('Error: Invalid directory selected')
              print()
              continue
      elif x[0] == 'help':
          hl()
      elif x[0] == 'open' : 
          i = x[1]
          new = os.path.join(os.getcwd(), i)
          print(r'-*-'*30)
          print(open(new).read())
          print(r'-*-'*30)

      else:
          print('Error: Invalid command!')
      print()

print('End ...')
