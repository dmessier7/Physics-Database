
import MultiTableLabDatabase as m

conn = m.s.connect('PhysicsDatabase.db')
m.c = conn.cursor()

# run()


g = m.Location
g.L = ['2', 'B', 'Other Box', '1', '-', '-', '-']

# SearchByItemName('Inventory', 'Oscilloscope')

m.CreateInventoryTable('Inventory')
m.CreateLocationTable('LocationTable')
m.CreateQuantityTable('QuantityTable')
m.AddItemToInventory('Hammer', 'Hammer')
m.AddLocation(g)
# SearchByItemName('Inventory', 'Oscilloscope')

# CreateOrAddQuantity(4593003696, 4593003440, 5)

# ChangeQuantityOfItemAtLocation()

# app = DatabaseApp()
# app.mainloop()

# root.mainloop()

conn.close()
