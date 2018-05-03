import sys
import string


#sinais = "---+++----+--+++"
#sinais = "+++000-0"
#tecnica = "mlt3"

def convert(binSring):
    return hex(int(binSring, 2))[2:]

def decodeNRZI(sinais):
    saidaNRZI = ""
    primeiroSinal = "-"
    for n in sinais:
        if(primeiroSinal == n):
            saidaNRZI+="0"
        else:
            saidaNRZI+="1"
            if(primeiroSinal=="-"):
                primeiroSinal="+"
            else:
                primeiroSinal="-"
    return saidaNRZI


def decodeMANCH(sinais):
    saidaMANCH = ""
    cont = 0
    while(cont <= len(sinais)-2):
        if(sinais[cont]==sinais[cont+1]):
            erro(saidaMANCH)
        else:
            if(sinais[cont]=="-" and sinais[cont+1]=="+"):
                saidaMANCH+="1"
            elif(sinais[cont]=="+" and sinais[cont+1]=="-"):
                saidaMANCH+="0"
            else:
                erro(saidaMANCH)
        cont+=2
    if(len(sinais) % 2 == 0 and sinais!=""):
        return saidaMANCH
    else:
        print ("Numero de sinais incorreto")
        erro(saidaMANCH)


def decodeMLT3(sinais):
    saidaMLT3 = ""
    us = "0"
    sa = "-"
    for n in sinais:
        if(n=="0"):
            if(us=="0"):
                saidaMLT3+="0"
            else:
                if(us=="+" and (sa=="-" or sa=="0")):
                    saidaMLT3+="1"
                    us="0"
                    sa="+"
                elif(us=="-" and (sa=="+" or sa=="0")):
                    saidaMLT3+="1"
                    us="0"
                    sa="-"
                else:
                    erro(saidaMLT3)
                    #print("Erro")
                    #sys.exit()
        elif(n=="+"):
            if(us=="+"):
                saidaMLT3+="0"
            else:
                if(us=="0" and sa=="-"):
                    saidaMLT3+="1"
                    us="+"
                    sa="0"
                else:
                    erro(saidaMLT3)
                    #print("Erro")
                    #sys.exit()
        elif(n=="-"):
            if(us=="-"):
                saidaMLT3+="0"
            else:
                if(us=="0" and sa=="+"):
                    saidaMLT3+="1"
                    us="-"
                    sa="0"
                else:
                    erro(saidaMLT3)
                    #print("Erro")
                    #sys.exit()
        else:
            erro(saidaMLT3)
            print("sinal invalido")
            #sys.exit()
    return saidaMLT3

#Exibe erro
def erro(variavel):
    if(variavel!=""):
        print(convert(variavel)+"\nErro")
        sys.exit()
    else:
        print("0 \nErro")
        sys.exit()

def decode8B10B(sinais):
    vBin = decodeNRZI(sinais)
    #print(vBin)
    rd = "-1"    
    saida8B10B = ""
    cont = 0
    if(len(vBin)<10):
        print("São necessarios pelo menos 10bits para completar a operação")
        sys.exit()
    while(cont<len(vBin)):
        bits = ""
        contBits = 0
        while(contBits<10):
            bits+=vBin[cont]
            cont+=1
            contBits+=1
        #print(bits)
        saida8B10B+=tabela8B10B(bits, rd)
        if(rd=="-1"):
            rd="+1"
        else:
            rd="-1"   
    return(saida8B10B)
    


