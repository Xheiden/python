

flag=True

while flag:
    option = input("Vendos y per te shtuar ose n per te hequr")
    if (option=='y'):
        nr=int(input("Vendos numrin: "))
        total+=nr
    elif (option=='n'):
        nr = int(input("Vendos numrin: "))
        total-=nr
    else:
        print("Totali juaj eshte: ", total)
        flag=False
"""
for count in range(1, , 3):
    print(count, "->", count**2)