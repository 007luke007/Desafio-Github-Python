# 1. Crie uma função chamada 'encontrar_maximo' de numeros alearoios informados pelo usuario
# 2. A função deve receber uma lista de números como parâmetro
# 3. Ela deve retornar o maior número da lista

def encontrar_maximo(numeros):
    if not numeros:
        return None  # Retorna None se a lista estiver vazia
    maximo = numeros[0]
    for numero in numeros:
        if numero > maximo:
            maximo = numero
    return maximo

# Exemplo de uso:
numeros_usuario = [3, 5, 2, 8, 1]
maior_numero = encontrar_maximo(numeros_usuario)
print(f"O maior número é: {maior_numero}")


# Saída esperada: O maior número é: 8
# 4. Teste a função com uma lista de números fornecida pelo usuário
numeros_usuario = [10, 20, 30, 40, 50]
maior_numero = encontrar_maximo(numeros_usuario)
print(f"O maior número é: {maior_numero}")

# Saída esperada: O maior número é: 50 

# 5. Adicione tratamento de erro para garantir que a lista não esteja vazia
numeros_usuario_vazio = []
maior_numero_vazio = encontrar_maximo(numeros_usuario_vazio)

if maior_numero_vazio is None:
    print("A lista está vazia. Não é possível encontrar o maior número.")

# Saída esperada: A lista está vazia. Não é possível encontrar o maior número.

# 6. Documente a função com uma docstring explicando seu propósito e parâmetros

def encontrar_maximo(numeros):
    """
    Encontra o maior número em uma lista de números.

    Parâmetros:
    numeros (list): Uma lista de números.

    Retorna:
    int ou None: O maior número da lista ou None se a lista estiver vazia.
    """
    if not numeros:
        return None  # Retorna None se a lista estiver vazia
    maximo = numeros[0]
    for numero in numeros:
        if numero > maximo:
            maximo = numero
    return maximo
# Exemplo de uso:
numeros_usuario = [7, 14, 3, 9, 21] 
maior_numero = encontrar_maximo(numeros_usuario)
print(f"O maior número é: {maior_numero}")  
# Saída esperada: O maior número é: 21
