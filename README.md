# Physics-Database
Database Program for Physics and Engineering Inventory

Objective: An interface for use by the lab techs and lab assistants to keep track of inventory, see the items required for lab set ups, and help ensure there's enough of what's need for set ups. At first this will be localized to one computer, but hopefully eventually we can connect it to the lab's cloud file storage to allow multiple computers to use and edit the system.

The progam will be written in python, using the sqlite library to create, manage, and pull from the database(s). What will be used for the GUI isn't super concrete. Right now I'm using PyQt5 which isn't amazing, so something else might work better. tKinter wasn't used because of limitations on the placement and style.

<p>Funcationality Requirements:</br>
    Main Menu</br>
        Class List :Phys 250, Phys 270, etc. (each opens up their Class tab)</br>
        Search  for Item (gives Item tab)</br>
             -Should show similar Items while you type in the name of the new one,</br>
                because it only stops against exact name dublicates</br>
        Lab List</br>
        Item List</br>
        Add Item (adds Item to the Item Database)</br>
             -Should show similar Items while you type in the name of the new one,</br>
                because it only stops against exact name dublicates</br>
        Search for Lab (gives Lab Tab)</br>
        Add Lab (add Lab to Lab Database)</br>
        Add Class (adds Class to Class Database)</p>
        
    Class Tab (eg Phys 250)</br>
        Class Name</br>

        Lab List: Free Fall, Projectile Motion, etc (each opens up their Lab tab)</br>
    Lab Tab (eg Projectile Motion, Ohm's Law)</br>
        Lab Name</br>
        Equipment Table, with each row:</br>
            Number of this item thats required for a table</br>
            Item (Opens up to Item tab)</br>
            Location of Item</br>
            Quantity of Item</br>
        Lab Pictures</br>
        Lab Description</br>
        List of Classes this Lab is in</br>
    Item tab</br>
        Item Name</br>
        Item Quantity</br>
        Item Location (Edits location in all Lab Tabs that contain that Item)</br>
        Item Description</br>
        Pictures</p>


Database Structure and Programming:

<p>Three General Rules for Databases</p>
<ol>
    <li>No Repeating Groups</li>
    <li>Data Dependancy on Key</li>
    <li>No Redundant Data</li>
</ol>

<p>There are three main Tables for Inventory</br>
  InventoryTable</br>
    Item ID | str Name | str Description</br>
  LocationTable</br>
    LocationID | str L0 | str L1 | str L2 | str L3 | str L4 | str L5</br>
  QuantityTable</br>
    ItemID | LocationID | int Quantity<p>

<p>Tables for Classes and Labs</br>
  Classes (e.g. PHYS 250, PHYS 210)</br>
    Class ID | str ClassName</br>
  Labs (e.g. Projectile Motion, RC Circuits)</br>
    Lab ID | str LabName</br>
  Matches</br>
    Class ID | Lab ID</br>

