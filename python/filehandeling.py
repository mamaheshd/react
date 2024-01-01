myfile=open('test.txt')
print(myfile)

#read the file content 
print(myfile.read())

#if you went to print the pragraph from certain index number then do the following using seek()
myfile.seek(6)
print(myfile.read())

myfile.seek(0)
print(myfile.read())

#readline(): it will return the list of the lines in the file
myfile.seek(0)
print(myfile.readline())

myfile.close()

#to write to an existing file
wfile=open('test.txt','w')
print(wfile)
wfile.write('This is python program')
wfile.write('\nThis is new line in test files')
wfile.close()

#create a new file using w if the file is not exist
newfile=open('abc.txt','w')
print(newfile)
newfile.write('This is python program')
newfile.write('\nThis is new line in test files')
newfile.close()


