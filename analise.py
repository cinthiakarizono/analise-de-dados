import pandas as pd
import tabula

# converter pdf em csv
tabula.convert_into("arquivos/relatorio.pdf", "arquivos/relatorio.csv", output_format = "csv", pages = "all")
