# -*- coding: utf-8 -*-
import sqlite3
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
    