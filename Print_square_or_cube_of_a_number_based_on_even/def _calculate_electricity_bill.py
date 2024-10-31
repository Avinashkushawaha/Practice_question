def calculate_electricity_bill(units):
    if units <= 100:
        bill = 0
    elif units <= 200:
        bill = (units - 100) * 0.5
    else:
        bill = (100 * 0.5) + ((units - 200) * 10)
        print(f" Total bill: ₹{bill}")

calculate_electricity_bill(350)        
