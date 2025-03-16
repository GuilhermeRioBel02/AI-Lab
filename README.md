# Otimizador de Corte CNC com Algoritmo Genético

## Descrição
Este projeto implementa um Algoritmo Genético para otimizar o corte de chapas, melhorando o aproveitamento de material e reduzindo desperdícios. A solução busca encontrar a melhor disposição de recortes dentro de uma chapa de dimensões definidas, utilizando operações genéticas como seleção, crossover e mutação.

## Funcionalidades
- Algoritmo Genético para otimização do corte.
- Visualização do layout inicial e final dos recortes.
- Parâmetros configuráveis como tamanho da população, dimensões da chapa e número de gerações.
- Impressão da melhor solução encontrada.

## Estrutura do Projeto
```
/otimizador_corte_cnc
├── common/
│   ├── layout_display.py  # Mixin para exibir layouts
├── genetic_algorithm.py    # Implementação do Algoritmo Genético
├── executar_algorithm.py   # Arquivo principal para execução
├── README.md               # Documentação do projeto
```

## Como Executar
1. Clone o repositório:
   ```sh
   git clone https://github.com/seu-usuario/otimizador_corte_cnc.git
   ```
2. Acesse a pasta do projeto:
   ```sh
   cd otimizador_corte_cnc
   ```
3. Execute o script principal:
   ```sh
   python executar_algorithm.py
   ```

## Dependências
- Python 3.x
- Biblioteca NumPy (se necessário para cálculos)
- Matplotlib (se necessário para visualização)

Para instalar as dependências:
```sh
pip install -r requirements.txt
```

## Contribuição
Sinta-se à vontade para contribuir com melhorias. Para isso:
1. Faça um fork do repositório.
2. Crie um branch para sua funcionalidade (`git checkout -b minha-funcionalidade`).
3. Faça commit das suas alterações (`git commit -m 'Adicionando nova funcionalidade'`).
4. Envie para o repositório (`git push origin minha-funcionalidade`).
5. Abra um Pull Request.

## Creditos
Projeto desenvolvido por Guilherme Pereira. Algumas partes do código foram organizadas com consulta ao ChatGPT para estruturação e otimização.

