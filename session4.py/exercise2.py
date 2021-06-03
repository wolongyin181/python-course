def shopping_calculator(shopping_cost,discount_applicable):

    if(shopping_cost>20 and discount_applicable ==True):
        return (shopping_cost*0.9)
    elif(shopping_cost>100 and discount_applicable == False):
        return (shopping_cost*0.95)
    else:
        return (shopping_cost)
 

total_shopping_cost = shopping_calculator(30,False)
print(f'The total shopping cost is £{total_shopping_cost}')