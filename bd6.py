# -*- coding: utf-8 -*-
import sqlite3
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