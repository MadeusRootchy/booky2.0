# -*- coding: utf-8 -*-
import sqlite3
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
    