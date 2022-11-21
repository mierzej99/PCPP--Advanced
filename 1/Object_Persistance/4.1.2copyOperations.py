class Delicacy:
    def __init__(self, param):
        self.name = param['name']
        self.price = param['price']
        self.weight = param['weight']

    def __str__(self):
        return f'name - {self.name}, price - {self.price}, weight - {self.weight}'


import copy
warehouse = list()
warehouse.append(Delicacy({'name': 'Lolly Pop', 'price': 0.4, 'weight': 133}))
warehouse.append(Delicacy({'name': 'Licorice', 'price': 0.1, 'weight': 251}))
warehouse.append(Delicacy({'name': 'Chocolate', 'price': 1, 'weight': 601}))
warehouse.append(Delicacy({'name': 'Sours', 'price': 0.01, 'weight': 513}))
warehouse.append(Delicacy({'name': 'Hard candies', 'price': 0.3, 'weight': 433}))

copy_warehouse = copy.deepcopy(warehouse)

for item in copy_warehouse:
    if item.weight > 300:
        item.price = item.price*0.8



print('Source list of candies')
for item in warehouse:
    print(item)

print('Proposal list of candies')

for item in copy_warehouse:
    print(item)