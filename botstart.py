userName = input()
userID = input()
userPlace = input()
userDateRange = input()
userAge = int(input())
userDateRangeBegin,userDateRangeEnd = input().split("-")
userBio = input()
storeData = f"{userName}\n{userAge}\n{userPlace}\n{userBio}"
storePersonalData = f"{userID}\n{userDateRangeBegin}\n{userDateRangeEnd}\n{userDateRange}"
finalData = storeData + "\n" +storePersonalData
print(finalData)
