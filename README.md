# **Automatização de Pedidos de Compra em PDF**

## **Apresentação do projeto:**
Esse é um projeto para incluir pedidos automaticamente e evitar que um vendedor tenha que ficar digitando manualmente todos os pedidos que uma empresa recebe, para isso criei um programa que se inicia via API. Basicamente quando um pedido (arquivo pdf) for incluido na pasta "Pedidos" no Google Drive (ou OneDrive), irá gerar um gatilho que irá enviar uma requisição HTTP para uma API em Python(arquivo app.py) que irá iniciar o trabalho de extrair os dados(arquivo caoa.py) desse PDF e enviar para o Gemini analisar e criar um JSON que poderá ser incluido em meu sistema ERP automaticamente. Esse projeto suporta diversos clientes com PDFs diferentes, já que você pode enviar na API de ativação (arquivo app.py) o comentário explicando onde está cada informação no PDF. 

## **Objetivo:**

Automatizar a leitura e inclusão de pedidos de compra em formato PDF em um sistema ERP através do envio de dados via JSON.

## **Ferramentas:**

Biblioteca pdfminer: Utilizada para extrair informações do arquivo PDF, como dados do cliente, itens do pedido, valores e informações de pagamento.
Biblioteca requests: Utilizada para enviar os dados extraídos do PDF para o sistema em formato JSON.

## **Funcionamento:**

Quando um pedido em formato PDF entra em uma pasta é enviado uma requisição POST para a API desenvolvida em Python.
O Python irá baixar esse arquivo e extrair o texto desse PDF com a biblioteca pdfminer.
Após isso é enviado para o Gemini via API com a biblioteca requests, um prompt padrão para que ele leia o conteúdo do pedido e crie um JSON para incluir no sistema.
O Gemini retorna o JSON e ai vocês enviam esse JSON para seu sistema ERP.


## **Benefícios:**

Ganho de tempo: Redução do tempo e esforço manual necessário para inserir pedidos de compra no sistema.
Melhoria da precisão: Diminuição de erros de digitação manual, garantindo a integridade dos dados.
Aumento da eficiência: Otimização do processo de recebimento e processamento de pedidos de compra.

## **Comentários:**

Já desenvolvi essa mesma ferramenta e já esta em produção na minha empresa, aumentamos a taxa de EDI em 53% (11-05-2024) em apenas uma semana utilizando o mesmo prompt para diversos clientes (mudando apenas o comentário para cada pedido).
Não divulguei no projeto a parte de download do pedido e inclusão no ERP, pois isso iria contra as politicas de desenvolvimento da minha empresa. Mas basicamente você vai criar um gatilho para quando um arquivo (PDF) for criado em uma pasta no Google Drive ou outro sistema de Nuvem, envie uma requisição HTTP (arquivo modelo.json) para a API em Python (arquivo app.py) que inicia o prompt do Gemini e retornar um JSON que será enviado por outra API para incluir no sistema automaticamente.
