
# função para comparar as notas
def comparar_nota(prova1: list[tuple[str, int]], prova2: list[tuple[str, int]]) -> None:
    nota_prova1 = {nome: nota for nome, nota in prova1}
    nota_prova2 = {nome: nota for nome, nota in prova2}
    
    melhoraram = []
    pioraram = []
    mantiveram = []
    
    for nome in nota_prova1:        
        nota1 = nota_prova1[nome]
        nota2 = nota_prova2[nome]
            
        if nota2 > nota1:
            melhoraram.append(nome)
        elif nota2 < nota1:
            pioraram.append(nome)
        else:
            mantiveram.append(nome)       
                
    print(f"melhoraram --> {melhoraram}")   
    print(f"pioraram --> {pioraram}")   
    print(f"mantiveram --> {mantiveram}")   


# programa principal
prova1 = [('A', 2), ('B', 9), ('C', 10), ('D', 8)]
prova2 = [('A', 1), ('B', 10), ('C', 10), ('D', 7)]
comparar_nota(prova1, prova2)