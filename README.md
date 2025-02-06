# Processador de Arquivos Python

Este projeto processa um arquivo de texto que contém logs de erros.

## Funcionalidade

O script realiza os seguintes passos:

1. Permite o upload manual de um arquivo de log (`ERROS -  LOG.txt`).
2. Lê o arquivo enviado, tentando diferentes codificações (UTF-8, Latin-1, ISO-8859-1).
3. Processa o conteúdo do arquivo para dividir entradas longas de `TO_CLOB` em duas partes.
4. Salva o arquivo processado com o nome `ERROS - RIRA LOG_PROCESSADO.txt`.
5. Baixa o arquivo processado para o computador do usuário.

## Como Usar

1. Faça o upload do arquivo de log `ERROS -  LOG.txt` quando solicitado.
2. O script tentará ler o arquivo em diferentes codificações (UTF-8, Latin-1, ISO-8859-1) e processar as linhas.
3. Após o processamento, o arquivo será baixado automaticamente como `ERROS - RIRA LOG_PROCESSADO.txt`.

## Dependências

- `google.colab`: Usado para upload e download de arquivos no Google Colab.
- `os`: Manipulação de arquivos e diretórios no sistema.

## Instalação

Este script foi projetado para ser executado no Google Colab. Não há necessidade de instalação adicional além do ambiente Colab.

1. Faça o upload do arquivo `ERROS - RIRA LOG.txt` quando solicitado.
2. Execute o script para processar o arquivo.

## Observações

- Certifique-se de que o arquivo de log esteja corretamente formatado conforme esperado.
- Caso o script não consiga processar o arquivo, ele tentará diferentes codificações automaticamente.
- O arquivo de saída será baixado automaticamente após o processamento.

## Contribuições

Sinta-se à vontade para fazer contribuições! Se você encontrar problemas ou desejar melhorias, crie uma issue ou um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
