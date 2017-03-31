import os
import subprocess
import winreg
from config import header, bar
import binascii

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
        print(stringData)

    except Exception as e:
        print(e)
