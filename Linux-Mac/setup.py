#!/usr/bin/env python
from subprocess import call
import platform
import os
W = '\033[0m'     # white (normal)
R = '\033[31m'    # red
G = '\033[32m'    # green
O = '\033[33m'    # orange
B = '\033[34m'    # blue
P = '\033[35m'    # purple
C = '\033[36m'    # cyan
LR = '\033[1;31m' # light red
LG = '\033[1;32m' # light green
LO = '\033[1;33m' # light orange
LB = '\033[1;34m' # light blue
LP = '\033[1;35m' # light purple
LC = '\033[1;36m' # light cyan

user_id = os.getuid()
if(user_id != 0):
    print LR + '[!] Must run install script as root' + W
installed = open("other/installed.txt", 'r')
if(installed == 'yes'):
    pass
else:
    if(platform.system() == "Linux" or platform.system() == "Darwin"):
        call("sudo easy_install pip", shell=True)
        import pip
        pip.main(['install', '-r', 'requirements.txt'])
        install_dir = "/usr/share/pySE"
        if not os.path.exists(install_dir):
            os.makedirs(install_dir)
        call("sudo cp -R * /usr/share/pySE", shell=True)
        call("sudo mv /usr/share/pySE/pyse.sh /usr/bin/pyse && chmod +x /usr/bin/pyse", shell=True)
        install = open("other/installed.txt", "w")
        install.write("yes")
        install.close()
    else:
        print LR + "[!] Not supported by pySE yet. Use Mac or Linux :/"
print LG + "[*] Run 'pyse' from commmand line to run the tool" + W
