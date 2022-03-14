P_1 = int(input("Enter Age of 1st Person: "))
P_2 = int(input("Enter Age of 2nd Person: "))
P_3 = int(input("Enter Age of 3rd Person: "))

# OLDEST

if P_1 > P_2 and P_1 > P_3:
    print("1st Person Oldest")

elif P_2 > P_1 and P_2 > P_3:
    print("2nd Person Oldest")

else:
    print("3rd Person Oldest")

# YOUNGEST

if P_1 < P_2 and P_1 < P_3:
    print("1st Person Youngest")

elif P_2 < P_1 and P_2 < P_3:
    print("2nd Person Youngest")

else:
    print("3rd Person Youngest")