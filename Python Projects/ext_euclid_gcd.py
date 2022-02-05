# t = t1 - q x t2

num_a = int(input("Enter first number: "))
num_b = int(input("Enter Second Number: "))
val_a = num_a
val_b = num_b
quotient = None
reminder = None
t1 = 0
t2 = 1
t =None

print("""
--------------------------------------------------------------------------------------
|     q     |     a     |     b     |     r    |     t1     |     t2     |     t     |
--------------------------------------------------------------------------------------

""")

while(num_b != 0):
    quotient = int(num_a / num_b)
    reminder = num_a % num_b
    t = t1 - (t2 * quotient)
    print("""
|     {}     |     {}     |     {}     |     {}    |     {}    |     {}    |     {}    |   
------------------------------------------------------------------------------------------------
    """.format(quotient, num_a, num_b, reminder,t1,t2,t))
    num_a = num_b
    num_b = reminder
    t1 = t2
    t2 = t


    print("""
|     {}     |     {}     |     {}     |     {}    |     {}    |     {}    |     {}    |    
---------------------------------------------------------------------------------------------
    """.format(quotient, num_a, num_b, reminder, t1, t2, t))
print("gcd({},{})={}".format(val_a, val_b, num_a))
