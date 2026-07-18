# Passo a passo do projeto
# abrir os 6 arquivos
# para cada arquivo
# verificar se algum valor na coluna vendas dequele arquivo e maior que 55.000
# se for maior que 55.000 envia o sms
# caso não seja maior não faz nada
import pandas as pd
import os
from twilio.rest import Client

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho' ]
for mes in lista_meses:
    
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    
    if (tabela_vendas['Vendas'] > 55.000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55.000,'Vendedor'].values[0]
        vendas =  tabela_vendas.loc[tabela_vendas['Vendas'] > 55.000,'Vendas'].values[0]
        print(f'Encontrou no mês {mes} {vendedor} com {vendas} e bateu a meta!') 

# Configuração para envio das mensagens SMS ou e-mail a depender da necessidade para empresa