def ordenar_intervalos(intervalos):    
    n = len(intervalos)
    for i in range(n):
        for j in range(i + 1, n):
            if intervalos[i][0] > intervalos[j][0]:
                intervalos[i], intervalos[j] = intervalos[j], intervalos[i]
    return intervalos

def processar_intervalos(intervalos):   
    if not intervalos:
        return 0, 0, []
   
    intervalos = ordenar_intervalos(intervalos)
    
    intervalos_unidos = []
    intervalo_atual = intervalos[0]
    
    for i in range(1, len(intervalos)):
        inicio, fim = intervalo_atual
        proximo_inicio, proximo_fim = intervalos[i]
                
        if fim >= proximo_inicio:
            intervalo_atual = (inicio, max(fim, proximo_fim))
        else:
            intervalos_unidos.append(intervalo_atual)
            intervalo_atual = intervalos[i]
    
    intervalos_unidos.append(intervalo_atual)
        
    total_intervalos = len(intervalos_unidos)
        
    soma_comprimentos = 0
    for inicio, fim in intervalos_unidos:
        soma_comprimentos += fim - inicio
    
    return total_intervalos, soma_comprimentos, intervalos_unidos

def main():    
    entrada = input("Digite os intervalos no formato a,b; a,b; ...: ")
        
    intervalos = []
    for item in entrada.split(';'):
        item = item.strip()
        if item:
            try:
                a, b = map(int, item.split(','))
                if a <= b:
                    intervalos.append((a, b))
                else:
                    print(f"Intervalo inválido (a > b): {item}")
            except ValueError:
                print(f"Formato inválido para o intervalo: {item}")
    
    if not intervalos:
        print("Nenhum intervalo válido foi informado.")
        return
    
    total_intervalos, soma_comprimentos, intervalos_resultantes = processar_intervalos(intervalos)

    print("\nIntervalos unidos:")
    for intervalo in intervalos_resultantes:
        print(intervalo)

    print(f"\nNúmero total de intervalos resultantes: {total_intervalos}")
    print(f"Soma total dos comprimentos dos intervalos: {soma_comprimentos}")

if __name__ == "__main__":
    main()
