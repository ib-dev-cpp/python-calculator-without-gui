i = input('put your expresion here\n') # taking the expresion from the user 

exec("result = " + i) # executing the code inside the ()

print('The result is %f' % float(result)) # printing the result