def tabela8B10B(bits, rd):
    v34 = bits[6:10]
    v56 = bits[0:6]
    #print("."+v56+".")
    saida = ""

    #tabela 3b4b
    if((v34=="1011" and rd=="-1")or(v34=="0100" and rd=="+1")):
        saida="000"     #0
    elif(v34=="1001"):
        saida="001"     #1
    elif(v34=="0101"):
        saida="010"     #2
    elif((v34=="1100" and rd=="-1")or(v34=="0011" and rd=="+1")):
        saida="011"     #3
    elif((v34=="1101" and rd=="-1")or(v34=="0010" and rd=="+1")):
        saida="100"     #4
    elif(v34=="1010"):
        saida="101"     #5
    elif(v34=="0110"):
        saida="110"     #6
    elif(v34=="1000" and rd=="+1"):
        if(v56=="110100" or v56=="101100" or v56=="011100"):
            saida="111"
        else:
            erro(saida)
    elif(v34=="0111" and rd=="-1"):
        if(v56=="100011" or v56=="010011"or v56=="001011"):
            saida="111"
        else:
            erro(saida)
    elif((v34=="0001" and rd=="+1") or (v34=="1110" and rd=="-1") and (v56!="110100" and v56!="101100" and v56!="011100" and v56!="100011" and v56!="010011" and v56!="001011")):
        saida="111"
    else:
        erro(saida)

    #tabela 5b6b
    if((v56=="100111" and rd=="-1") or (v56=="011000" and rd=="+1")):
        saida+="00000"   #0
    elif((v56=="011101" and rd=="-1") or (v56=="100010" and rd=="+1")):
        saida+="00001"   #1
    elif((v56=="101101" and rd=="-1") or (v56=="010010" and rd=="+1")):
        saida+="00010"   #2
    elif(v56=="110001"):
        saida+="00011"   #3
    elif((v56=="110101" and rd=="-1") or (v56=="001010" and rd=="+1")):
        saida+="00100"   #4
    elif(v56=="101001"):
        saida+="00101"   #5
    elif(v56=="011001"):
        saida+="00110"   #6
    elif((v56=="111000" and rd=="-1") or (v56=="000111" and rd=="+1")):
        saida+="00111"   #7
    elif((v56=="111001" and rd=="-1") or (v56=="000110" and rd=="+1")):
        saida+="01000"   #8
    elif(v56=="100101"):
        saida+="01001"   #9
    elif(v56=="010101"):
        saida+="01010"   #10
    elif(v56=="110100"):
        saida+="01011"   #11
    elif(v56=="001101"):
        saida+="01100"   #12
    elif(v56=="101100"):
        saida+="01101"   #13
    elif(v56=="011100"):
        saida+="01110"   #14
    elif((v56=="010111" and rd=="-1") or (v56=="101000" and rd=="+1")):
        saida+="01111"   #15
    elif((v56=="011011" and rd=="-1") or (v56=="100100" and rd=="+1")):
        saida+="10000"   #16
    elif(v56=="100011"):
        saida+="10001"   #17
    elif(v56=="010011"):
        saida+="10010"   #18
    elif(v56=="110010"):
        saida+="10011"   #19
    elif(v56=="001011"):
        saida+="10100"   #20
    elif(v56=="101010"):
        saida+="10101"   #21
    elif(v56=="011010"):
        saida+="10110"   #22
    elif((v56=="111010" and rd=="-1") or (v56=="000101" and rd=="+1")):
        saida+="10111"   #23
    elif((v56=="110011" and rd=="-1") or (v56=="001100" and rd=="+1")):
        saida+="11000"   #24
    elif(v56=="100110"):
        saida+="11001"   #25
    elif(v56=="010110"):
        saida+="11010"   #26
    elif((v56=="110110" and rd=="-1") or (v56=="001001" and rd=="+1")):
        saida+="11011"   #27
    elif(v56=="001110"):
        saida+="11100"   #28
    elif((v56=="101110" and rd=="-1") or (v56=="010001" and rd=="+1")):
        saida+="11101"   #29
    elif((v56=="011110" and rd=="-1") or (v56=="100001" and rd=="+1")):
        saida+="11110"   #30
    elif((v56=="101011" and rd=="-1") or (v56=="010100" and rd=="+1")):
        saida+="11111"   #31
    else:
        erro(saida)

    return saida


#Variaveis usadas
tecnica = ""
sinais  = ""


#Verifica os argumentos passados
if(len(sys.argv)==3):
    tecnica = sys.argv[1]
    sinais  = sys.argv[2]
    for n in sinais:
        if(n=="-" or n=="0" or n=="+"):
            pass
        else:
            print("'"+ n + "' nao e um sinal valido")
            sys.exit()
else:
    print("Erro: Vc deve digitar dois argumentos <tecnica codificacao> <valor hexa>")
    sys.exit()

if(tecnica=="nrzi"):
    print(convert(decodeNRZI(sinais)))
elif(tecnica=="manch"):
    print(convert(decodeMANCH(sinais)))
elif(tecnica=="mlt3"):
    print(convert(decodeMLT3(sinais)))
elif(tecnica=="8b10b"):
    print(convert(decode8B10B(sinais)))
else:
    print("Erro: Tecnica invalida")
    sys.exit()


#decodeNRZI(sinais)
#decodeMANCH(sinais)
#decodeMLT3(sinais)
#decodeT8B10B(sinais)
