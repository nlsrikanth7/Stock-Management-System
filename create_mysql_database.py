import yfinance as yf
from getpass import getpass
import mysql.connector
from mysql.connector import connect, Error, errorcode
import logging
import time


mydb= mysql.connector.connect(host = "localhost",user ="root",passwd ="Shrikanth_1", database='stockmanagementsystem')

mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE IF NOT EXISTS stockmanagementsystem")

mycursor.execute("CREATE TABLE IF NOT EXISTS stocks (id int(11), name varchar(255), price int(10), quantity int(11), category varchar(255))")
# mycursor.execute("CREATE TABLE stockprices (stockid int(10),Datetime date,Open int(10),High int(10),Close int(10),ADJCLOSE int(10),VOLULME int(10))")


mydb.commit()