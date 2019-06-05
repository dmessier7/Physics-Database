import sqlite3 as s
'''
The Steps to exectue database commands:
1. Connect to Database
2. Execute Command with Cursor
3. Commit Command with Cursor
4. Close Connection with Cursor -done in the run file at the end of execution
'''
conn = s.connect('PhysicsDatabase.db')
'''Connects to the PhysicsDatabase.db file that is in the same directory,
 Creates it if it's not thereselfself.
 db files are often hidden by your computer, which may be why it isn't visible '''
c = conn.cursor()
''' Cursor used by python to execute SQL commands.'''



# Item classes and Functions

# Location is a Array of Strings for the location of the item
class Location:
    ZerothLevel = str
    FirstLevel = str
    SecondLevel = str
    ThirdLevel = str
    FourthLevel = str
    FifthLevel = str
    SixthLevel = str
    L = [ZerothLevel, FirstLevel, SecondLevel, ThirdLevel, FourthLevel, FifthLevel, SixthLevel]

# Creating Tables

def CreateInventoryTable():
    c.execute('CREATE TABLE Inventory (ItemID INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Description TEXT);')
    conn.commit()
    # Won't Create the table with the same name twice in the same place

def CreateLocationTable():
    c.execute("""CREATE TABLE LocationTable (LocationID INTEGER PRIMARY KEY AUTOINCREMENT,
        L0 TEXT, L1 TEXT, L2 TEXT, L3 TEXT, L4 TEXT, L5 TEXT, L6 TEXT)""")
    conn.commit()

def CreateQuantityTable():
    c.execute('CREATE TABLE QuantityTable (ItemID INTEGER, LocationID INTEGER, Quantity INTEGER)')

def CreateClassTable():
    c.execute('CREATE TABLE ClassTable (ClassID INTEGER PRIMARY KEY AUTOINCREMENT, ClassName TEXT)')

def CreateLabTable():
    c.execute('CREATE TABLE LabTable (LabID INTEGER PRIMARY KEY AUTOINCREMENT, LabName TEXT, Description TEXT)')

def CreateClassLabTable():
    c.execute('CREATE TABLE ClassLabTable (ClassID INTEGER, LabID INTEGER)')

def CreateLabItemsTable():
    c.execute('CREATE TABLE LabItemsTable (LabID INTEGER, ItemID INTEGER, NumPerTable INTEGER, Num INTEGER)')

def CreateExtrasTable():
    c.execute('CREATE TABLE ExtrasTable (LabID INTEGER, ItemID INTEGER)')

# Single ID Functions
# X == 1 Add Thing, X == 0 Delete Thing

def AddItemToInventory(ItemName, ItemDescription, X):
    D = ItemDescription
    N = ItemName
    c.execute("SELECT * FROM Inventory WHERE Name = ?", (N,))
    if X == 1:
        if c.fetchone() is not None:
            print('Error. Name already used')
        else:
            c.execute("INSERT INTO Inventory(ItemID, name, description) VALUES(?, ?,?)", (None, N, D))
            conn.commit()
    elif X == 0:
        if c.fetchone() is None:
            print("Error. Item doesn't exist")
        else:
            c.execute("DELETE FROM Inventory WHERE Name = ?", (N,))
            conn.commit()
    else:
        print("Error. Inventory X is neither 0 nor 1")

def AddLocation(Loc):
    K = [Loc.L[0], Loc.L[1], Loc.L[2], Loc.L[3],
        Loc.L[4], Loc.L[5], Loc.L[6],]
    c.execute("SELECT * FROM LocationTable WHERE (L0,L1,L2,L3,L4,L5,L6) = (?,?,?,?,?,?,?)", (K[0], K[1], K[2], K[3], K[4], K[5], K[6],))
    if c.fetchall() is not None:
        print('Error. Location already exists')
    else:
        c.execute('INSERT INTO LocationTable VALUES(?,?,?,?,?,?,?,?)',
                      (None, K[0], K[1], K[2], K[3], K[4], K[5], K[6],))
        conn.commit()

def AddClass(ClassName, X):
    P = ClassName
    c.execute("SELECT * FROM ClassTable WHERE ClassName = ?", (P,))
    if X == 1:
        if c.fetchone() is not None:
            print('Error. Class already exists')
        else:
            c.execute("INSERT INTO ClassTable(ClassID, ClassName) VALUES(?, ?)", (None, P))
            conn.commit()
    elif X == 0:
        if c.fetchone() is None:
            print("Error. Class Doesn't Exist")
        else:
            c.execute("DELETE FROM ClassTable WHERE ClassName =?", (P,))
            conn.commit()
    else:
        print("Error. Class X is neither 0 nor 1")

def AddLab(LabName, Description, X):
    P = LabName
    D = Description
    c.execute("SELECT * FROM LabTable WHERE LabName = ?", (P,))
    if X == 1:
        if c.fetchone() is not None:
            print('Error. Lab already exists')
        else:
            c.execute("INSERT INTO LabTable(LabID, LabName, Description) VALUES(?, ?, ?)", (None, P, D))
            conn.commit()
    elif X == 0:
        if c.fetchone() is None:
            print("Error. Lab doesn't exist")
        else:
            c.execute("DELETE FROM LabTable WHERE LabName = ?", (P,))
            conn.commit()
    else:
        print("Error. Lab X is neither 0 nor 1")

# ID Retrieval Functions
def SearchIDByName(TableName, Name):
    f = 0;
    if TableName == "Inventory":
        c.execute("SELECT * FROM Inventory WHERE LabName = ?", (Name,))
        f = c.fetchone()
    elif TableName == "QuantityTable":
        c.execute("SELECT * FROM QuantityTable WHERE LabName = ?", (Name,))
        f = c.fetchone()
    elif TableName == "ClassTable":
        c.execute("SELECT * FROM ClassTable WHERE LabName = ?", (Name,))
        f = c.fetchone()
    elif TableName == "LabTable":
        c.execute("SELECT * FROM LabTable WHERE LabName = ?", (Name,))
        f = c.fetchone()
    else:
        print("Error. Table Not Applicable.")
    print(f[0])
    return f[0]

#def SearchLocationIDByName():


# Multiple ID (Relation) Functions
def AddClassLabRelation(ClassID, LabID, X):
    U = ClassID
    V = LabID
    c.execute("SELECT * FROM ClassLabTable WHERE ClassID = ? AND LabID", (U, V,))
    if X == 1:
        if c.fetchone() is not None:
            print('Error. Relation Already Exists')
        else:
            c.execute("INSERT INTO ClassLabTable (ClassID, LabID) VALUES(?, ?)", (U, V,))
            conn.commit()
    elif X == 0:
        if c.fetchone() is None:
            print("Error. Relation Doesn't Exist")
        else:
            c.execute("DELETE FROM ClassLabTable WHERE ClassID = ? AND LabID = ?", (U, V,))
            conn.commit()
    else:
        print("Error. ClassLabRelation X is neither 0 nor 1")

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
