#import package
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import locale
from PIL import Image

#import the data
df= pd.read_csv('df_clean.csv')

#head
#image by @serjosoza - from Unsplah 

st.set_page_config(page_title='Prevendo valores de apto SP', page_icon=None, layout='centered', initial_sidebar_state= 'expanded')

image= Image.open("image.png")
st.image(image, use_column_width=True)

st.subheader("Escolha as opções abaixo:")


#input parameters
list_district = ['Alto de Pinheiros', 'Anhanguera', 'Aricanduva', 'Artur Alvim', 'Barra Funda', 'Bela Vista', 'Belém', 'Bom Retiro', 'Brasilândia', 'Brooklin', 'Brás', 'Butantã', 'Cachoeirinha', 'Cambuci', 'Campo Belo', 'Campo Grande', 'Campo Limpo', 'Cangaíba', 'Capão Redondo', 'Carrão', 'Casa Verde', 'Cidade Ademar', 'Cidade Dutra', 'Cidade Líder', 'Cidade Tiradentes', 'Consolação', 'Cursino', 'Ermelino Matarazzo', 'Freguesia do Ó', 'Grajaú', 'Guaianazes', 'Iguatemi', 'Ipiranga', 'Itaim Bibi', 'Itaim Paulista', 'Itaquera', 'Jabaquara', 'Jaguaré', 'Jaraguá', 'Jardim Helena', 'Jardim Paulista', 'Jardim São Luis', 'Jardim Ângela', 'Jaçanã', 'José Bonifácio', 'Lajeado', 'Lapa', 'Liberdade', 'Limão', 'Mandaqui', 'Medeiros', 'Moema', 'Mooca', 'Morumbi', 'Pari', 'Parque do Carmo', 'Pedreira', 'Penha', 'Perdizes', 'Perus', 'Pinheiros', 'Pirituba', 'Ponte Rasa', 'Raposo Tavares', 'República', 'Rio Pequeno', 'Sacomã', 'Santa Cecília', 'Santana', 
'Santo Amaro', 'Sapopemba', 'Saúde', 'Socorro', 'São Domingos', 'São Lucas', 'São Mateus', 'São Miguel', 'São Rafael', 'Sé', 'Tatuapé', 'Tremembé', 'Tucuruvi', 'Vila Andrade', 'Vila Curuçá', 'Vila Formosa', 'Vila Guilherme', 'Vila Jacuí', 'Vila Leopoldina', 'Vila Madalena', 'Vila Maria', 'Vila Mariana', 'Vila Matilde', 'Vila Olimpia', 'Vila Prudente', 'Vila Sônia', 'Água Rasa']

col1, col2= st.beta_columns(2)
with col1:
    Size= st.slider('Tamanho em m²:', int(df.Size.min()), int(df.Size.max()), int(df.Size.mean()))
with col2:
    Parking= st.slider('Quantas vagas de estacionamento?', int(df.Parking.min()), int(df.Parking.max()), int(df.Parking.mean()))


col3, col4, col5 = st.beta_columns(3)
with col3:
    Rooms= st.selectbox('Quantos quartos?',('1','2','3','4','5','6','7','8','9','10'))
with col4:
    Toilets= st.selectbox('Quantos banheiros',('1','2','3','4','5','6','7','8'))
with col5:
    Suites = st.selectbox('Quantas suítes?', ('0','1','2','3','4','5','6'))


col6, col7, col8, col9 = st.beta_columns(4)
with col6:
    Elevator = st.radio('Elevador?', ('Sim', 'Não'))
    Elevator = 1 if Elevator == 'Sim' else 0


with col7:
    Furnished = st.radio('Mobiliado?', ('Sim', 'Não')) 
    Furnished = 1 if Furnished == 'Sim' else 0
    
with col8: 
    Pool= st.radio('Piscina?', ('Sim', 'Não'))    
    Pool = 1 if Pool == 'Sim' else 0

with col9:
    New= st.radio('Apartamento novo?', ('Sim','Não'))    
    New= 1 if New == 'Sim' else 0


col10, col11 = st.beta_columns(2)
    
with col10:
    District= st.selectbox('Em qual bairro?', tuple(list_district))
    District = list_district.index(District)           
with col11:
    ""

Type= st.radio('O que deseja?', ('Comprar','Alugar'))    
Type = 1 if Type == 'Comprar' else 0


data= {'Size': Size, 'Rooms': Rooms, 'Toilets': Toilets, 'Suites': Suites,'Parking': Parking,
'Elevator': Elevator, 'Furnished': Furnished, 'Pool': Pool, 
'New': New, 'District':District, 'Type': Type}

features= pd.DataFrame(data, index=[0])

#model and predict
model= pickle.load(open('modelpredict.pkl', 'rb'))
result=""
if st.button('Buscar'):
    result= float(model.predict(features))
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    valor = locale.currency(float(result), grouping=True, symbol=None)
    print(valor)
    valor = valor.replace('.', ',').replace(',', '.',  2 if result > 1000000.0 else 1)
    print(valor)
    st.write('---')
    st.markdown('Conforme as opções selecionadas, o modelo preveu que o valor é **R${}**'.format(valor))

st.write('---')
st.write('*Este app prevê valores de imóveis situados na cidade de São Paulo, usando um modelo de machine learning. Para consultar a documentação acesse meu [GitHub](https://github.com/jdomeneghini/ML_WebApp).*')
