# -*- coding: utf-8 -*-
import sqlite3

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