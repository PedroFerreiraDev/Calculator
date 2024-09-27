print("Seja Bem-Vindo à Calculadora!\n")
op = input("Selecione a operação que deseja realizar: \n[1] Soma \n[2] Subtração \n[3] Multiplicação \n[4] Divisão\n")

if op == '1':
    n1 = float(input("Digite um número: "))
    n2 = float(input("Digite outro número: "))
    resultado = n1 + n2
    print(f"{n1} + {n2} = {resultado}")

elif op == '2':
    n1 = float(input("Digite um número: "))
    n2 = float(input("Digite outro número: "))
    resultado = n1 - n2
    print(f"{n1} - {n2} = {resultado}")

elif op == '3':
    n1 = float(input("Digite um número: "))
    n2 = float(input("Digite outro número: "))
    resultado = n1 * n2
    print(f"{n1} x {n2} = {resultado}")

elif op == '4':
    n1 = float(input("Digite o dividendo: "))
    n2 = float(input("Digite o divisor: "))
    if n2 == 0:
        print("Erro: O divisor não pode ser 0.")
    else:
        resultado = n1 / n2
        print(f"{n1} / {n2} = {resultado}")

else:
    print("Opção inválida!")
