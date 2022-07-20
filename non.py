# -*- coding: utf-8 -*-
import sqlite3
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
    