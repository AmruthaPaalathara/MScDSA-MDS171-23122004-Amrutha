"""Create a sportMart class, where  you will have inventory/shelf of items and order of customers. Create csv file 
which will store your inventory details and order details. With the help of file handling techniques in python,read
the file and create an object fro trinity store and populate the inventory items and orders into the trinity store.
To make sure that you have added all the items in your file,use a display method to show your inventory and order 
history. """

class sportMart():
    def __init__(self):
        self.inventory = {}
        self.orders = {}

    def createInventory(self,ProductID,ProductName,Quantity,Price):
        temp={
            "productid" :ProductID,
            "productname" :ProductName,
            "quantity" :Quantity,
            "price" : Price
        }
        self.inventory[ProductID]=temp
    
    def createOrder(self,Orderid,ProductId,Quantity,Price):
        temp={
            "orderid" : Orderid,
            "productid" : ProductId,
            "quantity" : Quantity,
            "price" : Price,
            # "total" : Total  
        }
        self.orders[Orderid] = temp

    def printOrders(self):
        print(self.orders)

    def printInventory(self):
        print(self.inventory)


trinity = sportMart()
orders = open("order.csv","r")
o_header = orders.readline()
o_data = orders.readlines()
for data in o_data:
    tmp = data.strip().split(',')
    trinity.createOrder(tmp[0],tmp[1],tmp[2],tmp[3])

trinity.printOrders()

inventory = open("Inventory.csv","r")
i_header = inventory.readline()
i_data = inventory.readlines()
for data in i_data:
    temp = data.strip().split(',')
    trinity.createInventory(temp[0],temp[1],temp[2],temp[3])

trinity.printInventory()