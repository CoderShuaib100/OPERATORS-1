# creating the algorithm

demand = int(input("Enter the amount: "))

notes200 = demand // 200
demand = demand % 200
notes100 = demand // 100
demand = demand % 100

print("₹200 notes: ", notes200)
print("₹100 notes: ", notes100)