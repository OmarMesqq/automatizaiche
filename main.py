# AutomatizAIChE 
#
# Projeto Piloto de Programação da AIChE UFRJ
#   Omar Mesquita
#  
# Roteiro de automação de mensagens para o Processo Seletivo da AIChE UFRJ


# Soft depends

# Geralmente, são bibliotecas inclusas nos imports principais mas que 
# não necessariamente são incluídas na instalação padrão. 

# openpyxl (para o pandas ler arquivos .xlsx)
# tk ou TkInter (em sistemas Linux, para a interface gráfica do pywhatkit)

# Hard depends

import pandas as pd 
import pywhatkit as pwk
from time import sleep 

db = pd.read_excel(r"dados.xlsx") # Criação do database (db) oriundo dos dados alimentados 
                                 # pela planilha Excel

a = db.iloc[:,0]  # Variável utilizada para determinar quantos nomes há na lista de candidates

for i in range(len(a)): 
    
    nome = db.iloc[i,0]
    tel  = db.iloc[i,1]
    sit  = db.iloc[i,2]


    texto = "Isso é um teste. Ignore. oi, {}, tudo bem? Viemos dizer que você foi {}".format(nome, sit)


    if sit == 'Aprovade':

            pwk.sendwhatmsg_instantly(
   
                phone_no = "+{}".format(tel), 
                message = texto,
                tab_close = True
            )
            sleep(20) # Esse é o tempo médio para que o programa envie a mensagem no navegador
