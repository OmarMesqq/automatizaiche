# AutomatizAIChE 
# V 1.0
#
# Projeto Piloto de Programação da AIChE UFRJ
#   Omar Mesquita

# Módulos

import pandas as pd 
import pywhatkit as pwk
from time import sleep 
from text import texto

# Criação do database (db) oriundo dos dados alimentados pela planilha Excel
db = pd.read_excel(r"C:\dados.xlsx")


# Variável utilizada para determinar quantos nomes há na lista de candidates
a = db.iloc[:,0]  

for i in range(len(a)): 
    
    nome = db.iloc[i,0]
    tel  = db.iloc[i,1]
    sit  = db.iloc[i,2]

    msg = texto(nome)

    if sit == 'Aprovade' or sit == 'aprovade':

            pwk.sendwhatmsg_instantly(
   
                phone_no = "+{}".format(tel), 
                message = msg,
                tab_close = True
            )

            # Esse é o tempo médio para que o programa envie a mensagem no navegador
            sleep(20) 
