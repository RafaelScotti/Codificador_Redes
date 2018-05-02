import sys
import string

#FUNCAO NRZI
def nrzi(convertBin):
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
def manch(convertBin):
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
def mlt3(convertBin):
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
def t8b10b(convertBin):
    while((len(convertBin)%8)!=0):
        convertBin="0"+convertBin
    print(convertBin)

    saida8B10B = ""
    rd = "-1"
    v34 = ""
    v56 = ""
    cont = 0
    #contV = 3 #ate 3
    

    while(cont<len(convertBin)):
        v34 = convertBin[cont:cont+3]
        cont+=3
        v56 = convertBin[cont:cont+5]
        cont+=5
        #contV += cont
        #print("."+v56+".\n")
        saida8B10B+= tabela5B6B(v56, rd) + tabela3B4B(v34, rd)+" "
        if(rd=="-1"):
            rd="+1"
        else:
            rd="-1"
    #print("."+v34+".\n"+"."+v56+".")
    #print(v34, v56)
    print("\n"+saida8B10B)
    print(len(convertBin))

def tabela5B6B(v56, rd):
    if(v56=="00000"):         #0
        return "100111" if rd=="-1" else "011000"
    elif(v56=="00001"):         #1
        return "011101" if rd=="-1" else "100010"
    elif(v56=="00010"):         #2
        return "101101" if rd=="-1" else "010010"
    elif(v56=="00011"):         #3
        return "110001"
    elif(v56=="00100"):         #4
        return "110101" if rd=="-1" else "001010"
    elif(v56=="00101"):         #5
        return "101001"
    elif(v56=="00110"):         #6
        return "011001"
    elif(v56=="00111"):         #7
        return "111000" if rd=="-1" else "000111"
    elif(v56=="01000"):         #8
        return "111001" if rd=="-1" else "000110"
    elif(v56=="01001"):         #9
        return "100101"
    elif(v56=="01010"):         #10
        return "010101"
    elif(v56=="01011"):         #11
        return "110100"
    elif(v56=="01100"):         #12
        return "001101"
    elif(v56=="01101"):         #13
        return "101100"
    elif(v56=="01110"):         #14
        return "011100"
    elif(v56=="01111"):         #15
        return "010111" if rd=="-1" else "101000"
    elif(v56=="10000"):         #16
        return "011011" if rd=="-1" else "100100"
    elif(v56=="10001"):         #17
        return "100011"
    elif(v56=="10010"):         #18
        return "010011"
    elif(v56=="10011"):         #19
        return "110010"
    elif(v56=="10100"):         #20
        return "001011"
    elif(v56=="10101"):         #21
        return "101010"
    elif(v56=="10110"):         #22
        return "011010"
    elif(v56=="10111"):         #23
        return "111010" if rd=="-1" else "000101"
    elif(v56=="11000"):         #24
        return "110011" if rd=="-1" else "001100"
    elif(v56=="11001"):         #25
        return "100110"
    elif(v56=="11010"):         #26
        return "010110"
    elif(v56=="11011"):         #27
        return "110110" if rd=="-1" else "001001"
    elif(v56=="11100	"):         #28
        return "001110"
    elif(v56=="11101"):         #29
        return "101110" if rd=="-1" else "010001"
    elif(v56=="11110"):         #30
        return "011110" if rd=="-1" else "100001"
    elif(v56=="11111"):         #31
        return "101011" if rd=="-1" else "010100"
    else:
        return "\nErro: Valores invalidos"
    return "ok"

def tabela3B4B(v34, rd):
    if(v34=="000"):             #0
        return "1011" if rd=="-1" else "0100"
        #if(rd=="-1"):
        #    return "1011"
       # else:
        #    return "0100"
    elif(v34=="001"):           #1
        return "1001"
    elif(v34=="010"):           #2
        return "0101"
    elif(v34=="011"):           #3
        if(rd=="-1"):
            return "1100"
        else:
            return "0011"
    elif(v34=="100"):           #4
        if(rd=="-1"):
            return "1101"
        else: 
            return "0010"
    elif(v34=="101"):           #5
        return "1010"
    elif(v34=="110"):           #6
        return "0110"
    elif(v34=="111"):           #7 - falta implementar as outras formas
        if(rd=="-1"):
            return "1110"
        else:
            return "0001"
    else:
        return "\nErro: Valores invalidos"
    return "ok"

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
    nrzi(convertBin)
elif(tecnica=="manch"):
    manch(convertBin)
elif(tecnica=="mlt3"):
    mlt3(convertBin)
elif(tecnica=="8b10b"):
    t8b10b(convertBin)
else:
    print("Erro: Tecnica invalida")
    sys.exit()
