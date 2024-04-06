# Non-primitive data types -- can hold/store multiple pieces of data

# List - Array - collection of mutable data - can be changed

numbers = [13, 2, 5, 98, 56]
#         0   1  2   3  4

print(numbers)

print(numbers[2]) #index

numbers.append(42) # Add to list
print(numbers)

numbers.insert(2, 16) #set the index number (2), then the number to be inserted
print(numbers)

numbers.pop() # Will remove the number at the end of the list
print(numbers)

numbers.remove(98) # Will also remove, can set the value to be removed
print(numbers)

numbers.sort() # sort values from smallest to largest
print(numbers)

numbers.reverse() # reverse the list order
print(numbers)

print(len(numbers)) # length of a list

print("\n\n\n\n") # Can use to print enter/break line

# Tuple - imutable data (cannot be changed once defined)
# List but using () (imutable) instead of list [] (mutable)


names = ("John", "Jane", "Tom", "Mike")
print(names)
print(names[1])
# print(names[2] = "Steve") will error as this is a tuple
# Thus, cannot use any of the above methods to append/remove
# Can still use ones like "len" and "count" -- as long as they are not changing the list
print(names.count("Mike")) # Will return 1, counts the number of times "Mike" will appear in the list

days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
co_ordinates_of_famous_place = (123.56, 20.3) 


