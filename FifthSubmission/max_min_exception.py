largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == 'done' :
        break
    try:
        num2 = int(num)
        if largest is None :
            largest = num2
        elif num2 > largest :
            largest = num2

        if smallest is None :
            smallest = num2
        elif num2 < smallest :
            smallest = num2
    except:
        print('Invalid input')
        continue


print("Maximum is", largest)
print("Minimum is", smallest)
