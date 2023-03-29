quantidade_transacoes = int(input("Informe a quantidade de transações"))
total_transacoes = 0

for n_transacoes in range(1, quantidade_transacoes + 1, 1):
    transacao = float(input("Por informe a transação de numero {}".format(n_transacoes)))

    total_transacoes = total_transacoes + transacao

media = total_transacoes / quantidade_transacoes
print("Nesse dia foi gastou um total de R${}, com uma média de R${} por transação".format(total_transacoes, media))