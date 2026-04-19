from datetime import date
import streamlit as st
from PIL import Image
from pandas import read_csv
import pandas as pd
import scipy as sc
import seaborn as snb
from matplotlib import pyplot as plt
from pandas.plotting import scatter_matrix

# Chargement des données

# Chargement correct du BeansDataSet
try:
    fichier='BeansDataSet.csv'
    data=pd.read_csv(fichier)
    data.fillna(0, inplace=True)

except Exception as e:
    st.error(f'Erreur de lecture du fichier : {e}')
    st.stop()


st.sidebar.title('Navigation')
menu=st.sidebar.selectbox('Choisir un volet',['Accueil','Aperçu des données','Etude de Corrélation','Visualization','Rapport'])

if menu=='Accueil':
    st.markdown(
        """
        <div style='text-align:center;'>
        <h1> Analyse des ventes Beans DataSet </h1>
        </div>
        """, unsafe_allow_html=True
        )
    st.dataframe(data)

    
elif menu=='Aperçu des données':
    st.header('Aperçu des données')
    #---------------------------------------------------
    st.subheader('10 premières lignes')
    st.dataframe(data.head(10))
    #---------------------------------------------------
    st.subheader('10 dernières lignes')
    st.dataframe(data.tail(10))
    #---------------------------------------------------
    st.subheader('Statistiques descriptives')   
    st.write(data.describe())
    #---------------------------------------------------
    st.subheader('Répartition des Channel')   
    class_count=data.groupby('Channel').size()
    st.write(class_count)
    #---------------------------------------------------
    figure,ax_class=plt.subplots()
    data['Channel'].value_counts().plot(kind='bar',color=['green','red'],ax=ax_class)
    ax_class.set_xlabel('Channel')
    ax_class.set_ylabel('Nombre de Vente')
    st.pyplot(figure)

elif menu=='Etude de Corrélation':
    st.header('Etude de Corrélation')
    st.subheader('Matrice de Corrélation entre produits')
    try:
        fig_corr, ax_corr = plt.subplots(figsize=(10, 6))
        corr_matrix = data[['Robusta', 'Arabica', 'Espresso', 'Lungo', 'Latte', 'Cappuccino']].corr()
        snb.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', ax=ax_corr)
        st.pyplot(fig_corr)
    except Exception as e:
        st.error(f"Erreur lors de la matrice de corrélation : {e}")


elif menu=='Visualization':
    st.header('Visualisation')
    st.subheader('Histogrammes')
    data.hist(figsize=(12,10), bins=20)
    st.pyplot(plt.gcf())

    st.subheader('Histogramme pour Arabica')
    figure_his,ax_his=plt.subplots()
    ax_his.hist(data['Arabica'],bins=20,edgecolor='black')
    ax_his.set_xlabel("Quantité d'Arabica vendue")
    ax_his.set_ylabel('Fréquence')
    st.pyplot(figure_his)


    st.subheader('Graphes de densité')
    data.plot(kind='density', subplots=True, sharex=False, figsize=(12,10))
    st.pyplot(plt.gcf())
    
    st.subheader('Les Boites a Moustaches')
    data.plot(kind='box',subplots=True,sharex=False,sharey=False,figsize=(15,15),layout=(3,3))
    st.pyplot(plt.gcf())      

    st.subheader('Scatter Matrix')
    scatter_matrix(data,figsize=(25,25),c='b')
    st.pyplot(plt.gcf())

    st.subheader('Pairplot')
    graphe = snb.pairplot(data)
    st.pyplot(graphe.fig)
    
    st.subheader('Pairplot Arabica vs Espresso (hue Cappuccino)')    
    graphe2=snb.pairplot(data,hue='Cappuccino',vars=['Arabica','Espresso'])
    st.pyplot(graphe2.fig)
elif menu == 'Rapport':
    st.title("Rapport d'analyse Beans DataSet")
    st.write("Merci Beaucoup Mr.Benfriha ....Ton etudiant preferé <3 ...")
