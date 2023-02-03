import subprocess, time, sys, os, re, urllib, requests, json
from termcolor import colored
from tqdm import tqdm
import colorama
from colorama import Fore, Back, Style
os.system('clear')
colorama.init(autoreset=True)
print(Style.BRIGHT + Fore.RED + """
 _____         ___ _ _        
|  _  |___ ___|  _|_| |___ ___ 
|   __|  _| . |  _| | | -_|  _|
|__|  |_| |___|_| |_|_|___|_|  
""")

print(Fore.BLUE + """
Osint investigation tool
lookup online public data of a person anonymously 🥸👻
""")
time.sleep(3)
first_name = str(input("[+] first name: "))
last_name = str(input("[+] last name: "))
os.system('echo "name: '+first_name+' '+last_name+'" >> names.txt')
print(Fore.BLUE + "gathering information on target")
os.system('w3m -dump https://www.spokeo.com/'+first_name+'-'+last_name+'?loaded=1 > output.txt')
print(Fore.BLUE + "finding social media profiles 🌐👨‍👩‍👦")
os.system('google "'+first_name+' '+last_name+'" > socials.txt')
time.sleep(1)
print(Fore.BLUE + "getting your infomation ready!")
time.sleep(4)
for _ in tqdm(range(200),
    desc = "PROFILER ",
    ascii = False,ncols=100):
    time.sleep(0.2)

def menu():
    print(Fore.BLUE + """
=OSINT=MODULES==================================================================
  ├──[1] names
  ├──[2] location
  ├──[3] past locations
  ├──[4] family
  ├──[5] other names she or he goes by
  └──[6] personal data included
=ADD=MODULES====================================================================
  ├──[7] add the persons state to get better and closer results
  ├──[8] add the persons region to get exact/closer results
  ├──[9] add the persons email to get to see if the password is available
  └──[10] add phone number to get the address/names/location
=DUMP=MODULES===================================================================
    ├──[11] dump location of the phone number
    ├──[12] dump all Related Phone Number addresses
    ├──[13] dump all Related Phone Number names from the addresses
    └──[14] dump email results
=SOCIAL=PROFILES================================================================
        ├──[15] social media profiles
        └──[99] exit
    """)
    selection=int(input(Style.BRIGHT + Fore.RED + "[+] "+first_name+" "+last_name+": "))
    if selection==1:
        names()
    elif selection==2:
          location()
    elif selection==3:
          past_locations()
    elif selection==4:
          related_to()
    elif selection==5:
          go_by()
    elif selection==6:
          Includes()
    elif selection==7:
          add_location()
    elif selection==8:
          add_region()
    elif selection==9:
          addemail()
    elif selection==10:
          add_phonenumber()
    elif selection==11:
          dump_place()
    elif selection==12:
          dump_address()
    elif selection==13:
          dump_names()
    elif selection==14:
          email_results()
    elif selection==15:
          socials()
    elif selection==99:
          exit
    else:
        print(Fore.BLUE + "not a option")
        menu()

