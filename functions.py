# defining the function. 
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price * ((100 - discount_percent)/100)
    else:
        final_price = price
    
    return final_price

# function call

discount_price = calculate_discount(float(input('Enter original price: ')), float(input('Enter percent discount: ')))

print(discount_price)