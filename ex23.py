info_pessoa = {
    "nome": input("Digite o Nome: "),
    "idade": int(input("Digite a Idade: ")),
    "cpf": int(input("Digite o CPF: ")),
}

lista_pessoa = input("Informe o que deseja acessar (nome, idade, cpf): ")

print(info_pessoa[lista_pessoa])
