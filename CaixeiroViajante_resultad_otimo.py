class Grafo:
    def __init__(self, matriz_adj, valores_vertices):
        self.matriz_adj = matriz_adj
        self.valores_vertices = valores_vertices
        self.num_vertices = len(valores_vertices)
        self.melhor_lucro = 0
        self.melhor_rota = []
        self.max_vertices_visitados = 0

    def dfs(self, vertice_atual, custo_atual, lucro_atual, vertices_visitados, orçamento):
        if custo_atual > orçamento:
            return

        # Verificar se podemos retornar ao ponto inicial dentro do orçamento
        if len(vertices_visitados) > 1:  # Somente considerar retornar se ao menos um vértice além do inicial foi visitado
            custo_retorno = self.matriz_adj[vertice_atual][0]
            if custo_atual + custo_retorno <= orçamento:
                lucro_total = lucro_atual + self.valores_vertices[0]
                if len(vertices_visitados) > self.max_vertices_visitados or \
                   (len(vertices_visitados) == self.max_vertices_visitados and lucro_total > self.melhor_lucro):
                    self.max_vertices_visitados = len(vertices_visitados)
                    self.melhor_lucro = lucro_total
                    self.melhor_rota = vertices_visitados[:] + [0]

        for vizinho in range(self.num_vertices):
            if self.matriz_adj[vertice_atual][vizinho] > 0 and vizinho not in vertices_visitados:
                custo_aresta = self.matriz_adj[vertice_atual][vizinho]
                vertices_visitados.append(vizinho)
                lucro_novo = lucro_atual + self.valores_vertices[vizinho]
                self.dfs(vizinho, custo_atual + custo_aresta, lucro_novo, vertices_visitados, orçamento)
                vertices_visitados.pop()

    def explorar_todas_rotas(self, orçamento):
        self.dfs(0, 0, self.valores_vertices[0], [0], orçamento)
        if self.melhor_rota:
            melhor_rota_nomes = [chr(97 + v) for v in self.melhor_rota]
            print(f"Maior lucro: {self.melhor_lucro} - Rota: {melhor_rota_nomes}")
        else:
            print("Não foi possível encontrar uma rota dentro do orçamento")

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
