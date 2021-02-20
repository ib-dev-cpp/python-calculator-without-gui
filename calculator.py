f = open('data.txt', 'w') # opening the data.txt file in write mode

i = input('put your expresion here\n') # taking the expresion from the user 

f.write("result = " + i) # writing in the data.txt file 

f.close() # closing the file

f = open('data.txt') # open the data.txt in read mode

exec(f.read()) # executing the code inside the data.txt file

print('The result is %d' % result) # printing the result

f.close() # closing the file
