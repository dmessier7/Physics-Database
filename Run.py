import Database_Functions as d
import GUI_Functions as t
import sqlite3 as s

g = d.Location
g.L = ['2', 'B', 'Other Box', '1', '-', '-', '-']

# SearchByItemName('Inventory', 'Oscilloscope')


#d.CreateInventoryTable()
#d.CreateLocationTable()
#d.CreateQuantityTable()
#d.AddItemToInventory('Hammer', 'Hammer', 1)
#d.AddLocation(g)
#d.CreateClassTable()
#d.AddClass("PHYS250")
#d.CreateLabTable()
#d.AddLab("Free Fall", "Looking at Gravity")
#d.CreateClassLabTable()
#d.SearchIDByName("LabTable", "Free Fall")


# SearchByItemName('Inventory', 'Oscilloscope')
# ChangeQuantityOfItemAtLocation()

t.run()

#app = DatabaseApp()
#app.mainloop()

#root.mainloop()

d.conn.close()
