TOTAL_ENTREVISTADOS =10

qtd_excelente = 0
qtd_bom = 0
qtd_ruim = 0

print(f"=== INÍCIO DA PESQUISA DE ATENDIMENTO ({TOTAL_ENTREVISTADOS} ENTREVISTADOS) ===\n")

for i in range(1, TOTAL_ENTREVISTADOS + 1):
    print(f"--- Entrevistado {i} de {TOTAL_ENTREVISTADOS} ---")
    
    nome = input("Digite o nome: ").strip()
    
    while True:
        try:
            idade = int(input("Digite a idade: "))
            if idade > 0:
                break
            print("Por favor, digite uma idade válida (maior que 0).")
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros para a idade.")

    print("Opinião sobre o atendimento:")
    print("  1: EXCELENTE")
    print("  2: BOM")
    print("  3: RUIM")

    while True:
        opiniao = input("Digite sua opção (1, 2 ou 3): ").strip()
        
        # Estrutura de decisão para contabilizar a resposta
        if opiniao == "1":
            qtd_excelente += 1
            break
        elif opiniao == "2":
            qtd_bom += 1
            break
        elif opiniao == "3":
            qtd_ruim += 1
            break
        else:
            print("Opção inválida! Escolha apenas 1, 2 ou 3.")
            
    print() 

print("=" * 45)
print("           RESULTADO DA PESQUISA            ")
print("=" * 45)
print(f"a) Quantidade de respostas 'EXCELENTE': {qtd_excelente}")
print(f"b) Quantidade de respostas 'RUIM'     : {qtd_ruim}")
print(f"   (Informativo) Respostas 'BOM'      : {qtd_bom}")
print("=" * 45)