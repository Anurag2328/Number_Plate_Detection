#! /usr/bin/python3

import cgi
import subprocess
import time

print("content-type: text/html")
print()

# FieldStrorage is  a function to take input
f = cgi.FieldStorage()
plate_no = f.getvalue("x")


if plate_no == "KA 05 NB 1786":
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:lightblue;" >VECHICLE DETAILS</h1>')
    print('''<pre>
    Registration Name : RAHUL RATHOD 
    License No : 12345677889
    Make / Model : BABA HYUNDAI / VERNA
    Registration Date : 1/12/2011
    Registering Authority : UJJAIN , INDIA
    Vehicle Class : MCWG
    Fuel Type : CNG
    Engine No : IVK3N1734538
    Chassis No : HMSURVWVQSVWE
    Insurance Upto : 5/13/2022
    Fitness Upto : 4/8/2030
    </pre>''')
    print("</body>")

elif plate_no == "MH:01.CT.5470":
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:yellow;" >VECHICLE DETAILS</h1>')
    print('''<pre>
    Registration Name : ANKITA LUDBE
    License No : 098363357292
    Make / Model : HONDA / CITY
    Registration Date : 1/12/2014
    Registering Authority : MUMBAI, INDIA
    Vehicle Class : MCWG
    Fuel Type : CNG
    Engine No : IVK3N1734538
    Chassis No : HMSURVWVQSVWE
    Insurance Upto : 5/13/2022
    Fitness Upto : 4/8/2030
    </pre>''')
    print("</body>")

elif plate_no == "MH 12 HZ 0148":
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print('''<pre>
    Registration Name : AMAN PANWAR
    License No : 735382528936
    Make / Model : MARUTI SUZUKI / ALTO800
    Registration Date : 1/12/2014
    Registering Authority : MANDSAUR, INDIA
    Vehicle Class : MCWG
    Fuel Type : CNG
    Engine No : IVK3N1734538
    Chassis No : HMSURVWVQSVWE
    Insurance Upto : 5/13/2022
    Fitness Upto : 4/8/2030
    </pre>''')
    print("</body>")

else:
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print("No data available for this number...")
    print("</body>")
