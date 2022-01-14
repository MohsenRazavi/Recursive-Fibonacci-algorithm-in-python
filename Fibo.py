def Fibo(n):
    # define 3 variables . consider they are  first three numbers ...
    # the value you assign to c is not important
    a = 1
    b = 1
    c = 0
    print(a, b, end=' ')
    for i in range(n):
        c = a + b
        a = b
        b = c
        print(c, end=' ')


# getting n from input
n = int(input('Enter an integer number : '))
# calling the Fibo function
Fibo(n)

# You can Find Me on the link github.com/MohsenRazavi
