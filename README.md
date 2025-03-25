# trabalho_individual_2_FPAA
# MaxMin Select - Algoritmo de Seleção Simultânea do Maior e Menor Elemento

## Descrição do Projeto
Este projeto implementa o algoritmo **MaxMin Select** utilizando a técnica de **Divisão e Conquista**. O objetivo é encontrar o maior e o menor elemento de um array com um número reduzido de comparações em relação a uma abordagem ingênua. O método divide o problema em subproblemas menores, resolve-os recursivamente e combina os resultados para obter o máximo e o mínimo.

## Estrutura do Código
O algoritmo segue a seguinte lógica:
1. **Caso base**:
   - Se houver apenas um elemento no array, ele é tanto o mínimo quanto o máximo.
   - Se houver dois elementos, basta compará-los diretamente para determinar o mínimo e o máximo.
2. **Divisão**:
   - O array é dividido ao meio.
3. **Conquista**:
   - O algoritmo é chamado recursivamente para cada metade.
4. **Combinação**:
   - Os resultados das duas metades são combinados para determinar o mínimo e o máximo globais.

### Código-fonte (`main.py`)
O código implementa essa lógica da seguinte forma:

```python
# Implementação do algoritmo MaxMin Select

def maxmin_select(arr, left, right):
    if left == right:
        return arr[left], arr[left]
    
    if right - left == 1:
        if arr[left] < arr[right]:
            return arr[left], arr[right]
        else:
            return arr[right], arr[left]
    
    mid = (left + right) // 2
    min1, max1 = maxmin_select(arr, left, mid)
    min2, max2 = maxmin_select(arr, mid + 1, right)
    
    return min(min1, min2), max(max1, max2)


if __name__ == "__main__":
    arr = [3, 1, 9, 7, 5, 11, 2, 8]
    min_val, max_val = maxmin_select(arr, 0, len(arr) - 1)
    print(f"Menor elemento: {min_val}, Maior elemento: {max_val}")
```

## Como Executar o Projeto
Para rodar o código localmente, siga os passos:
1. Clone o repositório:
   ```bash
   git clone <https://github.com/JoseMiguel-ofc/trabalho_individual_2_FPAA.git>
   ```
2. Acesse a pasta do projeto:
   ```bash
   cd <trabalho_individual_2_FPAA>
   ```
3. Execute o script:
   ```bash
   python main.py
   ```

## Análise da Complexidade Assintótica

### Contagem de Comparações
O algoritmo reduz o número de comparações em relação a uma abordagem ingênua:
1. **Número de comparações em cada etapa**:
   - No pior caso, um algoritmo ingênuo que percorre toda a lista para encontrar o mínimo e depois o máximo realiza `2(n - 1)` comparações.
   - O algoritmo **MaxMin Select** divide o array em duas metades e executa a busca em cada uma delas recursivamente.
   - A cada nível da recursão, duas chamadas são feitas, e os valores mínimo e máximo são comparados na fase de combinação.
2. **Total de comparações**:
   - O número total de comparações pode ser aproximado por **(3n/2 - 2)**.
   - Isso reduz o número de comparações em relação a uma abordagem que percorreria a lista inteira duas vezes.
3. **Complexidade final**:
   - Como cada elemento do array é processado um número constante de vezes, a complexidade do algoritmo é **O(n)**.

### Aplicação do Teorema Mestre
A recorrência do algoritmo é:
```
T(n) = 2T(n/2) + O(1)
```
Os parâmetros são:
- **a = 2** (duas chamadas recursivas)
- **b = 2** (divisão do problema em duas partes)
- **f(n) = O(1)** (tempo gasto na combinação dos resultados)

Agora, aplicamos o Teorema Mestre:
1. **Cálculo de `log_b a`**:
   ```
   log_2(2) = 1
   ```
2. **Comparação com `f(n) = O(1)`**:
   - `O(n^p)`, onde `p = 1`
   - Comparando `n^p` com `f(n)`, temos `n^1` contra `O(1)`
3. **Caso do Teorema Mestre**:
   - O caso aplicável é `O(n^p)`, pois `f(n) = O(n^c)` onde `c < p`
4. **Solução final**:
   - De acordo com o Teorema Mestre, `T(n) = O(n)`

## Conclusão
O algoritmo MaxMin Select é eficiente para encontrar o maior e o menor elemento em um array, reduzindo o número de comparações necessárias em comparação com a abordagem ingênua. Sua complexidade de tempo é **O(n)**, tornando-o ideal para grandes conjuntos de dados.

