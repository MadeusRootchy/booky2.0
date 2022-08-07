# -*- coding: utf-8 -*-
import sqlite3

def Lister():
    try:
        conn = sqlite3.connect('BookyBase.db')
        cur = conn.cursor()

        sql = "SELECT * FROM contacts"

        cur.execute(sql)
        res = cur.fetchall()

        for row in res:
            print("Fullname: ", row[0])
            print("Phone_Number: ", row[1]) 
            print("Email: ", row[2])
            print("Address: ", row[3])
            print("\n")
    
        cur.close()
        conn.close()
        print("Done")

    except sqlite3.Error as error:
        print("Error,someting went wrong!",error)

def Create() :
    try:
        conn = sqlite3.connect('BookyBase.db')
        sql = '''CREATE TABLE contacts (
                   
                    fullname TEXT NOT NULL,
                    number TEXT NOT NULL,
                    email TEXT NOT NULL,
                    address TEXT NOT NULL
            );'''

        cur = conn.cursor()
        print("Connexion réussie à SQLite")
        cur.execute(sql)
        conn.commit()
        print("Table SQLite est créée")

        cur.close()
        conn.close()
        print("Connexion SQLite est fermée")

    except sqlite3.Error as error:
        print("Erreur lors de la création du table SQLite", error)
def connexion():
    try:
        conn = sqlite3.connect('BookyBase.db')
        cur = conn.cursor()
        print("Base de données crée et correctement connectée à SQLite")
        cur.close()
        conn.close()
        print("La connexion SQLite est fermée")

    except sqlite3.Error as error:
        print("Erreur lors de la connexion à SQLite", error)
def edit5(fullname,newadress):
    try:
        conn = sqlite3.connect('BookyBase.db')
        cur = conn.cursor()
        #pou nouvo adress lan
        sql = "UPDATE contacts SET address = ? WHERE fullname = ?"
        value = (newadress,fullname )
        cur.execute(sql, value)
        conn.commit()
        print("successfuly update")
        cur.close()
        conn.close()
        print("Connexion closed")

    except sqlite3.Error as error:
        print(" Errow ,Someting went wrong!",error)

def edit3(fullname,newname):
    try:
        conn = sqlite3.connect('BookyBase.db')
        cur = conn.cursor()
        #pou nouvo nimewo an
        sql = "UPDATE contacts SET fullname = ? WHERE fullname = ?"
        value = (newname,fullname )
        cur.execute(sql, value)
        conn.commit()
        print("successfuly update")
        cur.close()
        conn.close()
        print("Connexion closed")

    except sqlite3.Error as error:
        print("Error,someting went wrong!",error)
    

def Lister2(sea):
    try:
        conn = sqlite3.connect('BookyBase.db')
        cur = conn.cursor()

        sql = "SELECT * FROM contacts where fullname = ?"
        fullname = sea
        cur.execute(sql,(sea,))
        res = cur.fetchall()

        for row in res:
            print("Fullname: ", row[0])
            print("Phone_Number: ", row[1]) 
            print("Email: ", row[2])
            print("Address: ", row[3])
            print("\n")
    
        cur.close()
        conn.close()
        print("Done")

    except sqlite3.Error as error:
        print("Erreur lors du sélection à partir de la table contacts", error)
def edit4(fullname,newemail):
    try:
        conn = sqlite3.connect('BookyBase.db')
        cur = conn.cursor()
        #pou nouvo email lan
        sql = "UPDATE contacts SET email = ? WHERE fullname = ?"
        value = (newemail,fullname )
        cur.execute(sql, value)
        conn.commit()
        print("successfuly update")
        cur.close()
        conn.close()
        print("Connexion closed")

    except sqlite3.Error as error:
        print("Error,someting went wrong!")
def edit2(fullname,newnumber):
    try:
        conn = sqlite3.connect('BookyBase.db')
        cur = conn.cursor()
        #pou nouvo nimewo an
        sql = "UPDATE contacts SET number = ? WHERE fullname = ?"
        value = (newnumber,fullname )
        cur.execute(sql, value)
        conn.commit()
        print("successfuly update")
        cur.close()
        conn.close()
        print("Connexion closed")

    except sqlite3.Error as error:
        print("Error,someting went wrong!",error)
    

def edit(fullname,newname,newnumber,newemail,newaddress):
    try:
        conn = sqlite3.connect('BookyBase.db')
        cur = conn.cursor()
        #pou nouvonon an
        sql = "UPDATE contacts SET fullname = ? WHERE fullname = ?"
        value = (newname,fullname )
        cur.execute(sql, value)
        conn.commit()
        
        #pou nouvoemail lan
        sql2 = "UPDATE contacts SET email = ? WHERE fullname = ?"
        value = (newemail,fullname )
        cur.execute(sql2, value)
        conn.commit()
        #pou adres lan
        sql3 = "UPDATE contacts SET address = ? WHERE fullname = ?"
        value = (newaddress,fullname )
        cur.execute(sql3, value)
        conn.commit()

       
        print("successfuly update")
    
        cur.close()
        conn.close()
        print("Connexion closed")

    except sqlite3.Error as error:
        print("Error,someting went wrong!",error)

def Insertion(fullname,number,email,address) :
    try:
        conn = sqlite3.connect('BookyBase.db')
        cur = conn.cursor()

        cur.execute ("INSERT INTO contacts VALUES (?, ?, ?, ?);",(fullname,number,email,address))

        #conn = cur.execute(sql)
        conn.commit()
        print("Succesfully register!")
        cur.close()
        conn.close()
        print("Done")

    except sqlite3.Error as error:
        print("Error", error)

def sup(name) :
    try:
        conn = sqlite3.connect('BookyBase.db')
        cur = conn.cursor()
        sql = "DELETE FROM contacts WHERE fullname = ?"
        fullname = name
        cur.execute(sql, (fullname, ))
        conn.commit()
        #pull up anglais bate a laaa
        print("succefully register.")
    
        cur.close()
        conn.close()
        print("Done")

    except sqlite3.Error as error:
        print("Error,someting went wrong!",error)

