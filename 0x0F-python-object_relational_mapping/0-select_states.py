#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb

conn = MySQLdb.connect(user="root", passwd="root", db="hbtn_0e_0_usa")
cur = conn.cursor()

cur.execute("SELECT * FROM states")