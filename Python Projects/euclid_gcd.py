num_a = int(input("Enter first number: "))
num_b = int(input("Enter Second Number: "))
val_a = num_a
val_b = num_b
quotient= None
reminder=None

print("""
------------------------------------------------
|     q     |     a     |     b     |     r    |
------------------------------------------------
""")

while(num_b != 0):
    quotient = int(num_a / num_b)
    reminder = num_a % num_b
    print("""
|     {}     |     {}     |     {}     |     {}    |
----------------------------------------------------
    """.format(quotient,num_a,num_b,reminder))
    num_a = num_b
    num_b = reminder

    print("""
|     {}     |     {}     |     {}     |     {}    |
----------------------------------------------------
    """.format(quotient, num_a, num_b, reminder))
print("gcd({},{})={}".format(val_a,val_b,num_a))
