def calcular_prob_fenotipo_dominante(k, m, n):
    """
    Calcula a probabilidade de dois organismos selecionados aleatoriamente
    produzirem um descendente com fenótipo dominante.

    Argumentos:
    k (int): Número de indivíduos homozigotos dominantes ('AA')
    m (int): Número de indivíduos heterozigotos ('Aa')
    n (int): Número de indivíduos homozigotos recessivos ('aa')

    Retorna:
    float: A probabilidade do descendente ter o fenótipo dominante.
    """
    
    # 1. População total
    total_pop = k + m + n
    
    # 2. Total de pares possíveis (usando permutações, T * (T-1))
    # Este é o nosso denominador (espaço amostral).
    total_pares = total_pop * (total_pop - 1)
    
    # 3. Calcular a probabilidade de cada evento que gera um 'aa'
    
    # Caso 1: 'Aa' x 'Aa' (m x m)
    # Probabilidade do par: (m * (m-1)) / total_pares
    # Probabilidade de 'aa' nesse par: 0.25
    prob_mm = (m * (m - 1)) / total_pares
    
    # Caso 2: 'Aa' x 'aa' (m x n) e (n x m)
    # Probabilidade do par: (m*n + n*m) / total_pares = (2*m*n) / total_pares
    # Probabilidade de 'aa' nesse par: 0.5
    prob_mn = (2 * m * n) / total_pares
    
    # Caso 3: 'aa' x 'aa' (n x n)
    # Probabilidade do par: (n * (n-1)) / total_pares
    # Probabilidade de 'aa' nesse par: 1.0
    prob_nn = (n * (n - 1)) / total_pares
    
    # 4. Somar as probabilidades de gerar um 'aa' (fenótipo recessivo)
    prob_total_recessivo = (prob_mm * 0.25) + (prob_mn * 0.5) + (prob_nn * 1.0)
    
    # 5. A probabilidade do fenótipo dominante é o complemento (1 - P(aa))
    prob_dominante = 1 - prob_total_recessivo
    
    return prob_dominante

# Exemplo de uso
k_ex = 26
m_ex = 23
n_ex = 28

probabilidade = calcular_prob_fenotipo_dominante(k_ex, m_ex, n_ex)
print(f"Populacao: k={k_ex}, m={m_ex}, n={n_ex}")
print(f"Probabilidade de fenotipo dominante: {probabilidade:.5f}")
