import requests
from pdfminer.high_level import extract_text

caminho = r'CAMINHO_DO_ARQUIVO_PDF_BAIXADO'

def PedidoAI(url, comentCNPJ, comentOC, comentEndEnt, comentItemPC, comentCodigo, comentQuant, comentPreco, comentDesc):

    pedido  = extract_text(caminho)
    texto   =f'''abaixo vou enviar os dados extraidos de um pdf que seria um pedido de venda, com as informações preciso que você crie um json para mim no seguinte formato:
            "CNPJ": "cnpj_do_cliente", //{comentCNPJ}
            "PED_COMPRA": "numero_da_ordem_de_compra", //{comentOC}
            "MSGNOTA": "OC: numero_da_ordem_de_compra - endereço_de_entrega_do_cliente//{comentEndEnt}",
            "ENDENT": "endereço_de_entrega_do_cliente //{comentEndEnt}"
            "Itens": 
                "Itempc": "contagem_dos_itens", //{comentItemPC}
                "Produto": "codigo_do_produto",//{comentCodigo}
                "Quantidade": "quantidade_do_produto",//{comentQuant}
                "Preco": "preco_unitario_do_produto", //{comentPreco}
                "Descricao": "descricao_ou_nome_do_produto"//{comentDesc}

    REPITA O SUB-JSON "Itens" PARA CADA ITEM QUE APARECE NO PEDIDO.

    NÃO FORMATE O JSON, TRAGA ELE EM UMA LINHA SÓ

    SE A descricao_ou_nome_do_produto TIVER CARACTERE ESPECIAL OU ASPAS EXCLUA

    TEXTO EXTRAIDO DO PDF: {pedido}'''

    body = {"contents": [
            {"parts": [
                {"text": texto}
            ]}]}

    response = requests.post(url, json=body).json()

    json    = response['candidates'][0]['content']['parts'][0]['text']
    json    = str(json).split('{', 1)[1].split('}]}', 1)[0].replace('null','""')
    json    = str(json).replace('\n','')
    json    = '{' + json + '}]}'

    return json
