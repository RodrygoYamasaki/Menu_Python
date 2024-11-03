# Armazenamento de dados em listas
trens_operacionais = ["Trem 1", "Trem 2", "Trem 3"]
trens_manutencao = ["Trem 4"]
anomalias = [
    {"trem": "Trem 12", "data": "29/10/2024", "descricao": "Superaquecimento detectado"},
    {"trem": "Trem 34", "data": "29/10/2024", "descricao": "Desvio de pressão nos freios"}
]

def main_menu():
    print("┌────────────────────────────────────────┐")
    print("│           SISTEMA DE OPERAÇÕES         │")
    print("├────────────────────────────────────────┤")
    print("│              MENU PRINCIPAL            │")
    print("├────────────────────────────────────────┤")
    print("│ [1] Iniciar Monitoramento Contínuo     │")
    print("│ [2] Exibir Status em Tempo Real        │")
    print("│ [3] Análise de Dados com IA            │")
    print("│ [4] Relatório de Anomalias             │")
    print("│ [5] Encerrar Sistema                   │")
    print("└────────────────────────────────────────┘")

def obter_opcao_usuario():
    while True:
        try:
            escolha = int(input("Selecione uma opção: "))
            if escolha in range(1, 6):
                return escolha
            else:
                print("Opção inválida. Escolha entre 1 e 5.")
        except ValueError:
            print("Entrada inválida. Insira um número.")

def iniciar_monitoramento(trens, infraestrutura):
    print("\nIniciando monitoramento contínuo de trens e infraestruturas...")
    print(f"• Trens monitorados: {', '.join(trens)}")
    print(f"• Infraestruturas críticas: {infraestrutura} monitoradas")
    print("Monitoramento contínuo ativo! Todos os dados estão sendo registrados em tempo real.\n")
    return True  # Retorna True para indicar que o monitoramento foi iniciado

def exibir_status(trens_operacionais, trens_manutencao):
    print("\nStatus em Tempo Real de Todos os Sistemas:")
    print(f"• Trens operacionais: {len(trens_operacionais)}")
    print(f"• Trens em manutenção: {len(trens_manutencao)}")
    print("• Infraestruturas críticas: 5 monitoradas")
    print("• Última verificação de trilhos: 5 minutos atrás")
    print("• Temperatura média dos motores: 70°C")
    print("Todos os sistemas estão funcionando dentro dos parâmetros normais.\n")
    return len(trens_operacionais), len(trens_manutencao)  # Retorna informações para possível uso posterior

def analise_ia():
    print("\nAnálise de Dados com Inteligência Artificial:")
    print("• IA analisando padrões de operação e identificando anomalias...")
    print("• Algoritmo preditivo em execução para prever falhas potenciais...")
    print("• Detecção de padrões incomuns em velocidade e temperatura dos trens...")
    print("Análise concluída. Nenhuma falha prevista para as próximas 24 horas.\n")
    return "Nenhuma falha prevista"  # Retorno fictício de análise

def relatorio_anomalias(anomalias):
    print("\nRelatório de Anomalias Detectadas:")
    if anomalias:
        for anomalia in anomalias:
            print(f"• Trem: {anomalia['trem']}, Data: {anomalia['data']}, Descrição: {anomalia['descricao']}")
        print(f"• Total de anomalias no último mês: {len(anomalias)}")
    else:
        print("Nenhuma anomalia registrada.")
    print("Relatório completo disponível para download e análise detalhada.\n")

def encerrar_sistema():
    print("\nEncerrando sistema. Todas as operações de monitoramento serão pausadas.")
    print("Os dados coletados até agora foram salvos para futuras análises.")
    print("Sistema encerrado com sucesso. Até logo!")
    return False  # Retorna False para encerrar o loop principal

# Execução do Menu com Validação e Estruturas de Controle
executando = True
while executando:
    main_menu()
    escolha = obter_opcao_usuario()

    if escolha == 1:
        iniciar_monitoramento(trens_operacionais, infraestrutura = 5)
    elif escolha == 2:
        exibir_status(trens_operacionais, trens_manutencao)
    elif escolha == 3:
        analise_ia()
    elif escolha == 4:
        relatorio_anomalias(anomalias)
    elif escolha == 5:
        executando = encerrar_sistema()
