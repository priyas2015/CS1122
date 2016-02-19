#Priya Shah
#Homework 3
#CS1122


import binascii 

#Question Two - Converting decimal to binary 

def convertToBinary(num):

   if num > 1:
       convertToBinary(num//2)
       
   print(num % 2,end = '')


#Question Three - convert hexadecimal digits to ASCII

def convertToASCII(hexadecimal):
    word = ''
    
    for i in hexadecimal:
        num = i[2:]
        x = binascii.unhexlify(num)
        word += str(x)[2:3]
    
    return word



#Question Four - convert binay numbers to hexadecimal

def convertBinaryToHex(binary):

    return hex(int(binary,2))



#Question Five - convert octal digits to decimal

def convertOctal(num):

    toReturn = 0
    stringNum = str(num)

    power = len(stringNum) - 1


    for i in stringNum:
        x = int(i)
        
        toReturn += (x*(8**power))

        power -= 1

    return toReturn

def main():

    convertToBinary(57) #2a
    print('\n')
    convertToBinary(123) #2b
    print('\n')
    convertToBinary(85) #2c
    print('\n')
    convertToBinary(38) #2d
    print('\n')

    lst1 = ['0x41', '0x53', '0x43', '0x49', '0x49', '0x20', '0x77', '0x68', '0x61', '0x74', '0x20', '0x79', '0x6f', '0x75', '0x20', '0x64', '0x69', '0x64', '0x20', '0x74', '0x68', '0x65', '0x72', '0x65']
    lst2 = ['0x39', '0x41', '0x4d', '0x20', '0x69', '0x73', '0x20', '0x74', '0x6f', '0x6f', '0x20', '0x65', '0x61', '0x72', '0x6c', '0x79', '0x20', '0x66', '0x6f', '0x72', '0x20', '0x63', '0x6c', '0x61', '0x73', '0x73']
    lst3 = ['0x43', '0x6f', '0x6d', '0x70', '0x75', '0x74', '0x65', '0x72', '0x73', '0x20', '0x61', '0x72', '0x65', '0x20', '0x6d', '0x61', '0x67', '0x69', '0x63']
    lst4 = ['0x57', '0x68', '0x61', '0x74', '0x20', '0x74', '0x68', '0x65', '0x20', '0x68', '0x65', '0x78', '0x3f']
     

    print(convertToASCII(lst1)) #3a
    print(convertToASCII(lst2)) #3b
    print(convertToASCII(lst3)) #3c
    print(convertToASCII(lst4)) #3d

    
    print(convertBinaryToHex('00001011101011101101111010101101')) #4a
    print(convertBinaryToHex('11001010111111101111101011001110')) #4b
    print(convertBinaryToHex('10111110111011111101000000001101')) #4c
    print(convertBinaryToHex('00001011101011101101111010101101')) #4d


    print(convertOctal(10)) #5a
    print(convertOctal(42)) #5b
    print(convertOctal(77)) #5c
    print(convertOctal(113)) #5d

   
main()
