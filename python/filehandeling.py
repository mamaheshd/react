myfile=open('test.txt')
print(myfile)

#read the file content 
print(myfile.read())

#if you went to print the pragraph from certain index number then do the following using seek()
myfile.srrk(6)
print(myfile.read())

myfile.srrk(0)
print(myfile.read())

#readline(): it will return the list of the lines in the file
myfile.srrk(0)
print(myfile.readline())

myfile.close()

#to write to an existing file
wfile=open('test.txt','w')
print(wfile)
wfile.write('This is python program')
wfile.write('\nThis is new line in test files')
wfile.close()




