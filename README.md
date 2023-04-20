# Profiler
Profiler is a tool that looks up a name and from there you can interact with this tool like a shell and add location/state/region/phone number/email/vehicle identification number/ 

(I am currently working on adding a module for lisense plate lookup)

# OSINT
----------------------------------------------------------------------------------------------------------------------
this tool is used to investigatea person and find were and what there location is

# What this tool uses to investigate your target
----------------------------------------------------------------------------------------------------------------------
- spokeo.com
- google
- ipqualityscore.com
- faxvin.com
- anywho.com
- thisnumber.com

# installing Profiler

(i am not responsible for what u do with this tool)


1. - git clone https://github.com/openpolicy0/Profiler.git
2. - cd Profiler 
3. - python3 -m venv venv_profiler
4. - source venv_profiler/bin/activate
5. - pip install -r requirements.txt 

# About this tool
----------------------------------------------------------------------------------------------------------------------
- type help for the option
- getR names > get related names
- get locations > get all possible locations
- getP locations > get possible past locations
- getN family > get family names
- getON names > get other names she/he goes by
- getP included > get a list of personal data included
- get socials > get all social accounts
- dump all > dump all results on target
- dump phonenumL > dump single phone number location
- dumpR phonenums > dump related phone numbers
- dumpR phonenum/addrs > dump related phone number address
- dumpR phonenum/names > dump related phone number names
- dump emaildata > dump email data about the email
- dump carinfo > dump details about the vin number
