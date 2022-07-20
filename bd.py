# -*- coding: utf-8 -*-
import sqlite3

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

'''
number:345

ki nouvo non(Lub): 
ki nouvo imel (): 



'''