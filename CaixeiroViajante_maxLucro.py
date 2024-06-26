class Grafo:
    def __init__(self, matriz_adj, valores_vertices):
        self.matriz_adj = matriz_adj
        self.valores_vertices = valores_vertices
        self.num_vertices = len(valores_vertices)
        self.melhor_lucro = 0
        self.melhor_rota = []

    def dfs(self, vertice_atual, custo_atual, lucro_atual, vertices_visitados, orçamento, inicio):
        if custo_atual > orçamento:
            return

        # Imprimindo as tuplas dos vértices visitados e o valor atual
        print(f"{vertices_visitados} - Custo: {custo_atual} - Lucro: {lucro_atual}")
        
        # Se voltar ao ponto de partida com um caminho válido
        if vertice_atual == inicio and len(vertices_visitados) > 1:
            if len(vertices_visitados) == self.num_vertices + 1:
                if lucro_atual > self.melhor_lucro:
                    self.melhor_lucro = lucro_atual
                    self.melhor_rota = vertices_visitados[:]
            return
        
        for vizinho in range(self.num_vertices):
            if self.matriz_adj[vertice_atual][vizinho] > 0 and vizinho not in vertices_visitados:
                custo_aresta = self.matriz_adj[vertice_atual][vizinho]
                vertices_visitados.append(vizinho)
                lucro_novo = lucro_atual + self.valores_vertices[vizinho]
                self.dfs(vizinho, custo_atual + custo_aresta, lucro_novo, vertices_visitados, orçamento, inicio)
                vertices_visitados.pop()
        
        # Verificar se podemos voltar ao ponto de origem (vertice `inicio`) depois de visitar todos os vértices
        if len(vertices_visitados) == self.num_vertices:
            custo_retorno = self.matriz_adj[vertice_atual][inicio]
            if custo_atual + custo_retorno <= orçamento:
                vertices_visitados.append(inicio)
                self.dfs(inicio, custo_atual + custo_retorno, lucro_atual, vertices_visitados, orçamento, inicio)
                vertices_visitados.pop()

    def explorar_todas_rotas(self, orçamento):
        # Começar pelo vértice 'a' que é o índice 0
        inicio = 0
        self.dfs(inicio, 0, self.valores_vertices[inicio], [inicio], orçamento, inicio)
        print(f"Maior lucro: {self.melhor_lucro} - Rota: {self.melhor_rota}")

# Valores fornecidos
matriz_adj = [
    [0, 1, 2, 5],
    [1, 0, 6, 4],
    [2, 6, 0, 4],
    [5, 4, 4, 0]
]

valores_vertices = [10, 20, 30, 40]
orcamento = 10

grafo = Grafo(matriz_adj, valores_vertices)
grafo.explorar_todas_rotas(orcamento)
