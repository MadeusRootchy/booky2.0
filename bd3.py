# -*- coding: utf-8 -*-
import sqlite3

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