import Database_Functions as d

conn = d.s.connect('PhysicsDatabase.db')
d.c = conn.cursor()

# run()


g = d.Location
g.L = ['2', 'B', 'Other Box', '1', '-', '-', '-']

# SearchByItemName('Inventory', 'Oscilloscope')

d.CreateInventoryTable('Inventory')
d.CreateLocationTable('LocationTable')
d.CreateQuantityTable('QuantityTable')
d.AddItemToInventory('Hammer', 'Hammer')
d.AddLocation(g)
# SearchByItemName('Inventory', 'Oscilloscope')

# CreateOrAddQuantity(4593003696, 4593003440, 5)

# ChangeQuantityOfItemAtLocation()

# app = DatabaseApp()
# app.mainloop()

# root.mainloop()

conn.close()
