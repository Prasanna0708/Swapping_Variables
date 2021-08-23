a = 5
b = 6

'''
# Using 3rd variable 
temp = a
a = b
b = temp'''

'''#using Formula

a = a+b     #11
b = a-b     #11-6 = 5
a = a-b     #11-5 = 6'''

'''#using XOR operation

a = a ^ b
b = a ^ b
a = a ^ b'''

#without using 3rd variable and bits

a,b = b,a


print(a)
print(b)