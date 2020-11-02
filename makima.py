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
ver = 'Makima FM Version 0.0.0'
Info = f'{ver}. Type "help" for more information.'
commands = sorted(('open', 'ls', 'cd', 'write', 'ren', 'del', 'mov', 'make', 'cop', 'help'))
print(''.ljust(135, '-'))
print(''.ljust(135, '*'))
print(name)
print(''.ljust(135, '*'))
print(''.ljust(135, '-'))
print(Info)
print('Press "Enter" to exit, and "info" to see commands ...')
print()

x = None
while True:
      print(os.getcwd() + ' ~')
      print( '>>  ', end = '')
      x = input().split()
      print(''.ljust(len(os.getcwd()),'~'))


      if x == []:
          break
      elif x[0] == 'make' :
        made_path = os.path.join(os.getcwd(), x[1])
        os.makedirs(made_path)
        print(x[1], 'has been created in', os.getcwd())

      elif x[0] == 'write' :
        pass
      elif x[0] == 'ren' :
        pass
      elif x[0] == 'del' :
        pass
      elif x[0] == 'mov' :
        pass
      elif x[0] == 'cop' :
        pass
      elif x[0] == 'ls' :
        for i in os.listdir() :
            size = os.path.getsize(os.path.join(os.getcwd(), i))
            if '-s' in x :
                if 'M' in x:
                    print((str(round(size/1000000, 3)).rjust(10) + ' M-Bytes'.rjust(5)).ljust(20), end= '')
                    print(i)
                elif 'K' in x:
                    print((str(round(size/1000, 3)).rjust(10) + ' K-Bytes'.rjust(5)).ljust(20), end= '')
                    print(i)
                elif 'G' in x:
                    print((str(round(size/1000000000, 3)).rjust(10) + ' G-Bytes'.rjust(5)).ljust(20), end= '')
                    print(i)
                else:
                    print((str(size).rjust(10) + ' Bytes'.rjust(5)).ljust(20), end= '')
                    print(i)
            else:
                print(i, end = ' || ')
        print()
      elif x[0] == 'cd':
          if 'C:' in x :
              x[x.index('C:')] = 'C:\\'
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
          try:
            i = ' '.join(x[1:])
            new = os.path.join(os.getcwd(), i)
            Fil = open(new).read()
            print()
            print(r'==='*30)
            print(r'-*-'*30)
            print(Fil)
            print(r'-*-'*30)
            print(r'==='*30)
          except :
            print('Error: Invalid file selected')
      elif x[0] == 'info' :
          print(commands)
          print('To view more info on commands, type "help"')  
      else:
          print('Error: Not a valid command!')
      print()

print('End ...')
print()