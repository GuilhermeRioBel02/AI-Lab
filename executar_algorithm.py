from genetic_algorithm import GeneticAlgorithm

# Definir dimensões da chapa metálica
LARGURA_CHAPA = 500
ALTURA_CHAPA = 300

# Definir os recortes disponíveis (largura, altura)
RECORTES_DISPONIVEIS = [
    {"largura": 100, "altura": 50, "tipo": "retangular", "x": 0, "y": 0},
    {"largura": 200, "altura": 100, "tipo": "retangular", "x": 0, "y": 50},
    {"largura": 50, "altura": 50, "tipo": "retangular", "x": 100, "y": 0},
    {"largura": 150, "altura": 200, "tipo": "retangular", "x": 200, "y": 0},
]
# Configuração do Algoritmo Genético
TAM_POPULACAO = 10   # Número de indivíduos na população
NUM_GERACOES = 20    # Número de gerações

# Criar instância do Algoritmo Genético
ga = GeneticAlgorithm(TAM_POPULACAO, RECORTES_DISPONIVEIS, LARGURA_CHAPA, ALTURA_CHAPA, NUM_GERACOES)

# Executar otimização
melhor_solucao = ga.optimize_and_display()

# Exibir a melhor disposição encontrada
print("\nMelhor solução encontrada:")
for i, recorte in enumerate(melhor_solucao):
    print(f"Recorte {i+1}: x={recorte['x']}, y={recorte['y']}, Rotação={recorte['rotacao']}°")
