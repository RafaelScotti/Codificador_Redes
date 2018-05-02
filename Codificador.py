import sys
import string

#FUNCAO NRZI
def encodeNRZI(convertBin):
    saidaNRZI=""
    lastSinal = "-"
    #if(tecnica=="nrzi"):
    for n in convertBin:
        if(n=="1"):
            if(lastSinal=="+"):
                saidaNRZI = saidaNRZI + "-"
                lastSinal="-"
            else:
                saidaNRZI = saidaNRZI + "+"
                lastSinal="+"

        elif(n=="0"):
            saidaNRZI = saidaNRZI + lastSinal

    print(saidaNRZI)

#FUNCAO MANCH
def encodeMANCH(convertBin):
    saidaMANCH=""
    if(tecnica=="manch"):
        for n in convertBin:
            if(n=="1"):
                saidaMANCH = saidaMANCH + "-+"
            elif(n=="0"):
                saidaMANCH = saidaMANCH + "+-"
            #saidaMANCH +="

    print(saidaMANCH)

#FUNCAO MLT3
def encodeMLT3(convertBin):
    saidaMLT3=""
    ultimoSinal="0"
    penultimoSinal="-"
    if(tecnica=="mlt3"):
        for n in convertBin:
            if(n=="1" and penultimoSinal=="-" and ultimoSinal=="0"):
                saidaMLT3=saidaMLT3 + "+"
                penultimoSinal = ultimoSinal
                ultimoSinal="+"
            elif(n=="1" and penultimoSinal=="0" and ultimoSinal=="+"):
                saidaMLT3  += "0"
                penultimoSinal = ultimoSinal
                ultimoSinal = "0"
            elif(n=="1" and penultimoSinal=="0" and ultimoSinal=="-"):
                saidaMLT3+="0"
                penultimoSinal = ultimoSinal
                ultimoSinal = "0"
            elif(n=="1" and penultimoSinal=="+" and ultimoSinal=="0"):
                saidaMLT3+="-"
                penultimoSinal = ultimoSinal
                ultimoSinal="-"
            elif(n=="0"):
                saidaMLT3+=ultimoSinal
            #saidaMLT3+=" "
    print(saidaMLT3)


#FUNCAO 8B10B
def encode8B10B(convertBin):
    while((len(convertBin)%8)!=0):
        convertBin="0"+convertBin
    #print(convertBin)
    rd = "-1"    
    saida8B10B = ""
    cont = 0
    while(cont<len(convertBin)):
        bits = ""
        contBits = 0
        while(contBits<8):
            bits+=convertBin[cont]
            cont+=1
            contBits+=1
        #cont+=1
        #print(bits)
        saida8B10B+=tabela8B10B(bits, rd)
        if(rd=="-1"):
            rd="+1"
        else:
            rd="-1"    
    encodeNRZI(saida8B10B)

