#!/usr/bin/env python3
import os, shutil, zipfile, re

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
commands = sorted(('read', 'ls', 'check', 'search', 'cd', 'write', 'zip', 'unzip', 'ren', 'del', 'mov', 'make', 'cop', 'help'))
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
      elif x[0] == 'check' :
        print(os.path.exists(os.path.join(os.getcwd(), x[1]))) 
      elif x[0] == 'write' :
        new = os.path.join(os.getcwd(), x[1])
        Fil = open(new, 'a')      
        Fil.write(' '.join(x[2:]) + '\n') 
        Fil.close()      
        
      elif x[0] == 'ren' :
        m_file = shutil.move(x[1], x[2])
        print(f'File renamed to {m_file}')

      elif x[0] == 'del' :
        val = input('Are you sure you want PERMANENTLY to delete the file? ( y or n ): ')
        if val.lower() == 'y':
          if x[1] == '-r':
            shutil.rmtree(x[-1])
          else:
            os.unlink(x[-1])
          print(f'{os.path.abspath(x[-1])} deleted')
        else:
          pass

      elif x[0] == 'mov' :
        print('afsdasdf')
        val = input(f'Are you sure you want to move {x[1]} to {x[2]}? (Type Y or N): ')
        if val.lower() == 'y':
          m_file = shutil.move(x[1], x[2])
          print(f'{os.path.abspath(m_file)} moved')
        else:
          pass

      elif x[0] == 'cop' :
        if x[1] == '-r':
          c_file = shutil.copytree(x[-2], x[-1])
          print(f'{os.path.abspath(c_file)} copied')
        else:
          c_file = shutil.copy(x[-2], x[-1])
          print(f'{os.path.abspath(c_file)} copied')
      
      elif x[0] == 'search':
        files = os.listdir()
        if x[1] == 'exact':
          result = [i for i in files if re.match(x[-1], i) ]
        else:
          result = [i for i in files if re.search(x[-1], i) ]
        print(result)

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

      elif x[0] == 'zip':
        file = zipfile.ZipFile(x[-1] + '.zip', 'w')
        file.write(x[-1], compress_type = zipfile.ZIP_DEFLATED)
        file.close()

      elif x[0] == 'unzip':
        file = zipfile.ZipFile(x[-1])
        if len(x) == 3:
          file.extractall(x[1])
        else:
          file.extractall()
        file.close()

      elif x[0] == 'read' : 
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
            open(new).close()
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