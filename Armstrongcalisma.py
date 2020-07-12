number = input('Please insert a number : ')
if  not number.isdigit() :
    print ("It is an invalid entry. Don't use non-numeric, float, or negative values!")
liste = list(number)
summ = 0
if number.isdigit() == True:
    for i in liste:
        basamak = (int(i)) ** len(liste)
        summ += basamak
    if int(number) == summ :
        print(f'{summ} is an Armstrong number')
    else:
        print(f'{number} is not an Armstrong number')