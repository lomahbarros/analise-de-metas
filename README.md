# Analise de metas

Este projeto consiste em um processo automatizado de análise de dados de vendas. O fluxo começa com a abertura de seis arquivos distintos, cada um contendo registros de vendas. Para cada arquivo, o sistema verifica se algum valor presente na coluna vendas ultrapassa o limite de 55.000. Caso seja identificado um valor superior a esse patamar, é disparado automaticamente um SMS de alerta, garantindo que a equipe responsável seja informada rapidamente sobre resultados relevantes. Se nenhum valor exceder o limite estabelecido, nenhuma ação adicional é realizada, mantendo o processo simples e eficiente. Dessa forma, o projeto assegura monitoramento contínuo e comunicação imediata em situações críticas.

A conexão com o envio do sms é por conta da biblioteca do twilio, mas como cada empresa tem sua particularidade existe varias
possibilidade de conexão e o códigos de conexão foi removido

Criador do  Projeto https://www.youtube.com/watch?v=GQpQha2Mfpg&list=PLpdAy0tYrnKznoeLzn06M-izJJpoEyzHC
