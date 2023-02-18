import pandas as pd
import tabula


relatorio = pd.read_excel("arquivos\drive.xlsx")
convenio = relatorio["CONVENIO"]
#Definindo quais são os convenios existentes
convenios = set(convenio)
print(convenios)

if "BRUN" in convenio:
    print("sim")

