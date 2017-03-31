import os
os.system('python get-pip.py')
#execfile('get-pip.py')
# ^^ if the first one doesn't work
os.system("apt-get install python")
os.system("pip2 install -r requirements.txt")
os.system("pip install -r requirements.txt")
print "Installed! Now just run the PySE file!"
raw_input("")
