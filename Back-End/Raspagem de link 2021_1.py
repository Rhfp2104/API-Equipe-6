import requests
from bs4 import BeautifulSoup as bs
import time

dados = []
raiz = 'https://fatecsjc-prd.azurewebsites.net/api/'

url = 'https://fatecsjc-prd.azurewebsites.net/api/turmas.php'
html = requests.get(url).text
sopa = bs(html, 'html.parser')
semestres = sopa.findAll('a')

for s in semestres[2:3]:
  print ('Processando semestre...')
  time.sleep(3)
  print ('Primeiro semestre de 2021')
  time.sleep(3)
  sem = s.text.split('/')[0] #separa antes da barra
  sem = sem.split()[1] # "Turmas 2020-2" pega a 2a parte
  url = raiz + s.attrs['href']
  html = requests.get(url).text
  sopa = bs(html, 'html.parser')
  trs = sopa.findAll('tr', {'class': 'hidden'})
  for tr in trs:
    tds = tr.findAll('td')
    if len(tds) >= 3: #tem tabela sem todas as infos
      print (tds[2].text, sem, tr['id'], tds[1].text)
      dados.append([tds[2].text, sem, tr['id'], tds[1].text])


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
