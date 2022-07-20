# -*- coding: utf-8 -*-
import sqlite3
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