import os
import subprocess
import winreg
from config import header, bar
import binascii
import re

# hard coded for windows 10, magic value = '10ts'

shimCachePath = "CurrentControlSet\Control\Session Manager\AppCompatCache"

if __name__ == "__main__":
    print(header)
    try:
        registry = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
        system = winreg.OpenKey(registry, r'SYSTEM')

        key = winreg.OpenKey(system, shimCachePath)
        binary = winreg.QueryValueEx(key,'AppCompatCache')[0]

        stringData = str(binary)

        #remove null bytes (this is really funky I know)
        stringData = stringData.replace('\\x00', '')
        #remove hex character escape
        stringData = stringData.replace('\\x', '')

        f = open("exeList.txt", 'w+')
        for start in range(0, len(stringData)):
            # if we have a start of a file path
            if stringData[start:start+2] == 'C:':
                # windows maximum file path length is 260 TODO: account for //
                for end in range(0, 260):
                    if stringData[start + end: start + end + 4] == '.exe' or stringData[start + end: start + end + 4] == '.EXE':
                        f.write(stringData[start : start + end + 4].replace('\\\\', '\\') + '\n')
                        break
    except Exception as e:
        print(e)
