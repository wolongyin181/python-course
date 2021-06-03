def my_maths_function(number1,number2,operation):
    if operation=='add':
        return (number1+number2)
    if operation=='substract':
        return(number1-number2)
    if operation=='multiply':
        return (number1*number2)
    if operation=='divide':
        return(number1/number2)

result=my_maths_function(10,4,'add')
print(result)
