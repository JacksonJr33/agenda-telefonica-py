agenda = {}

while True:
    print('--- Agenda Telefônica ---')
    print('1 - Adicionar Contato')
    print('2 - Edita Contato (telefone)')
    print('3 - Remover Contato')
    print('4 - Buscar Contato')
    print('5 - Listar Todos')
    print('6 - Sair')
    opcao = int(input('Selecione uma opção: '))
    if opcao == 1:
        nome = input('Digite o Nome do Contato: ')
        telefone = input('Digite o Telefone do Contato: ')
        agenda[nome] = telefone
        print('Contato Adicionado com Sucesso!')
    elif opcao == 2:
        nome = input('Digite o Nome do Contato: ')
        if nome in agenda:
            agenda[nome] = input('Digite o Novo Telefone:')
            print('Telefone Alteradocom Sucesso!')
        else:
            print('Contato Não Encontrado!')
    elif opcao == 3:
        nome = input('Digite o Nome od Contato: ')
        if nome in agenda:
            del agenda[nome]
            print('Contato Removido com Sucesso!')
        else:
            print('Contato Não Encontrado!')
    elif opcao == 4:
        nome = input('Digite o Nome do Contato: ')
        if nome in agenda:
            print(f'Telefone de {nome}: {agenda[nome]}')
        else:
            print('Contato Não Encontrado!')
    elif opcao == 5:
        print('--- LISTA DE CONTATOS ---')
        for nome in agenda:
            print(f'Nome: {nome} - Telefone: {agenda[nome]}')
    elif opcao == 6:
        break
    else:
        print('Opção Inválida')