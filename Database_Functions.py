<<<<<<< HEAD:Database_Functions.py
=======
import sqlite3 as s
import sys
import random

from PyQt5 import QtGui
from PyQt5 import QtWidgets

>>>>>>> 9aaddf3e561a7cfb8d1214288a334329393bef9f:MultiTableLabDatabase.py
# Item classes and Functions

# Location is a Array of Strings for the location of the item
class Location:
    ZerothLevel = str
    FirstLevel = str
    SecondLevel = str
    ThirdLevel = str
    FourthLevel = str
    FifthLevel = str
    L = [ZerothLevel, FirstLevel, SecondLevel, ThirdLevel, FourthLevel, FifthLevel]


# Database Tools

def CreateInventoryTable(TableName):
    c.execute('CREATE TABLE ' + TableName + '(ItemID PRIMARY KEY, Name TEXT, Description TEXT);')
    conn.commit()
    # Won't Create the table with the same name twice in the same place


def AddItemToInventory(ItemName, ItemDescription):
    D = ItemDescription
    # X gives are random even number between 1 and 10000000
    X = random.randrange(1, 10000000, 2)
    # T makes the int X a string to be used
    T = str(X)
    N = ItemName
    c.execute("SELECT * FROM Inventory WHERE Name = ?", (N,))
    if c.fetchone() is not None:
        print('Error. Name already used')
    else:
        # the following takes the string T and compares it to every value in ItemID, if it matches a value it redefines T and tries again
        # Tested by replacing T in the following expression with the string of a known value, it never creates a new row b/c
        # the if statement is on a loop
        c.execute("SELECT * FROM Inventory WHERE ItemID = %s" % T)
        if c.fetchone() != None:
            T = random.randrange(1, 10000000, 2)
        else:
            c.execute("INSERT INTO Inventory(ItemID, name, description) VALUES(?, ?,?)", (T, N, D))
            conn.commit()


def CreateLocationTable(TableName):
    c.execute('CREATE TABLE ' + TableName + '(LocationID PRIMARY KEY, L0, L1, L2, L3, L4, L5, L6)')
    conn.commit()


def AddLocation(Location):
    # X gives a random odd number between 1 and 10000001
    X = random.randrange(1, 10000000 + 1, 2)
    T = str(X)
    K = Location
    c.execute(
        "SELECT * FROM LocationTable WHERE (L0,L1,L2,L3,L4,L5,L6) = (?,?,?,?,?,?,?,)"(K.L[0], K.L[1], K.L[2],
            K.L[3], K.L[4], K.L[5], K.L[6], ))
    if c.fetchone() is not None:
        print('Error. Location already exists')
    else:
        c.execute("SELECT * FROM LocationTable WHERE LocationID = %s" % T)
        if c.fetchone() is not None:
            T = random.randrange(1, 10000000 + 1, 2)
        else:
            c.execute('INSERT INTO ' + LocationTable + ' VALUES(?,?,?,?,?,?,?,?)',
                      (T, K.L[0], K.L[1], K.L[2], K.L[3], K.L[4], K.L[5], K.L[6]))
            conn.commit()


def CreateQuantityTable(TableName):
    c.execute('CREATE TABLE ' + TableName + '(ItemID INTEGER, LocationID INTEGER, Quantity INTEGER)')


def CreateOrAddQuantity(ItemID, LocationID, Quantity):
    c.execute("SELECT rowid FROM QuantityTable WHERE ItemID = ? AND LocationID=?", (ItemID, LocationID,))
    data = c.fetchone()
    if data is None:
        c.execute('INSERT INTO QuantityTable VALUES(?,?,?)', (ItemID, LocationID, Quantity))
    else:
        c.execute("UPDATE QuantityTable SET Quantity= Quantity +%s WHERE ItemID = ? AND LocationID  = ?" % (Quantity),
                  (ItemID, LocationID))
    conn.commit()


def ChangeQuantityOfItemAtLocation(QT, Item, Location, Change):
    # id(location makes new id)
    c.execute("UPDATE %s SET Quantity= Quantity +%s WHERE ItemID = ? AND LocationID  = ?" % (QT, Change),
              (id(Item), id(Location)))
    # c.execute("UPDATE ? SET Quantity= Quantity+? WHERE ItemID=? AND LocationID =? ", (QT, Change, id(Item), id(Location),))
    conn.commit()


# Sorting Functions
def SearchByItemName(TableName, ItemName):
    global f
    f = ItemName
    c.execute("SELECT * FROM " + TableName + " WHERE name ='" + ItemName + "'")
    data = c.fetchone()
    global ItemID
    ItemID = data[0]
    f.Name = data[1]
    f.Description = data[2]
    return f, ItemID;
