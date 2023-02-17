import pandas as pd
import tabula

# converter pdf em csv
relatorio = tabula.read_pdf("arquivos/relatorio.pdf", pages = "all")
print(relatorio)
filtrado = relatorio["Líquido"]