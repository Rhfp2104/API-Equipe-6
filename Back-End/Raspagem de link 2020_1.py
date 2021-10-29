import requests
from bs4 import BeautifulSoup as bs
import time

dados = []
raiz = 'https://fatecsjc-prd.azurewebsites.net/api/'

url = 'https://fatecsjc-prd.azurewebsites.net/api/turmas.php'
html = requests.get(url).text
sopa = bs(html, 'html.parser')
semestres = sopa.findAll('a')

#primeiro semestre tem uma estrutura diferente
print ('Processando semestre...')
time.sleep(3)
print ('Primeiro semestre de 2020')
time.sleep(3)
url = raiz + semestres[0].attrs['href']
html = requests.get(url).text
sopa = bs(html, 'html.parser')
turmas = sopa.findAll('a')

for t in turmas:
  u = raiz + '2020-1/' + t.attrs['href']
  html = requests.get(u).text
  sopa = bs(html, 'html.parser')
  equipes = sopa.findAll('a')
  for e in equipes:
    yt = e.attrs['href']
    print (yt,'2020-1', t.text, e.text)
    dados.append([yt,'2020-1', t.text, e.text])

#vamos pegar o github dos links do Youtube
for dado in dados:
  if not dado[0].startswith('https://'):
    #se não começa com https dá erro no requests.get
    dado[0] = 'https://' + dado[0] 
  html = requests.get(dado[0]).text
  ini = html.find(r'https://github.com')
  if ini != -1:
    fim = ini
    while html[fim] != '\\' and html[fim] != '"':
      fim = fim + 1
    print (html[ini:fim])
    dado.append(html[ini:fim])

#processamento da clonagem
for dado in dados:
  #processo de clonagem com as infos abaixo
  if len(dado) > 4: #tem github que dei append no final
    print (dado)