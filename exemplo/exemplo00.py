

aluno: str = 3

if isinstance(aluno, str):
    print("Nome correto")
else:
    print("Nao e string")


def calculadora(x:int, y:int):
    try:
        if isinstance(x, int):
            if isinstance(y, int):
                soma = x+y
            else:
                print("y nao e um numero")  

        else:
            print("x nao e um numero")
        return print(f"a soma de x e y: {soma}")
    except:
        print("algo deu errado")

calculadora(10, "3")