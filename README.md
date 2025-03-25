# bisseccao_falsaposicao

# Método da Falsa Posição e Bissecção

## Introdução

O **método da falsa posição** e o **método da bissecção** são ambos métodos numéricos utilizados para encontrar raízes de funções contínuas em intervalos fechados. Ambos os métodos baseiam-se na ideia de dividir o intervalo em subintervalos sucessivos para localizar a raiz de forma aproximada. A diferença principal entre eles está na forma de determinar os subintervalos e o ponto médio.

## Método da Falsa Posição

O **método da falsa posição** é uma melhoria do método da bissecção. Ele também parte de dois valores iniciais, `a` e `b`, mas, em vez de simplesmente calcular o ponto médio, o método calcula o ponto `c` de forma mais eficiente com base na interseção da reta que passa pelos pontos `(a, f(a))` e `(b, f(b))`.

A fórmula para calcular o ponto `c` é:

**c = b - (f(b) * (b - a)) / (f(b) - f(a))**

Onde:
- `a` e `b` são os limites do intervalo,
- `f(a)` e `f(b)` são os valores da função nos pontos `a` e `b`,
- `c` é o ponto de interseção calculado pela fórmula.

O algoritmo continua iterando até que a diferença entre `a` e `b` seja menor do que a precisão desejada (`precisao`).

### Passos do Método da Falsa Posição
1. Verificar se os valores de `f(a)` e `f(b)` têm sinais opostos. Se não tiverem, o intervalo fornecido não contém uma raiz.
2. Calcular o ponto `c` usando a fórmula:

   **c = b - (f(b) * (b - a)) / (f(b) - f(a))**

3. Avaliar `f(c)`. Se `f(c)` for suficientemente próximo de zero (ou seja, menor que a precisão), então `c` é a raiz aproximada.
4. Se `f(c)` e `f(a)` têm sinais opostos, o intervalo é ajustado para `[a, c]`, caso contrário, o intervalo é ajustado para `[c, b]`.
5. Repetir o processo até que a precisão desejada seja atingida.

## Método da Bissecção

O **método da bissecção** é um método simples, onde um intervalo inicial é fornecido e a cada iteração, o intervalo é dividido ao meio para encontrar um ponto médio, que é testado para ver se a raiz está nesse ponto. Se a raiz não for encontrada, o intervalo é ajustado.

### Passos do Método da Bissecção
1. Verificar se `f(a)` e `f(b)` têm sinais opostos. Se não tiverem, o intervalo não pode ser usado.
2. Calcular o ponto médio `c = (a + b) / 2`.
3. Avaliar `f(c)`. Se `f(c)` for suficientemente próximo de zero, então `c` é a raiz aproximada.
4. Ajustar o intervalo dependendo do sinal de `f(c)`.
5. Repetir o processo até que a precisão desejada seja atingida.

## Comparação entre os Métodos

O **método da falsa posição** tende a convergir mais rapidamente, já que ele utiliza a interpolação linear para refinar a estimativa de `c`. Por outro lado, o **método da bissecção** é mais simples e sempre convergente, mas pode ser mais lento dependendo da função.

## Exemplos de Uso

- **Falsa Posição**: útil quando o comportamento da função pode ser modelado bem por uma linha reta entre os dois pontos `a` e `b`.
- **Bissecção**: útil quando a função é contínua e garantidamente muda de sinal em algum ponto do intervalo.

Ambos os métodos são eficazes para encontrar raízes aproximadas em funções contínuas, sendo a escolha entre eles dependente da rapidez desejada e da complexidade da função.
