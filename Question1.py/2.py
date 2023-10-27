"""Create a menu driven program that will create new orders and update the inventory accordingly.
Export the final data to the file."""

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
        self.inventory[ProductID] = temp
    
    def createOrder(self,Orderid,ProductId,Quantity,Price):
        temp={
            "orderid" : Orderid,
            "productid" : ProductId,
            "quantity" : Quantity,
            "price" : Price,
            # "total" : Total  
        }
        self.orders[Orderid] = temp

    def new_order(self,Orderid,ProductId,Quantity,Price):
        tmp={
            "orderid" : Orderid,
            "productid" : ProductId,
            "quantity" : Quantity,
            "price" : Price 
        }
        self.orders[Orderid] = tmp

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

while True:
    def neworder():
        choose=int(input("Enter your choose : "))
        if choose==1:
            print("Create new order")
            trinity.new_order()
            neworder1=trinity.createOrder()
            trinity.createOrder.append(neworder1)

    neworder()
        


