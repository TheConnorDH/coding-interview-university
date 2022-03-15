# Python program to practice with and become comfortable using arrays

#Create Array
import array as arr

#Define Array (using ints)
a = arr.array('i', [1, 2, 3])
x = len(a)

#Print Array 'a'
print ("The new created array is : ", end =" ")
for i in range (0, x):
    print (a[i], end =", ")
print()

#Define Array (using floats)
b = arr.array('d', [1.5, 2.6, 4.6])
y = len(b)

#Print Array 'b'
print ("The new created array is : ", end =" ")
for d in range (0, y):
    print (b[i], end =", ")






