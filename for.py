prices = [5000, 3000, 2000, 1000]
months = [6, 9, 12]
mas = 0.7


#Nested for loops
for month in months:
    for price in prices:
        #סדר את זה יפה
        Neto = price * month * mas
        print("The net monthly salary is ")
        print(Neto)