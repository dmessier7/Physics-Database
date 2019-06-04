# Physics-Database
Database Program for Physics and Engineering Inventory

## Objective:   
An interface for use by the lab techs and lab assistants to keep track of inventory, see the items required for lab set ups, and help ensure there's enough of what's need for set ups. At first this will be localized to one computer, but hopefully eventually we can connect it to the lab's cloud file storage to allow multiple computers to use and edit the system.

The progam will be written in python, using the sqlite library to create, manage, and pull from the database(s). What will be used for the GUI isn't super concrete. Right now I'm using PyQt5 which isn't amazing, so something else might work better. tKinter wasn't used because of limitations on the placement and style.

## Funcationality Requirements:
My idea for the GUI is a window with the main menu on the side at all times taking up ~1/4 of the window, and a space for tabs taking up the other 3/4 of window. Tabs are similar to tabs on an internet browser.

Main Menu:  
Top   
* Lab List  
* Item List  
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


Class Tab:

Lab Tab: (eg Projectile Motion, Ohm's Law)  
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

There are three main Tables for Inventory  
1. InventoryTable: Item ID | str Name | str Description  
2. LocationTable: LocationID | str L0 | str L1 | str L2 | str L3 | str L4 | str L5  
3. QuantityTable: ItemID | LocationID | int Quantity  

Tables for Classes and Labs  
* Classes: Class ID | str ClassName  
* Labs: Lab ID | str LabName  
* ClassLab: Class ID | Lab ID
* LabItems: Lab ID | Item ID

