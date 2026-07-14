while True: 
    usuario_validos = ('admin', 'Admin')
    senha = '1234'
    input_usuario = input('Digite o nome do usuario: ')
    input_senha = input(('Digite a senha: '))
    if input_usuario in usuario_validos and input_senha == senha:
        print('Acesso permitido, voce entrou na calculadora')
        while True:
            print('Escolha uma das operações abaixo: ' \
            '1-adicao  ' \
                '2-subtracao  ' \
                    '3-multiplicacao  ' \
                        '4-divisao  ' \
                            '5-sair da calculadora  ')
            operacao = input('Digite o numero da operação escolhida: ')
            if operacao == '1':
                numero1 = int(input('Digite o primeiro numero da conta: '))
                numero2 = int(input('Digite o segundo numero da conta: '))
                print(f'O resultado da adicao e {numero1 + numero2}')
            elif operacao == '2':
                numero1 = int(input('Digite o primeiro numero da conta: '))
                numero2 = int(input('Digite o segundo numero da conta: '))
                print(f'O resultado da subtracao e {numero1 - numero2}')
            elif operacao == '3':
                numero1 = int(input('Digite o primeiro numero da conta: '))
                numero2 = int(input('Digite o segundo numero da conta: '))
                print(f'O resultado da multiplicacao e {numero1 * numero2}')
            elif operacao == '4':
                numero1 = int(input('Digite o primeiro numero da conta: '))
                numero2 = int(input('Digite o segundo numero da conta: '))
                if numero2 == 0:
                    print('Nao e possivel dividir por zero. Tente outro numero.')
                else:
                    print(f'O resultado da divisao e {numero1 / numero2}')
            elif operacao == '5':
                print('saindo...')
                break
        break
    else:
        print('Acesso negado, senha ou usuario incorreto, tente novamente')