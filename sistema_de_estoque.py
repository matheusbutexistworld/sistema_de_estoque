#Sistema de Controle de Estoque
#Modelagem de Dados com Dicionário e Lista

#Dicionário - A estrutura é composta por campos (Chaves e valores) detalhando o produto. Ex:Nome, Quantidade, Preço
produto1 = {
    "nome": "Arroz",
    "quantidade": 0,
    "preco": 0.00
}
produto2 = {
    "nome": "Feijão",
    "quantidade": 0,
    "preco": 0.00
}
produto3 = {
    "nome": "Óleo",
    "quantidade": 0,
    "preco": 0.00
}
#Utilizei a variável "produto1, produto2 e o produto3" para a visualização dos dicionários na aplicação.

#Lista de Dicionários (Produtos) - Permite percorrer, buscar e atualizar os produtos.
controle_estoque = [produto1, produto2, produto3]
#A variável controle_estoque foi escolhida para ter a visão de "Organização" e "Gerenciamento" dos itens dentro do sistema.

while True: #Define o laço "while", que é um comando que mantém o menu ativo, caso o usuário não escolha a opção "4" para sair.
    print("\n------ SISTEMA DE CONTROLE DE ESTOQUE ------")
    print("1. Visualizar o Estoque Atual")
    print("2. Adicionar Produto")
    print("3. Registrar Saída de Produto")
    print("4. Sair do Sistema")
    #A variável "escolha_do_usuario" foi definida para receber a entrada do usuário e direcioná-lo para a operação desejada.
    escolha_do_usuario = input("Digite sua opção: ")
    #Opção 1: Visualizar Estoque (O comando "for" foi usado para percorrer a lista "controle_estoque" e imprimir os produtos.)
    if escolha_do_usuario == "1":
        print("Visualizando o Estoque Atual")
        for produtos in controle_estoque:
            print(f"{produtos['nome']} - {produtos['quantidade']}, R${produtos['preco']}")
    #Opção 2: Adicionar Produto, o for foi usado para percorrer a lista "controle_estoque", e validar se o produto já existe, assim adicionando a quantidade informada pelo usuário.
    elif escolha_do_usuario == "2":
        adicionar_produto = input("Digite o nome do produto que deseja adicionar: ")
        inserir_quantidade = int(input("Digite a quantidade que deseja adicionar: "))
        for produtos in controle_estoque:
            if produtos["nome"] == adicionar_produto:
                produtos["quantidade"] += inserir_quantidade
                print(f"O Produto {adicionar_produto} foi adicionado com sucesso!")
                break
        else:
            print(f"O Produto {adicionar_produto} não foi encontrado no sistema.") # Caso o produto não seja encontrado na lista, o sistema informará ao usuário.
    #Opção 3: Registrar Saída de Produto, aqui existem duas validações, se o produto existe e se a quantidade é suficiente.    
    elif escolha_do_usuario == "3":
       retirada_produto = str(input("Digite o nome do produto que deseja remover: "))
       for produtos in controle_estoque:
            if produtos["nome"] == retirada_produto:
               retirada_quantidade = int(input("Digite a quantidade que deseja remover: "))
               if retirada_quantidade <= produtos["quantidade"]:
                    produtos["quantidade"] -= retirada_quantidade
                    print(f"O Produto {retirada_produto} teve {retirada_quantidade} quantidade removida com sucesso!")
                    break
               else:
                   print(f"A quantidade de {retirada_quantidade} está com o estoque insuficiente!")
                   break
       else:
           print(f"Produto {retirada_produto} não foi encontrado no estoque!")
#Opção 4: Sair do Sistema, o comando "break" foi usado para encerrar o programa.
    elif escolha_do_usuario == "4":
        print("Saindo do Sistema")
        break
    else:
        print(f"A operação {escolha_do_usuario} não existe no sistema.")