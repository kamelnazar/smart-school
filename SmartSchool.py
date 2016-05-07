import RPi.GPIO as GPIO
import time
from time import sleep
import MySQLdb
import os
#from termcolor import colored
# Set mode GPIO to use it in the program
GPIO.setmode(GPIO.BOARD)
# Clean Up the program
GPIO.cleanup()
# ignore all Errors in the program
GPIO.setwarnings(False)
#Room1 GPIO
# Use GPIO number 7 as output
GPIO.setup(7,GPIO.OUT)
#Room2 GPIO
# use GPIO number 11 as output
GPIO.setup(11,GPIO.OUT)
#Room3 GPIO
# use GPIO number 12 as output
GPIO.setup(12,GPIO.OUT)
#Room4 GPIO
# use GPIO number 13 as output
GPIO.setup(13,GPIO.OUT)
# to initialize the database
GPIO.setup(16,GPIO.OUT)
TRIG=24
ECHO=23

TR=31
EC=32
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#print "Distance Measurement In Progress"

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.setup(TR,GPIO.OUT)
GPIO.setup(EC,GPIO.IN)

db = MySQLdb.connect(host=" ",    # your host, usually localhost
                     user=" ",         # your username
                     passwd=" ",  # your password
                     db=" ")

#ID=2
#define x to use the connection
x = db.cursor()
x1=db.cursor()
x2=db.cursor()
x3=db.cursor()
x4=db.cursor()
x5=db.cursor()
Message1=db.cursor()
Message2=db.cursor()
Message3=db.cursor()

x.execute("SELECT Status  FROM TrigerTB where ID='1' ")
x1.execute("SELECT Status  FROM TrigerTB where ID='5' ")
x2.execute("SELECT Status  FROM TrigerTB where ID='3' ")
x3.execute("SELECT Status  FROM TrigerTB where ID='6' ")
x4.execute("SELECT Status  FROM TrigerTB where ID='4' ")
Message1.execute("SELECT MessageText  FROM MessageRaspberryTB where ID='1' ")
Message2.execute("SELECT MessageText  FROM MessageRaspberryTB where ID='2' ")
Message3.execute("SELECT MessageText  FROM MessageRaspberryTB where ID='3' ")

