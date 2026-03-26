print(" Classificação de Chamado: ")

severidade = int(input("Severidade (1, 2 ou 3): "))
horas = float(input("Horas em aberto: "))
usuarios = int(input("Quantidade de usuários afetados: "))
ambiente = input("Ambiente (producao/teste): ").lower()

if severidade == 3 and ambiente == "producao":
    prioridade = "Crítica"
    acao = "Acionar plantão imediatamente"

elif severidade == 3 or usuarios > 100:
    prioridade = "Alta"
    acao = "Encaminhar para a equipe responsável"

elif severidade == 2 or horas > 4:
    prioridade = "Média"
    acao = "Registrar e acompanhar"

else:
    prioridade = "Baixa"
    acao = "Colocar na fila de atendimento"

print("\n=== Resultado ===")
print("Prioridade:", prioridade)
print("Ação recomendada:", acao)