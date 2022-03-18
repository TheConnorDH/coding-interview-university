# Python program to practice with and become comfortable using arrays
# Connor Horrocks

# Create Array
import array as arr

# Define Array (using ints)
a = arr.array('i', [1, 2, 3])

# Print Array 'a' before insertion
print("Array 'a' is : ", end=" ")
for i in a:
    print(i, end=" ")
print()

# Add value within Array 'a' at specified location
a.insert(1, 4)

# Print Array 'a' after insertion
print("Array 'a' after inserting a new value is : ", end=" ")
for i in a:
    print(i, end=" ")
print()

# Remove value from within Array 'a' at specified location
print("The value being removed from Array 'a' is :", end=" ")
print(a.pop(2))

# Print Array 'a' after removal
print("Array 'a' after removal is : ", end=" ")
for i in a:
    print(i, end=" ")
print()
print()

# Define Array (using floats)
b = arr.array('d', [1.5, 2.6, 4.6])

# Print Array 'b' before insertion
print("Array 'b' is : ", end=" ")
for i in range(0, 3):
    print(b[i], end=" ")
print()

# Add value to the end of Array 'b'
b.append(6.2)

# Print Array 'b' after insertion
print("Array 'b' after inserting a new value is : ", end=" ")
for i in b:
    print(i, end=" ")
print()

# Remove first instance of a specific value from Array 'b'
x = 4.6
b.remove(x)
print("The value being removed from Array 'b' is :", end=" ")
print(x)

# Print Array 'b' after removal
print("Array ''b' after removal is : ", end=" ")
for i in b:
    print(i, end=" ")
print()
print()

# Access element from Array 'a'
print("The accessed element from Array 'a' is : ", a[2])

# Access element from Array 'b'
print("The accessed element from Array 'b' is : ", b[1])
print()

# Calculate average of Array 'a'
mean_a = sum(a)/len(a)
print("The mean of Array 'a' is :", end=" ")
print(mean_a)
print()

# Calculate and print average of Arrays
mean_b = sum(b)/len(b)
print("The mean of Array 'b' is :", end=" ")
print(mean_b)

# Print the number of elements in Array 'a'
print("The number of elements in Array 'a' is :", end=" ")
print(len(a))
print()

# Print the number of elements in Array 'b'
print("The number of elements in Array 'b' is :", end=" ")
print(len(b))
print()

# Print the location of a number in Array 'a'
print("The location of the number 4 in Array 'a' is :", end=" ")
print(a.index(4))
print()

# Print the location of a number in Array 'b'
print("The location of the number 6.2 in Array 'b' is :", end=" ")
print(b.index(6.2))
print()

# Add a number at the beginning of Array 'a'
a.insert(0, 6)
print("Array 'a' after adding a number to the beginning is :", end=" ")
for i in a:
    print(i, end=" ")
print()
print()

# Locate whether an element exists in Array 'a'
j = 6
if j in a:
    print("Element ", j, "exists in Array 'a'")
else:
    print("Element", j, "does not exist in Array 'a'")
