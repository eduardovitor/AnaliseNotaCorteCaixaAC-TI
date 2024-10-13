import re
import glob
import csv

# Dados extraídos do link: https://www.in.gov.br/web/dou/-/edital-n-9/2024/nm-de-05-de-agosto-de-2024-576447662

HEADERS = ["Polo","Nota/AC"]

dados = []
dados.insert(0,HEADERS)
nome_dataset = "dataset_ac_caixa.csv"

for arquivo in glob.glob("data/*.txt"):
    with open(arquivo, "r") as f:
        polo = re.search(r'(?<=/)([^/_]+)(?=_)',arquivo).group()
        conteudo = f.read()
        notas = re.findall(r'\b\d+,\d+\b',conteudo)
        for nota in notas:
            dados.append(
                [
                    polo,
                    int(nota.split(",")[0])
                ]
        )

with open(nome_dataset, "w") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerows(dados)
