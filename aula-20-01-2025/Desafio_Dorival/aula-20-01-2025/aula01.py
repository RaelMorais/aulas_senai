import img
img.cArt().ascart()
print("Exercicios do Dorivas")
escolha = input("Escolha de atividades de 1 até 9 ou desafio ")
match escolha:
    case "1":
        num = float(input("Entre com o numero 1: "))
        num2 = float(input("Entre com o numero 2: "))

        soma = num + num2

        print(f"A soma é {soma}")
    case "2":
        ano = 2025
        ano_nasc = int(input("Qual seu ano de nascimento? "))
        nome = input("Qual o seu nome? ")
        idade = ano - ano_nasc
        print(f"Olá {nome}, voce tem {idade} anos")
    case "3":
        num_impar = int(input("Qual é o número? "))
        num_resto = num_impar % 2
        if num_resto == 0:
            print("Número par")
        else:
            print("Numero impar")
    case "4":
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
        nota3 = float(input("Nota 3: "))
        nota4 = float(input("Nota 4: "))
        nota5 = float(input("Nota 5: "))

        media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

        if (media >= 5):
            print("Aprovado", media)
        elif (media > 2.5 and media <= 5):
            print("Recuperação", media)
        else:
            print("Reprovado", media)
    case "5":
        numero = 0
        for i in range(1, 11):
            print(i)
    case "6":
        numeros = []
        while True:
            numero = int(input("Digite o número: > "))
            if numero <= 0:
                break
            numeros.append(numero)
            if numeros:
                print(numeros)
                maior_numero = max(numeros)
                print("O maior número digitado foi:", maior_numero)
            else:
                print("Nenhum número positivo foi digitado.")
    case "7":
        def reverter_string():
            reverso = ""
            str = input("> ")
            for i in str:
                reverso = i + reverso
            print(reverso)
        reverter_string()
    case "8":
        frase = input("> ")
        d = {}
        for letra in frase:
            d[letra] = d.get(letra, 0) + 1 #Procura no dicionario, caso a letra não tenha sido processada, retorna 0
            '''
            O código percorre o dicionario: {"Banana"}, processa cada letra {"b" "a" "n" "a" "n" "a"}
            ele verifica se a primeira foi processada, caso não tenha sido, retorna o valor 0 (default), que se soma mais 1, 
            caso a letra seja processada d novamente, o valor 0 será 1, ou seja, a letra A foi processada uma vez, voltou como 0, somou +1, 
            virou 1, foi processada novamente, somou +1, virou 2. 
            
            '''
        print(d)
    case "Desafio":
        print("Teste")
    case _:
        print("Número inválido")

print("teste de ignore")