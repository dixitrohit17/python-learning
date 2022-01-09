# ---- Print Hello World ---- #
strHelloWorld = "Hello World !"
print (strHelloWorld)
strNewLine = '\n'
# ---- String Quote ---- #
num1 = 1
num2 = 2
SumOfTwoNumber = num1 + num2
print ("Sum of the two numbers: "+str(SumOfTwoNumber))

# ---- Python With String  ---- #
print(' ---- Python With String  ---- ' + strNewLine)
print(strHelloWorld[0])                           # First Letter of the string
print(strHelloWorld[1])                           # Nth letter of the string
print(strHelloWorld[2:])                          # Range of the string
print(strHelloWorld[2:15])                        # Range of the string
print(strHelloWorld * 2)                          # Print string two times
print(strHelloWorld + " " + strHelloWorld + strNewLine)        # Concatinate two strings


# ---- Python With Lists ---- #
print(' ---- Python With Lists  ---- '+ strNewLine)
pyAsianCountryList = ['India', 'Japan', 'Afganistan', 'Bangladesh','Pakistan','Srilanka','Nepal','Bhutan']
pyEuropeContryList = ['Scotland','France','Germany']
print(pyAsianCountryList)
print(pyAsianCountryList [0])
print(pyAsianCountryList [0:3])
print(pyAsianCountryList [2:])

print(pyAsianCountryList + pyEuropeContryList)
print(strNewLine)

# ---- Python With Tuples  ---- #
print(' ---- Python With Tuples  ---- ' + strNewLine)
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print (tuple)               # Prints the complete tuple
print (tuple[0])            # Prints first element of the tuple
print (tuple[1:3])          # Prints elements of the tuple starting from 2nd till 3rd 
print (tuple[2:])           # Prints elements of the tuple starting from 3rd element
print (tinytuple * 2)       # Prints the contents of the tuple twice
print (tuple + tinytuple)   # Prints concatenated tuples
print(strNewLine)

# ---- Python With Dictionary  ---- #
print(' ---- Python With Dictionary  ---- ' +strNewLine)

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values
print(strNewLine)