def Fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return Fibo(n-1) + Fibo(n-2)


n = int(input("Enter an integer number : "))
print(Fibo(n))


# You can find me on the link github.com/MohsenRazavi
