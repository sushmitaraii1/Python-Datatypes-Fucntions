# 1. Write a Python function to find the Max of three numbers.
def maximum(a,b,c):
    return max(a,b,c)


x = input("Enter three numbers separated with space: ").split()
a = int(x[0])
b = int(x[1])
c = int(x[2])
print(f"Maximum numer is {maximum(a,b,c)}.")