from bisseccao import bisseccao
from falsa_posicao import falsa_posicao
import math

# Função fornecida para o método da Falsa Posição
def funcao_falsa_posicao(x):
    return -4 * math.sin(x) * math.exp(x)

# Função de exemplo para a Bissecção (x^2 - 2)
def funcao_bisseccao(x):
    return x**2 - 2

# Intervalos
a_bisseccao, b_bisseccao = 1, 2
a_falsa_posicao, b_falsa_posicao = 0, 1  # Alterar conforme necessário para encontrar uma raiz válida

# Chamando os métodos
try:
    raiz_bisseccao = bisseccao(funcao_bisseccao, a_bisseccao, b_bisseccao)
    print(f"\nRaiz encontrada pelo método da Bissecção: {raiz_bisseccao:.6f}")
except ValueError as e:
    print(f"\nErro no método da Bissecção: {e}")

try:
    raiz_falsa_posicao = falsa_posicao(funcao_falsa_posicao, a_falsa_posicao, b_falsa_posicao)
    print(f"\nRaiz encontrada pelo método da Falsa Posição: {raiz_falsa_posicao:.6f}")
except ValueError as e:
    print(f"\nErro no método da Falsa Posição: {e}")