def names():
    print(Fore.GREEN + "[+] finding all possible names of "+first_name+" "+last_name+"")
    time.sleep(4)
    f = open("output.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match(first_name, line):
          print(Style.BRIGHT + Fore.BLUE + "[🥸👉] "+line)
    menu()

def location():
    print(Fore.GREEN + "[+] finding all the possible locations of "+first_name+" "+last_name+"")
    time.sleep(4)
    f = open("output.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Resides in", line):
          print(Style.BRIGHT + Fore.YELLOW + "[🌍] "+line)
    menu()

def past_locations():
    print(Fore.GREEN + "[+] finding all the possible last locations of "+first_name+" "+last_name+"")
    time.sleep(5)
    f = open("output.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Lived", line):
          print(Style.BRIGHT + Fore.YELLOW + "[🌐 geo] "+line)
    menu()

def related_to():
    print(Fore.GREEN + "[+] finding all possible family members of "+first_name+" "+last_name+"")
    time.sleep(6)
    f = open("output.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Related", line):
          print(Style.BRIGHT + Fore.YELLOW + "[👨‍👩‍👦] "+line)
    menu()

def go_by():
    print(Fore.GREEN + "[+] finding all possible other names "+first_name+" "+last_name+" goes by")
    time.sleep(4)
    f = open("output.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Also known", line):
          print(Style.BRIGHT + Fore.YELLOW + "[🧐] "+line)
    menu()

def Includes():
    print(Fore.GREEN + "[+] finding all possible person info Included on "+first_name+" "+last_name+"")
    time.sleep(3)
    f = open("output.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Includes", line):
          print(Style.BRIGHT + Fore.YELLOW + "[🧐] "+line)
    menu()

def add_location():
    print(Fore.BLUE + "type the state she/he lives in")
    time.sleep(2)
    print(Style.BRIGHT + Fore.RED + """AL - alabama
AK - alaska
AZ - arizona
AR - arkansas
CA - california
CO - colorado
CT - connecticut
DE - delaware
DC - district of columbia
FL - florida
GA - Georgia
HI - hawaii
ID - idaho
IL - illinois
IN - indiana
IA - iowa
KS - kansas
KY - kentucky
LA - louisiana
ME - maine
MD - maryland
MA - massachusetts
MI - michigan
MN - minnesota
MS - mississippi
MO - missouri
MT - montana
NE - nebraska
NV - nevada
MH - new hampshire
NJ - new jersey
NM - new mexico
NY - new york
NC - north carolina
ND - north dakota
OH - ohio
OK - oklahoma
OR - oregon
PA - pennsylvania
PR - puerto rico
RI - rhode island
SC - south carolina
SD - south dakota
TN - tennessee
TX - texas
UT - utah
VT - vermont
VA - virginia
WA - washington
WV - west virginia
WI - wisconsin
WY - wyoming
    """)
    global location
    location = str(input(Fore.BLUE + "[+] add state: "))
    str(os.system('w3m -dump https://www.spokeo.com/'+first_name+'-'+last_name+'/'+location+' > output.txt'))
    print(Fore.BLUE + "==================")
    print(Style.BRIGHT + Fore.CYAN + first_name)
    print(Style.BRIGHT + Fore.CYAN + last_name)
    print(Style.BRIGHT + Fore.CYAN + location)
    print(Fore.BLUE + "==================")
    anykey=input(Fore.BLUE + "press enter")
    print(Style.BRIGHT + Fore.GREEN + "saved!")
    time.sleep(3)
    menu()

def add_region():
    print(Fore.BLUE + "[+] type the region were "+first_name+" "+last_name+" lives in to get better results")
    time.sleep(2)
    global region
    region = str(input(Fore.BLUE + "[+] add region: "))
    os.system('w3m -dump https://www.spokeo.com/'+first_name+'-'+last_name+'/'+location+'/'+region+' > output.txt')
    print(Fore.BLUE + "==================")
    print(Style.BRIGHT + Fore.CYAN + first_name)
    print(Style.BRIGHT + Fore.CYAN + last_name)
    print(Style.BRIGHT + Fore.CYAN + region)
    print(Fore.BLUE + "==================")
    anykey=input(Fore.BLUE + "press enter")
    print(Style.BRIGHT + Fore.GREEN + "saved!")
    time.sleep(3)
    menu()

def addemail():
    print(Fore.BLUE + "[+] type the email of "+first_name+" "+last_name+" to get possible password")
    time.sleep(3)
    global mail
    mail = input(Fore.BLUE + "[+] Enter The Email : ")
    time.sleep(3)
    print(Fore.BLUE + "==================")
    print(Style.BRIGHT + Fore.CYAN + first_name)
    print(Style.BRIGHT + Fore.CYAN + last_name)
    print(Style.BRIGHT + Fore.CYAN + mail)
    print(Fore.BLUE + "==================")
    anykey=input(Fore.BLUE + "press enter")
    print(Style.BRIGHT + Fore.GREEN + "saved!")
    time.sleep(3)
    menu()

def add_phonenumber():
    print(Fore.BLUE + "[+] type the phone number of "+first_name+" "+last_name+" to get better results")
    time.sleep(2)
    print(Style.BRIGHT + Fore.YELLOW + "[+] type the number like this > 88809990000 then in the second line type the number like this > 888-999-0000")
    global number
    number = str(input(Fore.BLUE + "[+] add phone number: "))
    print(Style.BRIGHT + Fore.YELLOW + "[+] now type the number like this > 888-999-0000")
    global number2
    number2 = str(input(Fore.BLUE + "[+] add phone number: "))
    os.system('w3m -dump https://www.anywho.com/phone/'+number+' > phone_number.txt')
    os.system('w3m -dump https://www.thisnumber.com/'+number2+' > phone_addresses.txt')
    print(Fore.BLUE + "==================")
    print(Style.BRIGHT + Fore.CYAN + first_name)
    print(Style.BRIGHT + Fore.CYAN + last_name)
    print(Style.BRIGHT + Fore.CYAN + number)
    print(Style.BRIGHT + Fore.CYAN + number2)
    print(Fore.BLUE + "==================")
    anykey=input(Fore.BLUE + "press enter")
    print(Style.BRIGHT + Fore.GREEN + "saved!")
    time.sleep(3)
    menu()

def dump_place():
    print(Fore.GREEN + "[+] finding possible location from "+first_name+" "+last_name+"'s phone number")
    time.sleep(4)
    f = open("phone_number.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("City/State:", line):
          print(Style.BRIGHT + Fore.YELLOW + "[📱🌏] > "+line)
    f = open("phone_number.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Street Address:", line):
          print(Style.BRIGHT + Fore.YELLOW + "[📱🌍] > "+line)
    menu()

def dump_address():
    print(Fore.GREEN + "[+] finding all addresses we found searching the number you gave us")
    time.sleep(6)
    f = open("phone_addresses.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Address:", line):
          print(Style.BRIGHT + Fore.YELLOW + "[📱🌎] > "+line)
    menu()

def dump_names():
    print(Fore.GREEN + "[+] finding all address names from the phone number you gave us")
    time.sleep(6)
    f = open("phone_addresses.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("Name:", line):
          print(Style.BRIGHT + Fore.YELLOW + "[📱🙎] > "+line)
    menu()

def email_results():
    print(Fore.GREEN + "[+] dumping out information we found on the given email")
    time.sleep(8)
    key = "VrzIuNfj27KXWnHHALabdRqfBowBVciW"
    api = "https://ipqualityscore.com/api/json/email/"+key+"/"+mail+""
    response = urllib.request.urlopen(api)
    data = response.read()
    value = json.loads(data)
    print('')
    print(Style.BRIGHT + Fore.YELLOW + "[+] Success Status: " + str(value['success']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] Valid: " + str(value['valid']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] Disposable: " + str(value['disposable']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] Honeypot: " + str(value['honeypot']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] Smtp Score: " + str(value['smtp_score']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] Overall Score: " + str(value['overall_score']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] First Name: " + str(value['first_name']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] Generic: " + str(value['generic']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] Dns Valid: " + str(value['dns_valid']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] Deliverability: " + str(value['deliverability']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] Frequent Complainer: " + str(value['frequent_complainer']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] Spam Trap: " + str(value['spam_trap_score']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] Catch All: " + str(value['catch_all']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] Time Out: " + str(value['timed_out']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] Abused Recently: " + str(value['recent_abuse']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] Fraud Score: " + str(value['fraud_score']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] Suggested Domain: " + str(value['suggested_domain']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] Leaked: " + str(value['leaked']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] Domain Age Human: " + str(value['domain_age']['human']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] Time Stamp: " + str(value['domain_age']['timestamp']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] ISO: " + str(value['domain_age']['iso']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] First Seen: " + str(value['first_seen']['human']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] First Seen Timestamp: " + str(value['first_seen']['timestamp']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] First Seen ISO: " + str(value['domain_age']['iso']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] Sanitized Email: " + str(value['sanitized_email']))
    print(Style.BRIGHT + Fore.YELLOW + "[+] Request ID: " + str(value['request_id']))
    print('')
    menu()

def socials():
    print(Fore.GREEN + "[+] finding all possible social media accounts on "+first_name+" "+last_name+"")
    time.sleep(3)
    f = open("socials.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("https://www.tiktok.com/", line):
          print(Style.BRIGHT + Fore.YELLOW + "[🧐] social profile links > "+line)
          f = open("socials.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("https://www.instagram.com/", line):
          print(Style.BRIGHT + Fore.YELLOW + "[🧐] social profile links > "+line)
          f = open("socials.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("https://twitter.com/", line):
          print(Style.BRIGHT + Fore.YELLOW + "[🧐] social profile links > "+line)
          f = open("socials.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("https://www.amazon.com/", line):
          print(Style.BRIGHT + Fore.YELLOW + "[🧐] social profile links > "+line)
          f = open("socials.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("https://www.yahoo.com/", line):
          print(Style.BRIGHT + Fore.YELLOW + "[🧐] social profile links > "+line)
          f = open("socials.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("https://www.linkedin.com/", line):
          print(Style.BRIGHT + Fore.YELLOW + "[🧐] social profile links > "+line)
          f = open("socials.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("https://www.youtube.com/", line):
          print(Style.BRIGHT + Fore.YELLOW + "[🧐] social profile links > "+line)
          f = open("socials.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("https://www.aol.com/", line):
          print(Style.BRIGHT + Fore.YELLOW + "[🧐] social profile links > "+line)
          f = open("socials.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("https://insurance-agent.safeco.com/", line):
          print(Style.BRIGHT + Fore.YELLOW + "[🧐] social profile links > "+line)
          f = open("socials.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("https://viralpornhub.com/", line):
          print(Style.BRIGHT + Fore.YELLOW + "[🧐] social profile links > "+line)
          f = open("socials.txt", "r")
    lines = f.readlines()
    lines[0:449]
    for line in lines:
        if re.match("https://www.pinterest.com/", line):
          print(Style.BRIGHT + Fore.YELLOW + "[🧐] social profile links > "+line)
    menu()

menu()
