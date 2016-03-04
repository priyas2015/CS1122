REFERNCE = {

    1: "ADD",
    2: "SUB",
    3: "STA",
    5: "LDA",
    6: "BRA",
    7: "BRZ",
    8: "BRP"

    }

def disassemble(code):
    x = ''
    if  str(code)[0] != '0' and str(code)[0] != '9':
        
            x = x + INS_REF[int(str(code)[0])]
            x = x + ' '+ str(code)[1:]
            
    elif str(code)[0] == '0':
        
            x = x + 'HTL'
            
    elif str(code)[0] == '9':
        
            if str(code)[2] == '2':
                x = x + 'OUT'
                
            if str(code)[2] == '1':
                x = x + 'INP';
    return x
    

def main:

    assembly = [901,221,309,901,308,509]

    disassembled = ''

    for i in assembly:
            disassembled = disassembled + disassemble(i) + '\n'
            i = i + 1

    print(disassembled)

if __name__ == "__main__":
    main()
