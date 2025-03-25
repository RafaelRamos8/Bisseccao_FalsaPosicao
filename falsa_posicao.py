import math

# Função fornecida
def funcao(x):
    return x**2 - 2

# Método da Falsa Posição
def falsa_posicao(funcao, a, b, precisao=1e-6, max_iter=100):
    if funcao(a) * funcao(b) > 0:
        raise ValueError("O intervalo fornecido não garante a existência de uma raiz única.")
    
    iteracao = 0
    while abs(b - a) > precisao and iteracao < max_iter:
        iteracao += 1
        
        # Calculando o ponto c (ponto da falsa posição)
        c = b - (funcao(b) * (b - a)) / (funcao(b) - funcao(a))
        
        # Exibindo os valores de a, b, c e f(c) a cada iteração
        print(f"Iteração {iteracao} | a = {a:.6f} | b = {b:.6f} | c = {c:.6f} | f(c) = {funcao(c):.6f}")
        
        # Verificar se f(c) está suficientemente próximo de 0
        if abs(funcao(c)) < precisao:
            return c
        
        # Ajustar o intervalo conforme o sinal de f(c)
        if funcao(c) * funcao(a) < 0:
            b = c
        else:
            a = c
            
    return (a + b) / 2  # Retorna o valor aproximado da raiz

# Intervalo inicial
a = 1
b = 2
precisao = 1e-6

# Chamada do método da falsa posição
raiz_falsa_posicao = falsa_posicao(funcao, a, b, precisao)

# Exibir a raiz final
print(f"Raiz encontrada pelo método da Falsa Posição: {raiz_falsa_posicao:.6f}")
