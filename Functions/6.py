# 6. Write a Python function to check whether a number is in a given range.


def test_range(num):
    if num in range(0,10):
        print( " %s is in the range"%str(num))
    else :
        print("The number is outside the given range.")


sample = int(input("Enter a number: "))

test_range(sample)