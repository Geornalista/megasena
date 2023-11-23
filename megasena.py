import streamlit as st
import numpy as np

# LAYOUT=========================================================================================
st.set_page_config(
  page_title='TESTA NÚMEROS DA MEGASENA',
  page_icon='💰',
  layout="wide")

st.header('💰 Digite os números a serem testados (Entre 1 e 60): 💰')

numeros = st.text_input(' ','')

numeros = numeros.split()
palpite = []
for item in numeros:
    if int(item) < 61:
        palpite.append(int(item))
    else:
        st.write('Número digitado maior que 60',int(item))

filename = 'megasena.txt'
data = np.loadtxt(filename,skiprows=0,unpack=True)
nsize = data.shape[1]

quadra = 0
quina = 0
sena = 0

for i in range(nsize):
    tt = 0
    tmp = (data[:,i])
    for item in palpite:
        if item in tmp:
            tt = tt+1
    if tt == 4:
        quadra = quadra+1
    elif tt == 5:
        quina = quina+1
    elif tt == 6:
        sena = sena+1

texto1 = '💰 NÚMERO DE QUADRAS: ' + str(quadra) + '💰'
texto2 = '💰💰 NÚMERO DE QUINAS: ' + str(quina) + '💰💰'
texto3 = '💰💰💰 NÚMERO DE MEGASENAS: ' + str(sena) + '💰💰💰'

st.header(texto1)
st.header(texto2)
st.header(texto3)
