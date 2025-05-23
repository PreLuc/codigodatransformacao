from sistema_tarefas.tarefa import adicionar_tarefa, listar_tarefas, marcar_concluida, remover_tarefa
from sistema_tarefas.arquivo import carregar_tarefas, salvar_tarefas

def menu():
    print("\n==== Sistema de Controle de carros ====")
    print("1. Adicionar carro")
    print("2. Listar carros")
    print("3. Marcar como vendido")
    print("4. carro quebrado")
    print("5. Sair")

def main():
    tarefas = carregar_tarefas()

    while True:
        menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            descricao = input("Digite a descrição do carro: ")
            adicionar_tarefa(tarefas, descricao)
        elif escolha == '2':
            listar_tarefas(tarefas)
        elif escolha == '3':
            id_tarefa = int(input("Digite o ID do carro a marcar: "))
            marcar_concluida(tarefas, id_tarefa)
        elif escolha == '4':
            id_tarefa = int(input("Digite o ID do carro quebrado: "))
            remover_tarefa(tarefas, id_tarefa)
        elif escolha == '5':
            salvar_tarefas(tarefas)
            ("vas.")
        elif escolha =='6':
             id_tarefa=int(input('digite o ID do carro vermelho'))
             adicionar_tarefa(tarefas,descricao)
        break
    else:
       print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    main()
