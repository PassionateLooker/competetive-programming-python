kara=int(input("Enter kara sold:"))
rani=int(input("Enter rani sold:"))

karaMoney=kara*5
raniMoney=rani*7

print("Kara earned ",kara*5)
print("Rani earned ",rani*7)
if karaMoney>raniMoney:
    print("Kara earned more than rani")
else:
    print("Rani earned more than Kara")