def tabela8B10B(bits, rd):
    v34 = bits[0:3]
    v56 = bits[3:8]
    #print("."+v56+".")
    saida = ""

    #tabela 5b10b
    if(v56=="00000"):           #0
        saida = "100111" if rd=="-1" else "011000"
    elif(v56=="00001"):         #1
        saida = "011101" if rd=="-1" else "100010"
    elif(v56=="00010"):         #2
        saida = "101101" if rd=="-1" else "010010"
    elif(v56=="00011"):         #3
        saida = "110001"
    elif(v56=="00100"):         #4
        saida = "110101" if rd=="-1" else "001010"
    elif(v56=="00101"):         #5
        saida = "101001"
    elif(v56=="00110"):         #6
        saida = "011001"
    elif(v56=="00111"):         #7
        saida = "111000" if rd=="-1" else "000111"
    elif(v56=="01000"):         #8
        saida = "111001" if rd=="-1" else "000110"
    elif(v56=="01001"):         #9
        saida = "100101"
    elif(v56=="01010"):         #10
        saida = "010101"
    elif(v56=="01011"):         #11
        saida = "110100"
    elif(v56=="01100"):         #12
        saida = "001101"
    elif(v56=="01101"):         #13
        saida = "101100"
    elif(v56=="01110"):         #14
        saida = "011100"
    elif(v56=="01111"):         #15
        saida = "010111" if rd=="-1" else "101000"
    elif(v56=="10000"):         #16
        saida = "011011" if rd=="-1" else "100100"
    elif(v56=="10001"):         #17
        saida = "100011"
    elif(v56=="10010"):         #18
        saida = "010011"
    elif(v56=="10011"):         #19
        saida = "110010"
    elif(v56=="10100"):         #20
        saida = "001011"
    elif(v56=="10101"):         #21
        saida = "101010"
    elif(v56=="10110"):         #22
        saida = "011010"
    elif(v56=="10111"):         #23
        saida = "111010" if rd=="-1" else "000101"
    elif(v56=="11000"):         #24
        saida = "110011" if rd=="-1" else "001100"
    elif(v56=="11001"):         #25
        saida = "100110"
    elif(v56=="11010"):         #26
        saida = "010110"
    elif(v56=="11011"):         #27
        saida = "110110" if rd=="-1" else "001001"
    elif(v56=="11100"):         #28
        saida = "001110"
    elif(v56=="11101"):         #29
        saida = "101110" if rd=="-1" else "010001"
    elif(v56=="11110"):         #30
        saida = "011110" if rd=="-1" else "100001"
    elif(v56=="11111"):         #31
        saida = "101011" if rd=="-1" else "010100"
    else:
        return "\nErro: Valores invalidos"
    

    #tabela 3b4b
    if(v34=="000"):             #0
        saida += "1011" if rd=="-1" else "0100"
    elif(v34=="001"):           #1
        saida += "1001"
    elif(v34=="010"):           #2
        saida += "0101"
    elif(v34=="011"):           #3
        if(rd=="-1"):
            saida += "1100"
        else:
            saida += "0011"
    elif(v34=="100"):           #4
        if(rd=="-1"):
            saida += "1101"
        else: 
            saida += "0010"
    elif(v34=="101"):           #5
        saida += "1010"
    elif(v34=="110"):           #6
        saida += "0110"
    elif(v34=="111"):           #7 
        if(rd=="+1"):
            if(v56=="01011" or v56=="01101" or v56=="01110"): #D.x.A7 - x11, x13, x14 RD +1
                saida += "1000"
                #print("D.x.A7 - x11, x13, x14 RD +1")
            else:
                saida += "0001" #D.x.P7
                #print("P7+")
        elif(rd=="-1"):
            if(v56=="10001" or v56=="10010" or v56=="10100"): #D.x.A7 - x17, x18, x20 RD -1
                saida += "0111"
                #print("D.x.A7 - x17, x18, x20 RD -1")
            else:
                saida += "1110" #D.x.P7
                #print("P7-")
    else:
        return "\nErro: Valores invalidos"
    
    return saida



#===main===
#variaveis utilizadas
tecnica = ""
valorHexa = ""

if(len(sys.argv)==3):
    tecnica = sys.argv[1]
    valorHexa = sys.argv[2]
    if(all(c in string.hexdigits for c in valorHexa)):
        pass
    else:
        print("Erro: Codigo hexadecimal invalido!")
        sys.exit()
else:
    print("Erro: Vc deve digitar dois argumentos <tecnica codificacao> <valor hexa>")
    sys.exit()

t = len(valorHexa)*4 #completa total de bits
convertBin = (bin(int(valorHexa, 16))[2:]).zfill(t)#Converte para binario
#print(convertBin)


if(tecnica=="nrzi"):
    encodeNRZI(convertBin)
elif(tecnica=="manch"):
    encodeMANCH(convertBin)
elif(tecnica=="mlt3"):
    encodeMLT3(convertBin)
elif(tecnica=="8b10b"):
    encode8B10B(convertBin)
else:
    print("Erro: Tecnica invalida")
    sys.exit()
