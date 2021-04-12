#the sum function takes a number and a function square or cube as an argument
#it then calculates the sum of square or cubes of numbers ranging 1 to num + 1

def sum(num, function):
    total =0
    for i in range (1,num+1):
        total = total + function(i)
    return total

def square(x):
    return x*x

def cube(x):
    return x*x*x

print("The sum of squares is:")
print(sum(3,square))
print("\nThe sum of cubes is:")
print(sum(3,cube))
