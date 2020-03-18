# Creates calculator

def mort_payment(num_of_years, int_rate, loan_amount):
    num_of_terms = num_of_years * 12
    n = (int_rate/100)/12
    
    print(num_of_terms)
    print(n)
    
    payment = loan_amount * (n * (1 + n)**num_of_terms)/(1 + n)**(num_of_terms - 1)
    return payment

mort_payment(30, 6, 250000)
360
0.005
[26]:
1256.2499999999998

# adds interest factors

def mort_payment2(num_of_years, int_rate, loan_amount):
    terms = input("How often will interest be calcuated? Please choose monthly, weekly, or daily.")
       
    if terms == "monthly":
        num_of_terms = num_of_years * 12
        n = (int_rate/100)/12
    elif terms == "weekly":
        num_of_terms = num_of_years * 52
        n = (int_rate/100)/52
    else:
        num_of_terms = num_of_years * 356
        n= (int_rate/100)/356
    
    print(num_of_terms)
    print(n)
    
    payment = loan_amount * (n * (1 + n)**num_of_terms)/(1 + n)**(num_of_terms - 1)
    return payment

mort_payment2(30, 6, 250000)

# How often will interest be calcuated? Please choose monthly, weekly, or daily. daily

10680
0.00016853932584269662
[3]:
42.141932836763026