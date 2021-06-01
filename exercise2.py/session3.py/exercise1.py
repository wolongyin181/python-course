shirt_price = float(input('What is the price of the shirt?'))
shirt_colour = str(input('What is the colour of the shirt?'))

shirt_in_budget = shirt_price <=25.00
shirt_correct_colour = shirt_colour == 'yellow'
print (f'Shirt is available within budget and correct colour:{shirt_in_budget == True and shirt_correct_colour == True}')