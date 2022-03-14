Mark = input("Enter Mark: ")

Mark = int(Mark)

if Mark < 25:
    print(" F ")

elif Mark >= 25 and Mark < 45:
    print(" E ")

elif Mark >= 45 and Mark < 50:
    print(" D ")

elif Mark >= 50 and Mark < 60:
    print(" C ")

elif Mark >= 60 and Mark < 80:
    print(" B ")

else:
    print(" A ")