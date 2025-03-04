import math

# função para calcular a distância
def calcular_distancia(ponto: list[tuple[int, int]]) -> None:
    if not ponto:
        return
    
    def calcular(p: tuple[int, int]) -> float:
        x, y = p
        return math.sqrt(x**2 + y**2)
        
    distancias = {p: calcular(p) for p in ponto}
    print(f'ponto mais distante --> {max(distancias, key=distancias.get)}')
    
    print(f'{sum(distancias.values())}')

# programa principal
ponto = [(1, 2), (0, 0), (2, 1), (-1, -2)]
calcular_distancia(ponto)