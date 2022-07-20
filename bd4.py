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