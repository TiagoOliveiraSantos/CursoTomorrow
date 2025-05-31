processos = [
    {'id': 'P1', 'chegada': 2, 'execucao': 6, 'prioridade': 5, 'deadline': 8},
    {'id': 'P2', 'chegada': 4, 'execucao': 2, 'prioridade': 1, 'deadline': 12},
    {'id': 'P3', 'chegada': 0, 'execucao': 3, 'prioridade': 5, 'deadline': 6},
    {'id': 'P4', 'chegada': 4, 'execucao': 4, 'prioridade': 10, 'deadline': 8},
]

processos.sort(key=lambda p: p['chegada'])  # FIFO ordena por chegada
tempo_atual = 0
ordem_execucao = []
waiting_times = []
tat_times = []

print("==============================")
print("RESULTADO — ALGORITMO: FIFO")
print("==============================")
print("Ordem de execução:")

for p in processos:
    if tempo_atual < p['chegada']:
        tempo_atual = p['chegada']
    inicio = tempo_atual
    fim = tempo_atual + p['execucao']
    waiting = inicio - p['chegada']
    tat = fim - p['chegada']

    ordem_execucao.append(p['id'])
    waiting_times.append(waiting)
    tat_times.append(tat)
    tempo_atual = fim

    print(f"Processo: {p['id']} | Conclusão: {fim}ms | Waiting Time: {waiting}ms | TAT: {tat}ms | Deadline: {p['deadline']}ms | Cumpriu Deadline: {'SIM' if fim <= p['deadline'] else 'NÃO'}")

print("\nMédias:")
print(f"Average Waiting Time: {sum(waiting_times)/len(waiting_times):.2f}ms")
print(f"Average Turn Around Time: {sum(tat_times)/len(tat_times):.2f}ms")
