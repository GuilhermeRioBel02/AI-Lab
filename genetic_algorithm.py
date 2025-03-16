from common.layout_display import LayoutDisplayMixin
import random

class GeneticAlgorithm(LayoutDisplayMixin):
    def __init__(self, TAM_POP, recortes_disponiveis, sheet_width, sheet_height, numero_geracoes=100):
        print("Algoritmo Genético para Otimização do Corte de Chapa. Executado por Guilherme Pereira.")
        self.TAM_POP = TAM_POP
        self.initial_layout = [
            {**recorte, 'rotacao': recorte.get('rotacao', 0)} for recorte in recortes_disponiveis
        ]  # Garante que todos os recortes tenham a chave 'rotacao'
        
        self.sheet_width = sheet_width
        self.sheet_height = sheet_height
        self.POP = []
        self.POP_AUX = []
        self.aptidao = []
        self.numero_geracoes = numero_geracoes
        self.initialize_population()
        self.melhor_aptidoes = []
        self.optimized_layout = None  # Layout otimizado será definido depois da execução do algoritmo

    def initialize_population(self):
        """Inicializa a população de indivíduos aleatoriamente, incluindo rotação."""
        self.POP = []
        for _ in range(self.TAM_POP):
            individuo = []
            for recorte in self.initial_layout:
                novo_recorte = recorte.copy()
                novo_recorte['rotacao'] = random.choice([0, 90])  # Rotação de 0° ou 90°
                individuo.append(novo_recorte)
            self.POP.append(individuo)

    def evaluate(self):
        """Avalia a aptidão de cada indivíduo com base na ocupação da chapa."""
        self.aptidao = [self.calcular_aptidao(ind) for ind in self.POP]

    def calcular_aptidao(self, individuo):
        """Calcula a aptidão de um indivíduo considerando rotação e ocupação do espaço."""
        area_ocupada = sum(
            (recorte['y'] if recorte['rotacao'] == 90 else recorte['x']) * 
            (recorte['x'] if recorte['rotacao'] == 90 else recorte['y'])
            for recorte in individuo
        )
        return -abs(self.sheet_width * self.sheet_height - area_ocupada)  # Quanto menor a diferença, melhor

    def genetic_operators(self):
        """Executa crossover e mutação para evoluir a população."""
        nova_populacao = []
        for _ in range(self.TAM_POP // 2):
            pai1, pai2 = random.sample(self.POP, 2)
            filho1, filho2 = self.crossover(pai1, pai2)
            nova_populacao.extend([self.mutacao(filho1), self.mutacao(filho2)])

        self.POP = nova_populacao

    def crossover(self, pai1, pai2):
        """Realiza crossover simples, combinando características dos pais."""
        ponto_corte = len(pai1) // 2
        filho1 = pai1[:ponto_corte] + pai2[ponto_corte:]
        filho2 = pai2[:ponto_corte] + pai1[ponto_corte:]
        return filho1, filho2

    def mutacao(self, individuo):
        """Aplica mutação aleatória em um recorte, alterando sua rotação."""
        if random.random() < 0.2:  # 20% de chance de mutação
            index = random.randint(0, len(individuo) - 1)
            individuo[index]['rotacao'] = 0 if individuo[index]['rotacao'] == 90 else 90
        return individuo

    def run(self):
        """Executa o algoritmo genético por N gerações."""
        for _ in range(self.numero_geracoes):
            self.evaluate()
            self.genetic_operators()

        melhor_indice = self.aptidao.index(max(self.aptidao))
        self.optimized_layout = self.POP[melhor_indice]
        return self.optimized_layout

    def optimize_and_display(self):
        """
        Exibe o layout inicial, executa a otimização e exibe o layout otimizado.
        """
        self.display_layout(self.initial_layout, title="Layout Inicial - Algoritmo Genético")
        
        self.optimized_layout = self.run()
        
        self.display_layout(self.optimized_layout, title="Layout Otimizado - Algortimo Genético")
        return self.optimized_layout