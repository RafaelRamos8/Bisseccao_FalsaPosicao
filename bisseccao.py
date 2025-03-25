def bisseccao(funcao, a, b, precisao=1e-6, max_iter=100):
    if funcao(a) * funcao(b) >= 0:
        raise ValueError("O intervalo fornecido não garante a existência de uma raiz única.")

    print("\nMétodo da Bissecção:")
    print(f"Iteração | a\t | b\t | c\t | f(c)")

    for i in range(max_iter):
        c = (a + b) / 2  # Calcula o ponto médio
        fc = funcao(c)

        print(f"{i+1}\t | {a:.6f} | {b:.6f} | {c:.6f} | {fc:.6f}")

        if abs(fc) < precisao:
            return c  # Retorna a raiz encontrada

        if funcao(a) * fc < 0:
            b = c
        else:
            a = c

    return (a + b) / 2  # Melhor aproximação da raiz
