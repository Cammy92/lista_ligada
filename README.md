# Aplicação de Lista Ligada - Instruções de Execução e Testes

Este repositório contém uma implementação de lista ligada em Python, incluindo a classe `OutOfBoundsException`, e testes associados para verificar o funcionamento da lista ligada e da exceção.

## Instruções de Execução

Siga estas etapas para executar os testes na lista ligada:

### Pré-requisitos

Antes de começar, certifique-se de que você tenha o Python instalado no seu sistema. Você pode baixar o Python em [https://www.python.org/downloads/](https://www.python.org/downloads/).

### Passo 1: Clonar o Repositório

Clone este repositório em seu sistema local usando o seguinte comando Git:

```bash
git clone https://github.com/Cammy92/lista_ligada.git
```

### Passo 2: Navegar até o Diretório

Navegue até o diretório do repositório clonado usando o terminal ou prompt de comando:

```bash
cd lista_ligada
```

### Passo 3: Executar os Testes

Execute os testes da lista ligada com o seguinte comando:

```bash
pytest main.py
```
Os testes serão executados e você verá a saída no terminal. Certifique-se de que todos os testes passem com sucesso.

### Testes da Classe OutOfBoundsException
A classe OutOfBoundsException é testada nos testes da lista ligada, garantindo que seja levantada corretamente quando ocorrerem índices fora dos limites da lista. Os testes incluem o seguinte:

Tentativa de acessar um índice 0 em uma lista vazia.
Tentativa de acessar um índice 5 em uma lista com menos de 5 elementos.

______________________________________________________________________________

### Instruções para Executar em um Contêiner Docker
Você também pode executar os testes da lista ligada em um contêiner Docker. Siga estas etapas:

### Pré-requisitos
Antes de prosseguir, certifique-se de que você tenha o Docker instalado em seu sistema. Você pode baixar e instalar o Docker em https://www.docker.com/get-started.

### Passo 4: Criar um Dockerfile
Antes de executar os testes, crie um arquivo Dockerfile no diretório do seu projeto. Você pode fazer isso com um editor de texto ou usando um comando de terminal, por exemplo:

```bash
touch Dockerfile
```
Abra o Dockerfile em um editor de texto e adicione o seguinte conteúdo:

```bash

# Use the official Python image from Docker Hub
FROM python:3

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o código fonte para o contêiner
COPY . /app

# Instale as dependências (se houver algum) usando o pip
RUN pip install -r requirements.txt

# Comando para executar os testes
CMD ["python", "main.py"]

```

Certifique-se de que o arquivo "Dockerfile" esteja no mesmo diretório que seu código fonte.

### Passo 4: Construir a Imagem Docker
Abra um terminal ou prompt de comando e navegue até o diretório que contém o seu Dockerfile e código fonte. Em seguida, execute o seguinte comando para construir a imagem Docker:

```bash
docker build -t lista-ligada-app .
```

O comando acima irá construir uma imagem Docker com base no Dockerfile no diretório atual. Certifique-se de incluir o ponto (.) no final do comando para indicar o diretório atual.

### Passo 5: Executar o Contêiner Docker
Após a construção bem-sucedida da imagem Docker, você pode executar um contêiner com base nessa imagem usando o seguinte comando:


```bash
docker run lista-ligada-app
```

O comando acima executará o contêiner com base na imagem "lista-ligada-app" que você criou. Os testes da lista ligada serão executados no contêiner e você verá a saída no terminal.

Certifique-se de que seu código-fonte e arquivos de teste estejam no mesmo diretório do Dockerfile.

### Contribuição
Fique à vontade para contribuir com melhorias ou correções para este repositório. Sinta-se à vontade para abrir problemas (issues) ou solicitações de pull (pull requests).

Divirta-se trabalhando com listas ligadas em Python!

Lembre-se de substituir seu-usuario e repo-da-lista-ligada pelos valores apropriados no URL do Git e nas instruções. Isso deve ajudar você a criar um README.md formatado para o GitHub com instruções de execução e testes.

