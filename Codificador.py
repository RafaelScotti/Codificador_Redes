import sys
import string
tecnica = ""
valorHexa = ""

if(len(sys.argv)==3):
    if(sys.argv[1]=="nrzi" or sys.argv[1]=="manch" or sys.argv[1]=="mlt3" or sys.argv[1]=="8b10b"):
        tecnica = sys.argv[1]
    else:
        print("Técnica de codificacao invalida")
        sys.exit()
    valorHexa = sys.argv[2]
    if(all(c in string.hexdigits for c in valorHexa)):
        print("OK")
    else:
        print("Codigo hexadecimal invalido!")
        sys.exit()
else:
    print("Vc deve digitar dois argumentos <tecnica codificacao> <valor hexa>")
    sys.exit()


t = len(valorHexa)*4 #verifica total de bits
convertBin = (bin(int(valorHexa, 16))[2:]).zfill(t)#Converte para binario
print(convertBin)
#======DEFINIR FUNCAO NRZI======
saidaNRZI=""
lastSinal = "-"
if(tecnica=="nrzi"):
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

#=====FIM CODIFICADOR NRZI======

#=====DEFINIR FUNCAO MANCH======
saidaMANCH=""
if(tecnica=="manch"):
    for n in convertBin:
        if(n=="1"):
            saidaMANCH = saidaMANCH + "-+"
        elif(n=="0"):
            saidaMANCH = saidaMANCH + "+-"
 
print(saidaMANCH)
#=====FIM CODIFICADOR MANCH======

#=====DEFINIR FUNCAO MLT-3=======

saidaMLT3=""
ultimoSinal="0"
penultimoSinal="-1"
if(tecnica=="mlt3"):
    for n in convertBin:
        if(n=="+1"):
            if(ultimoSinal=="0"):
                if(penultimoSinal=="-1"):    
                    daMLT3 = saidaMLT3 + "+1"
                    ultimoSinal = ultimoSinal
                    ultimoSinal = "+1"
            elif(penultimoSinal=="1"):
                saidaMLT3 = saidaMLT3 + "-1"
                penultimoSinal = ultimoSinal
                ultimoSinal = "-1"
        elif(ultimoSinal=="1"):
            if(penultimoSinal=="+1"):
                saidaMLT3 = saidaMLT3+"0"
                penultimoSinal="+1"
                ultimoSinal= "0"
            elif(penultimoSinal=="-1"):
                saidaMLT3 = saidaMLT3+"0"
                penultimoSinal="-1"
                ultimoSinal= "0"
 
    else:
        saidaMLT3 = saidaMLT3 + ultimoSinal

print(saidaMLT3)
#APAGAR TUDO
#CRIA UMA VARIAVEL Q ARMAZENA O ULTIMO SINAL (QUE NAO SEJA O "N") E ALTERAR ELA DEPENDENDO
#DO VALOR LIDO NO "N"






