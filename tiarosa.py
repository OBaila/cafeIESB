#Cardapio do Café
casa = {
    "1": ("FORTE", 5.00),
    "2": ("Legero", 7.00),
    "3": ("Ristretto", 3.00),
    "4": ("Café Gelado", 8.00),
    "5": ("Pastel de Nata", 2.80),
    "6": ("Menu: Café + lanche", 7.50)
}

orden = []
total = 0
proximo_codigo = 6  

while True:
    print("CAFE TIA ROSA")
    print("Cardápio:")
    for codigo, (item, preco) in casa.items():
        print(f"{codigo} - {item:<14} | R${preco:.2f}")
    print("0 - Finalizar pedido")

  #Sessão 1 para o staff adiconar produtos ao sistema, descrição e preço.
    print("9 - Staff: Adicionar item ao cardápio")

    escolha = input("Escolha o item: ")
    if escolha == "0":
        break
    elif escolha == "9":
        nome = input("Nome do produto: ")
        try:
            preco = float(input("Preço do produto: "))
            casa[str(proximo_codigo)] = (nome, preco)
            print(f" Item '{nome}' adicionado com sucesso como código {proximo_codigo}.")
            proximo_codigo += 1
        except ValueError:
            print("Preço inválido. Tente novamente.")
  #Sessão 1 para o staff adiconar produtos ao sistema, descrição e preço.

  #Sessão 2 para o staff fazer o pedido dos clientes. 
    elif escolha in casa:
        item, preco = casa[escolha]
        orden.append(item)
        total += preco
        print(f"{item} adicionado ao pedido.")
    else:
        print("Opção inválida.")
nome = input("\nDigite seu nome para retrirar pedido: ")
print("\nPedido finalizado:")
for item in orden:
    print(f"- {item}")
print(f"Total: R${total:.2f}")
  #Sessão 2 para o staff fazer o pedido dos clientes.

  #Sessão 3 para o staff pedir dados dos clientes para futuras promoções.
if input("Deseja receber promoções por SMS? (sim/não): ").lower() == "sim":
    nome = input("Digite seu nome: ")
    telefone = input("Digite seu telefone: ")
    print(f"Obrigado, {nome}! Enviaremos promoções para {telefone}.")
print(f"{nome} seu pedido será entregue em breve")
    #Sessão 3 para o staff pedir dados dos clientes para futuras promoções.
