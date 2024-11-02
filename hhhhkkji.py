"""

for count in range (1, 11, 1):
    print(count, "->" )
"""
"""
count=1
while count<11:
    print(count)
    count=count+1
"""
"""
for count in range (9, 0, -1):
    print(count, "->")


"""
"""
total=0
option=input("Vendos y per te shtuar ose n per te hequr")
flag=True

while flag:
    option = input ("Vendos y per te shtuar ose n per te hequr ")
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
