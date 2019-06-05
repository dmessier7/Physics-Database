# Physics-Database
Database Program for Physics and Engineering Inventory

## Objective:   
An interface for use by the lab techs and lab assistants to keep track of inventory, see the items required for lab set ups, and help ensure there's enough of what's need for set ups. At first this will be localized to one computer, but hopefully eventually we can connect it to the lab's cloud file storage to allow multiple computers to use and edit the system.

The progam will be written in python, using the SQLite3 library to create, manage, and pull from the database(s). This means managing the databases is done by writing python functions which executes SQL commands. What will be used for the GUI isn't super concrete. Right now I'm using PyQt5 which isn't amazing, so something else might work better. tKinter wasn't used because of limitations on the placement and style.

## Functionality Requirements:
My idea for the GUI is a window with the main menu on the side at all times taking up ~1/4 of the window, and a space for tabs taking up the other 3/4 of window. Tabs are similar to tabs on an internet browser.  
Some Notes
* Classes (e.g PHYS 250, PHYS 220), Lab (Free Fall, Vector Forces), Items (Oscilloscope, Ruler).
* Locations are 6 strings are follow a hierarchy completely up to the people using the program. We'll need to write down some guidelines.
* I hope that eventually we can incorporate a calendar interface to organize labs

Main Menu:  
Top   
* Lab List  
* Item List
* Location List
* Quick Search

Bottom
* Class List in Numerical order, with the ability to click on each for their respective Class Tab
* Add Class Button (Opens the Add Class Tab)

Lab List Tab: Free Fall, Projectile Motion, etc (each opens up their Lab tab)
* List of Labs by Category, with the ability to click on each for their respective Lab tab
* Search Bar (edits List to show the closest matches)
* Add Lab Button (Opens the Add Lab Tab)  

Item List Tab: 
* List of Items by Alphabetical Order, with the ability to click on each for their respective Item tab
* Add Item Button (Opens the Add Item Button)

Quick Search:  
Should be a little search bar that search the names of Lab, Items, Classes, and maybe Locations 


Class Tab:
* Class Name
* List of Labs that Class covers in general order (the order of labs and the labs covered varies slightly each semester, hopefully when the calendar feature is implimented it can reflect that)

Lab Tab:  
* Lab Name
* Lab Category
* Equipment Table, with each row:  
        * Number of this item thats required for a table  
        * Item (Opens up to Item tab)  
        * Location of Item  
        * Quantity of Item  
* Lab Pictures  
* Lab Description  
* List of Classes this Lab is in  
        
Item tab:  
* Item Name  
* Item Quantity  
* Item Location (Edits location in all Lab Tabs that contain that Item)  
* Item Description  
* Pictures  


## Database Structure and Programming:

Three General Rules for Databases
1. No Repeating Groups  
2. Data Dependancy on Key  
3. No Redundant Data  

Tables for Inventory  
* Inventory: Item ID | Name | Description  
* LocationTable: LocationID | L0 | L1 | L2 | L3 | L4 | L5  
* QuantityTable: ItemID | LocationID | Quantity  

Tables for Class and Lab Management 
* ClassTable: ClassID | ClassName  
* LabTable: LabID | LabName  
* ClassLabTable: ClassID | LabID
* LabItemsTable: LabID | ItemID | NumPerTable | Num
* ExtrasTable: LabID | ItemID  (For items to be left on extra table)

Random Tables
* LabPics: LabID | Picture Link?
* ItemPics: ItemID | Picture Link?
