import subprocess

printNaTela = 333
sumValores = 444
subValores= 555
divValores = 666
multValores = 777
ifValores = 888
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
        elif palavra.startswith('vouTerQueRepetirIvetoSangalo('):
            condition = palavra.split('vouTerQueRepetirIvetoSangalo(')[1].rsplit(')', 1)[0]
            functions.append((5, condition))
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

def vouTerQueRepetirIvetoSangalo(condition):
    conversao = [ord(char) for char in condition]
    conversao.insert(0, ifValores)
    conversao.append(endComando)
    for i in conversao:
         CodigoInteiro.append(str(i))

def Converter(func, acao):
    content = codigo.split(f'{func}(')[1].split(')', 1)[0].strip('"')
    conversao = [ord(char) for char in content]
    conversao.insert(0, acao )
    conversao.append(endComando)
    for i in conversao:
         CodigoInteiro.append(str(i))

def execute_js():
    subprocess.run(['node', 'interpretador.js', *map(str, CodigoInteiro)])

with open('toninho.tt', 'r') as file:
    codigo = file.read().strip()
interpret(codigo)
execute_js()
