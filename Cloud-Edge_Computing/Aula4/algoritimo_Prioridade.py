import copy

processos = [
    {'id': 'P1', 'chegada': 2, 'execucao': 6, 'prioridade': 5, 'deadline': 8},
    {'id': 'P2', 'chegada': 4, 'execucao': 2, 'prioridade': 1, 'deadline': 12},
    {'id': 'P3', 'chegada': 0, 'execucao': 3, 'prioridade': 5, 'deadline': 6},
    {'id': 'P4', 'chegada': 4, 'execucao': 4, 'prioridade': 10, 'deadline': 8},
]

tempo_atual = 0
ordem_execucao = []
waiting_times = []
tat_times = []
finalizados = []
fila = copy.deepcopy(processos)

print("\n==============================")
print("RESULTADO — ALGORITMO: PRIORIDADE")
print("==============================")

while len(finalizados) < len(processos):
    disponiveis = [p for p in fila if p['chegada'] <= tempo_atual]
    if not disponiveis:
        tempo_atual += 1
        continue
    processo = max(disponiveis, key=lambda p: p['prioridade'])
    fila.remove(processo)

    inicio = tempo_atual
    fim = tempo_atual + processo['execucao']
    waiting = inicio - processo['chegada']
    tat = fim - processo['chegada']
    tempo_atual = fim

    ordem_execucao.append(processo['id'])
    waiting_times.append(waiting)
    tat_times.append(tat)
    finalizados.append(processo)

    print(f"Processo: {processo['id']} | Conclusão: {fim}ms | Waiting Time: {waiting}ms | TAT: {tat}ms | Deadline: {processo['deadline']}ms | Cumpriu Deadline: {'SIM' if fim <= processo['deadline'] else 'NÃO'}")

print("\nMédias:")
print(f"Average Waiting Time: {sum(waiting_times)/len(waiting_times):.2f}ms")
print(f"Average Turn Around Time: {sum(tat_times)/len(tat_times):.2f}ms")
