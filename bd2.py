# -*- coding: utf-8 -*-
import sqlite3

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