functions = []

def interpret(codigo):
    
    palavras = codigo.split()
    
    for palavra in palavras:
        if palavra.startswith('veja so caga tronco(') and codigo.endswith(')'):
            functions.append(0)
        if palavra.startswith('scan(') and codigo.endswith(')'):
            functions.append(1)
        if palavra.startswith('if(') and codigo.endswith(')'):
            functions.append(2)
        if palavra.startswith('elif(') and codigo.endswith(')'):
            functions.append(3)
        if palavra.startswith('else(') and codigo.endswith(')'):
            functions.append(4)
        if palavra.startswith('for(') and codigo.endswith(')'):
            functions.append(5)
        if palavra.startswith('while(') and codigo.endswith(')'):
            functions.append(6)
        else:
            print("Erro: Comando desconhecido.")
            
def functionsPy(functions):
    for function in functions:
        if function == 0:
            vejasocagatronco()
        if function == 1:
            # scan()
        if function == 2:
            # if()
        if function == 3:
            # elif()
        if function == 4:
            # else()
        if function == 5:
            # for()
        if function == 6:
            # while()
        
            


def vejasocagatronco:
    print("a")
            
        
        
        
codigo = 'print("banana") if(true)'
interpret(codigo)

for i in functions:
    print(i)