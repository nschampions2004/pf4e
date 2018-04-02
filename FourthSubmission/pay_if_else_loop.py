hrs = input("Enter Hours:")
rate = input("Enter rate:")
ot_rate = float(rate)*1.5
pay = float()
if(float(hrs) > 40) :
     pay = (float(hrs)-40)*ot_rate + 40*float(rate)
else :
     pay = float(hrs)*float(rate)

print(pay)
