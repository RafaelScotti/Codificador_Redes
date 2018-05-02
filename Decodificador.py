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
    
    if((len(sinais)%10)!=0):
        return "Erro! numero de sinais invalido"
    #print(convertBin)
    rd = "-1"    
    saida8B10B = ""
    cont = 0
    while(cont<len(vBin)):
        bits = ""
        contBits = 0
        while(contBits<8):
            bits+=sinais[cont]
            cont+=1
            contBits+=1
        #print(bits)
        saida8B10B+=tabela8B10B(bits, rd)
        if(rd=="-1"):
            rd="+1"
        else:
            rd="-1"    
    


def tabela8B10B(bitsSinais, rd):
    v34 = bitsSinais[6:10]
    v56 = bitsSinais[0:6]
    #print("."+v56+".")
    saida = ""

    if((v56=="100111" and rd=="-1") or (v56=="011000" and rd=="+1")):
        saida="00000"   #0
    elif((v56=="011101" and rd=="-1") or (v56=="100010" and rd=="+1")):
        saida="00001"   #1
    elif((v56=="101101" and rd=="-1") or (v56=="010010" and rd=="+1")):
        saida="00010"   #2
    elif(v56=="110001"):
        saida="00011"   #3
    elif((v56=="110101" and rd=="-1") or (v56=="001010" and rd=="+1")):
        saida="00100"   #4
    elif(v56=="101001"):
        saida="00101"   #5
    elif(v56=="011001"):
        saida="00110"   #6
    elif((v56=="111000" and rd=="-1") or (v56=="000111" and rd=="+1")):
        saida="00111"   #7
    elif((v56=="111001" and rd=="-1") or (v56=="000110" and rd=="+1")):
        saida="01000"   #8
    elif(v56=="100101"):
        saida="01001"   #9
    elif(v56=="010101"):
        saida="01010"   #10
    elif(v56=="110100"):
        saida="01011"   #11
    elif(v56=="001101"):
        saida="01100"   #12
    elif(v56=="101100"):
        saida="01101"   #13
    elif(v56=="011100"):
        saida="01110"   #14
    elif((v56=="010111" and rd=="-1") or (v56=="101000" and rd=="+1")):
        saida="01111"   #15
    


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
