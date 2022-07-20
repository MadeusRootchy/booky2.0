# -*- coding: utf-8 -*-
import sqlite3
import numpy as np
import csv
import sys
from nimewo import edit2
from search import Lister2
from email import edit4
from adres import edit5
from non import edit3
from bd import connexion
from bd2 import Create
from bd3 import Insertion
from bd4 import Lister
from BD8 import sup
contact={}
lischwa=[1,2,3,4,5,6]

while True :
    print("   ----------Booky----------")
    choix=input("\t1.Add contact\n\t2.Edit contact\n\t3.Delete contact\n\t4.Search contact\n\t5.Contact lists\n\t6.Exit\n\n\tMake a choice:\n\t ")
    choix=int(choix)
    if not  isinstance(choix,int):
            print("choice can't be a letter :")
            choix=input("1.Add contact\n2.Edit contact\n3.Delete contact\n4.Search contact\n5.Contact lists\n6.Exit\n\nMake a choice:\n ")
        
    while int(choix) not in lischwa:
        print("choice must be a number between 1 and 6  :")
        choix=input("1.Add contact\n2.Edit contact\n3.Delete contact\n4.Search contact\n5.Contact lists\n6.Exit\n\nMake a choice:\n ")
    
    if int(choix)==1:
        lischwa2 = [1,2]
        chwa=input("1.Add a new contact\n2.import a contact from google contact\n\nMake a choice :  ")
        chwa=int(chwa)
        if not isinstance (chwa,int):
            print("choice can be a letter")
            chwa=input("1.Add a new contact\n2.import a contact from google contact")
        while int(chwa) not in lischwa2:
            print("choice must be a number between 1 and 2  :")
            chwa=input("1.Add a new contact\n2.import a contact from google contact")
            
        if int (chwa)==1:
            fullname=input("Enter the fullname : ")
            while not fullname :
                fullname=input("Enter the fullname please : ")
            
            number=input("Enter the phone number : ")
            while not number :
                number=input("Enter the phone_Number please : ")
            while not isinstance(number,int):
                print("The phone number can't be letter!")
                number=input("enter the phone_Number please : ")

            email=input("Enter the mail : ")
          
            address=input("Enter the adress : ")
            connexion()
            Create()
            Insertion(fullname,number,email,address)
        if int(chwa)==2:
          print("Currently undisponible , call the programmer")

            
    if int(choix)==2  :
        
        fullname = input("Enter the name to edit :")
        change = input(" Put :\n[1] To edit the name\n[2] To edit the number\n[3]To edit  the email\n[4] To edit the address\n\n")
        if int(change)== 2:
            newnumber = input("Enter the new number : ")
            edit2(fullname,newnumber)
        if int(change)== 1:
            newname = input("Enter the new name : ")
            edit3(fullname,newname)
        if int(change)== 3:
            newemail = input("Enter the new email : ")
            edit4(fullname,newemail)
        if int(change)== 4:
            newadress = input("Enter the new adress : ")
            edit5(fullname,newadress)
        else :
            pass
    if int(choix)==3  :
        name = input("Enter the fullname to delete :")
        sup(name)
    if int(choix)==4  :
        sear = input("Enter the name to search information about : ")
        Lister2(sear)
        
    if int(choix)==5 :
        Lister()
        


    if int(choix)==6:
        break

    
        

