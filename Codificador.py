import sys
import string
tecnica = ""
valorHexa = ""

if(len(sys.argv)==3):
    tecnica = sys.argv[1]
    valorHexa = sys.argv[2]
    if(all(c in string.hexdigits for c in valorHexa)):
        print("OK")
    else:
        print("Erro: Codigo hexadecimal invalido!")
        sys.exit()
else:
    print("Erro: Vc deve digitar dois argumentos <tecnica codificacao> <valor hexa>")
    sys.exit()

t = len(valorHexa)*4 #verifica total de bits
convertBin = (bin(int(valorHexa, 16))[2:]).zfill(t)#Converte para binario
print(convertBin)

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
    print("Em desenvolvimento!")


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
