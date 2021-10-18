import configparser
import mysql.connector
from mysql.connector import Error


def getconfig():
    config = configparser.ConfigParser()
    config.read("C:\\Users\\Punam\\workspace_python\\apilatestnew\\configuration\\properties.ini")
    return config


concat= {
    "host" : getconfig()['SQL']['hostname'],
    "database" : getconfig()['SQL']['database'],
    "user" : getconfig()['SQL']['username'],
    "password" : getconfig()['SQL']['password']
}

def getconnection():
    try:
        con = mysql.connector.connect(**concat)
        if con is not None:
            print("connected")
            return con
        else:
            print("not connected")
    except Error as e:
        print(e)


def runUquery(uquery, data):
    con = getconnection()
    cursor = con.cursor()
    cursor.execute(uquery, data)
    con.commit()
    con.close()

def rungquery(gquery):
    con = getconnection()
    cursor = con.cursor()
    cursor.execute(gquery)
    row = cursor.fetchone()
    con.close()
    return row

