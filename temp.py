printNaTela = 111
sumValores = 222
subValores= 333
divValores = 444
multValores = 555
endComando = 999 



CodigoInteiro = []

def interpret(codigo):
    
    functions = []
    
    palavras = codigo.split()
    
    for palavra in palavras:
        if palavra.startswith('vejasocagatronco(') and codigo.endswith(')'):
            functions.append(0)
            
        elif palavra.startswith('falaComigoLudmillo(') and codigo.endswith(')'):
            functions.append(1)
            
        elif palavra.startswith('eaeTilapio(') and codigo.endswith(')'):
            functions.append(2)
            
        elif palavra.startswith('vocePodeFazerIssoSeborreio(') and codigo.endswith(')'):
            functions.append(3)
            
        elif palavra.startswith('calmaAeCalabreso(') and codigo.endswith(')'):
            functions.append(4)
            
        # elif palavra.startswith('for(') and codigo.endswith(')'):
        #     functions.append(5)
        else:
            print("Erro: Comando desconhecido.")
            
        functionsPy(functions)
            
def functionsPy(functions):
    
    for function in functions:
        if function == 0:
            vejaSoCagaTronco()
            
        elif function == 1:
            falaComigoLudmillo()
            
        elif function == 2:
            eaeTilapio()
            
        elif function == 3:
            vocePodeFazerIssoSeborreio()
            
        elif function == 4:
            calmaAeCalabreso()
            
        elif function == 5:
            vouTerQueRepetirIvetoSangalo()
            
        else:
            print("função não existente")
  
        
def vejaSoCagaTronco():
    Converter('vejasocagatronco', printNaTela)
def falaComigoLudmillo():
    Converter("falaComigoLudmillo", sumValores)
def eaeTilapio():
    Converter("eaeTilapio", subValores)
def vocePodeFazerIssoSeborreio():
    Converter("vocePodeFazerIssoSeborreio", divValores)
def calmaAeCalabreso():
    Converter("calmaAeCalabreso", multValores)
# def vouTerQueRepetirIvetoSangalo():
#     Converter("vouTerQueRepetirIvetoSangalo")
    
def Converter(func, acao):
    content = codigo.split(f'{func}(')[1].rsplit(')', 1)[0].strip('"')
    conversao = [ord(char) for char in content]
    conversao.insert(0, acao )
    conversao.append(endComando)
            
    print(conversao)
            
codigo = 'eaeTilapio("banana")'
interpret(codigo)

    