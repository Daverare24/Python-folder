import array as arr

a = arr.array('i', [12, 34, 56, 78, 90])
print("this array is",str(a))

floatar = arr.array('d', [12.5, 34.6, 56.7, 78.8, 90.9]) 
print("this float array is",str(floatar))

print("the count of 56 is",a.count(56))

#add an element to the array

a.append(1000)
print("the array after appending 1000 is",str(a))

a.reverse()
print("the array after reversing is",str(a))