userName = input()
userID = input()
userPlace = input()
userAreaRange = input()
userAge = int(input())
userDateRangeBegin,userDateRangeEnd = input().split("-")
userBio = input()
storeData = f"{userName}\n{userAge}\n{userPlace}\n{userBio}"
storePersonalData = f"{userID}\n{userDateRangeBegin}\n{userDateRangeEnd}\n{userAreaRange}"
finalData = storeData + "\n" +storePersonalData
print(finalData)
