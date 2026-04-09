def adicionar_tarefa(tarefa):
    # 'a' abre o arquivo para adicionar (append) sem apagar o que já existe
    with open("tarefas.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(tarefa + "\n")
    print("Tarefa salva com sucesso!")

def listar_tarefas():
    try:
        with open("tarefas.txt", "r", encoding="utf-8") as arquivo:
            print("\n--- Lista de Tarefas ---")
            for i, linha in enumerate(arquivo, 1):
                print(f"{i}. {linha.strip()}")
    except FileNotFoundError:
        print("Nenhuma tarefa cadastrada ainda.")

while True:
    print("\n1. Adicionar Tarefa | 2. Listar Tarefas | 3. Sair")
    escolha = input("O que deseja fazer? ")

    if escolha == '1':
        t = input("Descreva a tarefa: ")
        adicionar_tarefa(t)
    elif escolha == '2':
        listar_tarefas()
    elif escolha == '3':
        break
    else:
        print("Opção inválida.")
