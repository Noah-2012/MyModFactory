import json
from time import *
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

def progress_bar():
    with open("b0.json") as file:
        obj8 = json.load(file)
    ran = obj8['LoadingTimeBegin']
    waittime = obj8['LoadingTimeBegin']
    
    chars = '############################################################'
    loop = range(1, len(chars) + 1)
    load = 1
    
    
    maxwait = 0.5
    if waittime > maxwait:
        print("Warning! Waittime is high.")
    
    for idx in loop:
        print("Loading Terminal Data [",chars[:idx], "]",load,"/61", end='\r')
        sleep(ran)
        load = load + 1
    

Datei1 = str()
datei2 = str()    
datei = str()
datei3 = str()

with open('b0.json', 'r') as file:
    obj8 = json.load(file)
    gru = obj8['rootacces']

def insert(name):
    if name == ("Demodisk"):
        global Datei1
        Datei1 = open('Demodisk.txt', 'r+')
        print(Datei1.read())
    elif name ==("Kontrolle"):
        global datei2
        datei2 = open('Kontrolle.txt', 'r+')
        print(datei2.read())
    elif name == ("Terminal Config"):
        datei3 = open('config.txt', 'r')
        print(datei3.read())
    elif name == ("W/.mode"):
        t = str(input('Overwirting disk name: '))   
        if t == ("Demodisk"):
            t3 = open('Demodisk.txt', 'w')
            t2 = str(input('Overwriting Text: '))
            t3.write(t2)
        elif t == ("Kontrolle"):
            t4 = open('Kontrolle.txt', 'w')
            t5 = str(input('Overwriting Text: '))
            t4.write(t5)
        elif t == ("Terminal Config"):
            if gru == 1:
                t6 = open('a0.json', 'r+')
                print(t6.read())
                t7 = str(input('Overwriting Text: '))
                t6.write(t7)
            else:
                with open("b0.json") as file:
                    obj5 = json.load(file)
                c = obj5['errorcodes']['NoAccesErrno']
                print("No acces to Terminal Config.", c)            
    else:
        with open("b0.json") as file:
            obj7 = json.load(file)
        ErrnoDisk = obj7['errorcodes']['NoAccesErrno']      
        print("No Disk insert with this name. ",ErrnoDisk)
        
def exit():
    with open('a0.json') as file:
       obj6 = json.load(file)
    Loadingt = obj6['EndTextTrue']
    
    if Loadingt is True:
        print("Terminal turn off. [", "\033[32m" + "OK", "\033[0m" + "]")
        sleep(0.2)
        print("All log files closed. [", "\033[32m" + "OK", "\033[0m" + "]")
        sleep(0.2)
        print("All OpenGL connections separated. [", "\033[32m" + "OK", "\033[0m" + "]")
        sleep(0.2)
        print("'_main_.py' will be saved. [", "\033[32m" + "OK", "\033[0m" + "]")
        sleep(0.2)
        print("'_sys_.py will be saved [", "\033[32m" + "OK", "\033[0m" + "]")
        sleep(0.6)
        print("Menu control closed. [", "\033[32m" + "OK", "\033[0m" + "]")
        sleep(1)
        print("Session is saved. [", "\033[32m" + "OK", "\033[0m" + "]")
        sleep(0.2)
        print("All data closed. [", "\033[32m" + "OK", "\033[0m" + "]")
        sleep(0.2)
        print("MS Dos will be saved. [", "\033[32m" + "OK", "\033[0m" + "]")
        sleep(0.5)
        print("Python will exit. [", "\033[32m" + "OK", "\033[0m" + "]")
        sleep(0.2)
        print("Java finishes writing cmos files. [", "\033[32m" + "OK", "\033[0m" + "]")
        sleep(2)
        print("C++ turn off. [", "\033[32m" + "OK", "\033[0m" + "]")
        sleep(3)
