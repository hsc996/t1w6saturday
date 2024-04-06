# while loop

x = 1
while x <= 5: # 1 <= 5 = True
    print(x) # 1
    x += 1 # (or x = x +1) 1 + 1 etc + will break before 6

print("the end")

# For loop

students = ["John", "Hannah", "Tash", "Mike"]

for student in students:
    print(student)

for i in range(101): # This will print 1-100
    print(i)

for i in range(1, 101): # For even numbers
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")

list_even = []
list_odd = []

for i in range(1, 101): # For even numbers
    if i % 2 == 0:
        list_even.append(i)
    else:
        list_odd.append(i)

print(f"Even list: {list_even}")
print("\n")
print(f"Odd list: {list_odd}")