row = x.fetchall()
row1=x1.fetchall()
row2=x2.fetchall()
row3=x3.fetchall()
row4=x4.fetchall()
RowMessage1=Message1.fetchall()
RowMessage2=Message2.fetchall()
RowMessage3=Message3.fetchall()
count=0
while 1:
    for I in row:
        ID = I[0]
        if ID == 1:
            #Turn ON Room1
            GPIO.output(7,GPIO.HIGH)
            print " "
            print "Room 1 in the (floor 1)"
            print " "
            print bcolors.BOLD +  bcolors.BOLD + bcolors.WARNING + "Turned ON" + bcolors.ENDC
            print " "
        else:
            #turn Off Room1
            GPIO.output(7,GPIO.LOW)
            print "Room 1 in the (floor 1)"
            print " "
            print "Turned OFF"
            print " "
        break
    
        
    print bcolors.BOLD + bcolors.UNDERLINE + bcolors.HEADER + bcolors.WARNING + bcolors.OKGREEN + "********************************************************************"  + bcolors.ENDC
    print " "
    for I1 in row1:
        ID1 = I1[0]
        if ID1 == 1:
            #turn ON Room2
            GPIO.output(11,GPIO.HIGH)
            print  "Room 2 in the (floor 1)"
            print " "
            print bcolors.BOLD +  bcolors.WARNING +  "Turned ON" + bcolors.ENDC
            print " "
        else:
            #turn Off Room2
            GPIO.output(11,GPIO.LOW)
            print "Room 2 in the (floor 1)"
            print " "
            print "Turned OFF"
            print " "
        break
    
        
    print bcolors.BOLD + bcolors.UNDERLINE + bcolors.HEADER + bcolors.WARNING + bcolors.OKGREEN + "********************************************************************"  + bcolors.ENDC
    print " "
    for I2 in row2:
        ID2 = I2[0]
        if ID2 == 1:
            #turn ON Room3
            GPIO.output(12,GPIO.HIGH)
            print "Room 1 in the ((floor 2))"
            print " "
            print bcolors.BOLD + bcolors.WARNING +  "Turned ON" + bcolors.ENDC
            print " "
        else:
            #turn Off Room3
            GPIO.output(12,GPIO.LOW)
            print "Room 1 in the ((floor 2))"
            print " "
            print "Turned OFF"
            print " "
        break
    
       
    print bcolors.BOLD + bcolors.UNDERLINE + bcolors.HEADER + bcolors.WARNING + bcolors.OKGREEN + "********************************************************************"  + bcolors.ENDC
    print " "
    for I3 in row3:
        ID3 = I3[0]
        if ID3 == 1:
            #turn ON Room4
            GPIO.output(13,GPIO.HIGH)
            print "Room 2 in the ((floor 2))"
            print " "
            print bcolors.BOLD +  bcolors.WARNING + "Turned ON"  + bcolors.ENDC
            print " "
        else:
            #turn Off Room4
            GPIO.output(13,GPIO.LOW)
            print "Room 2 in the ((floor 2))"
            print " "
            print "Turned OFF"
            print " "
        break
    
    print bcolors.BOLD + bcolors.UNDERLINE + bcolors.HEADER + bcolors.WARNING + bcolors.OKGREEN + "********************************************************************"  + bcolors.ENDC
    print " "
    for I4 in row4:
        ID4 = I4[0]
        if ID4 == 1:
            #turn ON Room4
            GPIO.output(16,GPIO.HIGH)
            print "Generator"
            print " "
            print bcolors.BOLD +  bcolors.WARNING +  "Turned ON" + bcolors.ENDC
            print " "
        else:
            #turn Off Room4
            GPIO.output(16,GPIO.LOW)
            print "Generator"
            print " "
            print "Turned OFF"
            print " "
        break
    
    print bcolors.BOLD +  bcolors.WARNING + "********************************************************************" + bcolors.ENDC
    print bcolors.BOLD + bcolors.UNDERLINE + bcolors.HEADER + bcolors.WARNING + bcolors.OKGREEN + "Messages List: "  + bcolors.ENDC
    print " "
    print RowMessage1," is the Honor on the School"
    print " "
    print RowMessage2," is the Winner on the School"
    print " "
    print RowMessage3," is the First on the School"
    print " "
    print bcolors.BOLD +  bcolors.WARNING + "********************************************************************" + bcolors.ENDC
    
    GPIO.output(TRIG, False)
    
    #print "Waiting For Sensor 1 To Settle..."
    
    time.sleep(3)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
     
    while GPIO.input(ECHO)==1:  
        pulse_end = time.time()

    pulse_duration=pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)
    
    print "Distance in parking 1: ",distance,"cm"
    
    #Defenition of parking 2:
    
    GPIO.output(TR, False)
    #print "Waiting For Sensor 2 To Settle"
    
    time.sleep(3)

    GPIO.output(TR, True)
    time.sleep(0.00001)
    GPIO.output(TR, False)

    while GPIO.input(EC)==0:
        pulse_start1 = time.time()
     
    while GPIO.input(EC)==1:  
        pulse_end1 = time.time()

    pulse_duration1=pulse_end1 - pulse_start1

    distance1 = pulse_duration1 * 17150

    distance1 = round(distance1, 2)
   
    
    
    if distance < 8:
        db = MySQLdb.connect(host="sql6..net",    # your host, usually localhost
                     user=" ",         # your username
                     passwd=" ",  # your password
                     db=" ")
        curb = db.cursor()
        curb.execute("UPDATE ParckingTB SET Status=1 WHERE ID='1'")
        db.autocommit(True)
        print "Parking 1 is not available"
    else:
        db = MySQLdb.connect(host="sql6..net",    # your host, usually localhost
                     user=" ",         # your username
                     passwd=" ",  # your password
                     db=" ")
        curb = db.cursor()
        curb.execute("UPDATE ParckingTB SET Status=2 WHERE ID='1'")
        db.autocommit(True)
        print bcolors.WARNING +  "Parking 1 is available" + bcolors.ENDC
    print "********************************************************************"
    print "Distance in parking 2: ",distance1,"cm"
    if distance1 < 8:
        db = MySQLdb.connect(host="sql6..net",    # your host, usually localhost
                     user=" ",         # your username
                     passwd=" ",  # your password
                     db=" ")
        curb = db.cursor()
        curb.execute("UPDATE ParckingTB SET Status=1 WHERE ID='2'")
        db.autocommit(True)
        print "Parking 2  is not available"
    else:
        db = MySQLdb.connect(host="sql6..net",    # your host, usually localhost
                     user=" ",         # your username
                     passwd=" ",  # your password
                     db=" ")
        curb = db.cursor()
        curb.execute("UPDATE ParckingTB SET Status=2 WHERE ID='2'")
        db.autocommit(True)
        print bcolors.WARNING + "Parking 2 is available" + bcolors.ENDC
    print "********************************************************************"
    db = MySQLdb.connect(host="sql6..net",    # your host, usually localhost
                     user=" ",         # your username
                     passwd=" ",  # your password
                     db=" ")
    x = db.cursor()
    x.execute("SELECT Status  FROM TrigerTB where ID='1' ")
    row = x.fetchall()

    x1 = db.cursor()
    x1.execute("SELECT Status  FROM TrigerTB where ID='5' ")
    row1 = x1.fetchall()

    x2 = db.cursor()
    x2.execute("SELECT Status  FROM TrigerTB where ID='3' ")
    row2 = x2.fetchall()

    x3 = db.cursor()
    x3.execute("SELECT Status  FROM TrigerTB where ID='6' ")
    row3 = x3.fetchall()

    x4 = db.cursor()
    x4.execute("SELECT Status  FROM TrigerTB where ID='4' ")
    row4 = x4.fetchall()
    
    Message1=db.cursor()
    Message2=db.cursor()
    Message3=db.cursor()
    Message1.execute("SELECT MessageText  FROM MessageRaspberryTB where ID='1' ")
    Message2.execute("SELECT MessageText  FROM MessageRaspberryTB where ID='2' ")
    Message3.execute("SELECT MessageText  FROM MessageRaspberryTB where ID='3' ")
    RowMessage1=Message1.fetchall()
    RowMessage2=Message2.fetchall()
    RowMessage3=Message3.fetchall()
    os.system('clear')


