import sys
import string
import binascii

sinais = "---+++----+--+++"
#sinais = "+++000-0"
tecnica = "manch"

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

    print(convert(saidaNRZI))


def decodeMANCH(sinais):
    saidaMANCH = ""
    cont = 0
    if(len(sinais) % 2 == 0 and sinais!=""):
        while(cont <= len(sinais)-2):
            if(sinais[cont]==sinais[cont+1]):
                if(saidaMANCH!=""):
                    print(convert(saidaMANCH)+"\nErro")
                    sys.exit()
                else:
                    print("0 \nErro")
                    sys.exit()
            elif(sinais[cont]=="-"):
                saidaMANCH+="1"
            else:
                saidaMANCH+="0"
            cont+=2

        print(convert(saidaMANCH))
    else:
        print("Erro, numero de sinais incorreto!")


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
                    print("Erro")
                    sys.exit()
        elif(n=="+"):
            if(us=="+"):
                saidaMLT3+="0"
            else:
                if(us=="0" and sa=="-"):
                    saidaMLT3+="1"
                    us="+"
                    sa="0"
                else:
                    print("Erro")
                    sys.exit()
        elif(n=="-"):
            if(us=="-"):
                saidaMLT3+="0"
            else:
                if(us=="0" and sa=="+"):
                    saidaMLT3+="1"
                    us="-"
                    sa="0"
                else:
                    print("Erro")
                    sys.exit()
        else:
            print("sinal invalido")
            sys.exit()
    print(convert(saidaMLT3))


#decodeNRZI(sinais)
#decodeMANCH(sinais)
decodeMLT3(sinais)
#decodeT8B10B(sinais)
