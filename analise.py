import pandas as pd
import tabula


relatorio = pd.read_excel("arquivos\drive.xlsx")

convenio = pd.DataFrame(relatorio["CONVENIO"])
#Definindo quais são os convenios existentes
convenios = set(convenio)
#Quantificando quantos serviços foram solicitados por cada convenio
quantidade = convenio["CONVENIO"].value_counts()
print(quantidade)
total = relatorio["VALOR"].sum()
print(f"Total: R$ {total}")
