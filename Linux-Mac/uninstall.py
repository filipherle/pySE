import os
import shutil
import sys
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
T  = '\033[93m' # tan
M = '\033[1;35;32m' # magenta

main = raw_input (''+T+'Do you really want to uninstall PySE?>'+W+'')
if main == "yes" or "y" or "Yes" or "Y":
    try:
        shutil.rmtree('/usr/share/pySE')
        os.remove('/usr/bin/pyse')
        print (''+G+'Successfully Removed!'+W+'')
    except:
        print (''+R+'PySE is already uninstalled or not yet installed!'+W+'')
else:
    print (''+G+'Okay!'+W+'')
    sys.exit()
