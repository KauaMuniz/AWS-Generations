import re
from pathlib import Path

arquivo_sequencia = Path(__file__).with_name("preproinsulin-seq.txt")

with arquivo_sequencia.open("r", encoding="utf-8") as arquivo:
    conteudo_arquivo = arquivo.read()


conteudo_limpo = re.findall("[a-z]+",conteudo_arquivo)


print("A sequência proteica de forma limpa:")
print("")
print("".join(conteudo_limpo))
print("")
contador = 0

for caracte in "".join(conteudo_limpo):
    contador += 1

print(f"A quantidade caracteres da sequência é de : {contador}")
