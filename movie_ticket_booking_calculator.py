base_price = 15                                                            #to store the base price of the movie ticket
age = 21
seat_type = 'Gold'
show_time = 'Evening'

if age > 17:
    print('The user is eligible to book a movie ticket.')

if age >= 21:
    print('The user is eligible for Evening shows.')
else:
    print('User is not eligible for Evening shows.')

is_member = False                                                         #user is not a member
is_weekend = False

discount = 0                                                               #The user qualifies for a discunt if they are a member.
if is_member and age >= 21:                                                #checking if user has membership and using 'and' operator to check if both user and age are true
    discount = 3                                                          #updated discount to 3 inside body of the if statement
    print('The user qualifies for a membership discount.')
else:
    print('The user does not qualify for a membership discount.')
print(f'Discount: {discount}%')                                              #another way is print('Discount:', discount)

extra_charges = 0                                                           #extra charges to apply to movie ticket on weekends only
if is_weekend or show_time == 'Evening':
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')
print(f'Extra charges: R{extra_charges}')

if age >= 18 or age >=21 and (show_time != 'Evening' or is_member):       # I used () to group conditions and control the order in which they are evaluated.
    print('Ticket booking condition satisfied')
    
    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1
    print(f'Service charges: R{service_charges}')

    final_price = base_price + extra_charges + service_charges - discount

    print(f'Final price of the ticket: R{final_price}')
else:
    print('Ticket booking failed due to restrictions.')      


