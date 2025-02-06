from google.colab import files
import os

# Passo 1: Upload manual do arquivo
print("📂 Faça o upload do arquivo 'ERROS -  LOG.txt'")
uploaded = files.upload()

# Obtém o nome do arquivo enviado
arquivo_nome = list(uploaded.keys())[0]
print(f"✅ Arquivo carregado: {arquivo_nome}")

# Verifica se o arquivo existe
if not os.path.exists(arquivo_nome):
    print("❌ Erro: Arquivo não encontrado após upload!")
    exit()

# Função para processar as linhas do arquivo
def processar_linhas(linhas):
    resultado = []
    for linha in linhas:
        if "TO_CLOB" in linha and "||" in linha:
            partes = linha.split("||", 1)  # Divide a linha apenas na primeira ocorrência de ||

            # Se houver partes para processar
            if len(partes) > 1:
                parte_1 = partes[0].strip()  # Parte antes do TO_CLOB
                conteudo_clob = partes[1].strip().replace("TO_CLOB(q'[", "").replace("]')", "")  # Remover TO_CLOB e q'[ ]'

                # Dividir o conteúdo do TO_CLOB em duas partes longas, mantendo a estrutura JSON
                ponto_divisao = len(conteudo_clob) // 2
                posicao_divisao = conteudo_clob.find(",", ponto_divisao)
                if posicao_divisao == -1:
                    posicao_divisao = conteudo_clob.find("}", ponto_divisao)  # Caso não haja vírgula, tentamos após uma chave
                
                parte_2 = conteudo_clob[:posicao_divisao].strip()  # Primeira linha do TO_CLOB
                parte_3 = conteudo_clob[posicao_divisao:].strip()  # Segunda linha do TO_CLOB

                # Montar as duas linhas de TO_CLOB
                linha_sintetizada_1 = parte_1 + " || TO_CLOB(q'[" + parte_2 + "]')"
                linha_sintetizada_2 = " || TO_CLOB(q'[" + parte_3 + "]')"

                # Adicionar as duas linhas ao resultado
                resultado.append(linha_sintetizada_1)
                resultado.append(linha_sintetizada_2)
            else:
                resultado.append(linha.strip())
        else:
            resultado.append(linha.strip())  # Para as linhas que não têm TO_CLOB
    return resultado

# Tentando abrir o arquivo com diferentes codificações
codificacoes = ['utf-8', 'latin-1', 'ISO-8859-1']
for encoding in codificacoes:
    try:
        with open(arquivo_nome, 'r', encoding=encoding) as file:
            linhas = file.readlines()
        print(f"✅ Arquivo lido com sucesso usando a codificação: {encoding}")
        break  # Sai do loop se a leitura for bem-sucedida
    except UnicodeDecodeError:
        print(f"⚠️ Falha ao ler com {encoding}, tentando outra codificação...")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        exit()

# Processando as linhas
linhas_processadas = processar_linhas(linhas)

# Criando o arquivo de saída
arquivo_saida = "ERROS -  LOG_PROCESSADO.txt"
with open(arquivo_saida, 'w', encoding='utf-8') as file:
    file.writelines(linha + '\n' for linha in linhas_processadas)

print(f"✅ Arquivo processado com sucesso! Salvo como: {arquivo_saida}")

# Baixando o arquivo processado para o computador
files.download(arquivo_saida)
