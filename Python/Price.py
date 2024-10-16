rows=int(input("Enter number of rows"))
for i in range(rows+1):
    j=0
    while j<=i*10000:
        print("*",end=" ")
        j+=1
    print()