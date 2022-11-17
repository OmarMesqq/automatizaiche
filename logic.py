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
from tkinter.filedialog import askopenfilename


def upload(): 

    arquivo = askopenfilename(
        filetypes= (("Arquivos Excel","*.xlsx"), ("all files","*.*"))                    
    )

    db = pd.read_excel(arquivo) 

    # Variável utilizada para quantidade de candidates na planilha                              
    a = db.iloc[:,0]  


    for i in range(len(a)): 
    
        nome = db.iloc[i,0]
        tel  = db.iloc[i,1]
        sit  = db.iloc[i,2]

        msg = texto(nome)
    

    if sit == 'aprovade' or sit == 'Aprovade':

            pwk.sendwhatmsg_instantly(
   
                phone_no = "+{}".format(tel), 
                message = msg,
                tab_close = True,
                wait_time = 5
            )
        
            sleep(20)