import streamlit as st
import pandas as pd
import numpy as np

st.title(" Tableau de Bord - Prédiction de Stocks")

# 1. Simulation de la base de données (Historique des ventes)
@st.cache_data
def charger_donnees():
    dates = pd.date_range(start="2026-01-01", periods=100)
    # Ventes aléatoires entre 10 et 50 par jour
    ventes = np.random.randint(10, 50, size=100)
    df = pd.DataFrame({"Date": dates, "Ventes": ventes})
    return df

df = charger_donnees()

st.subheader(" Historique des ventes (Derniers jours)")
st.dataframe(df.tail())

# 2. Algorithme de prédiction (Moyenne mobile sur 7 jours)
df['Prédiction (Tendance)'] = df['Ventes'].rolling(window=7).mean()

st.subheader("Courbe des ventes et Prédictions")
st.line_chart(df.set_index('Date')[['Ventes', 'Prédiction (Tendance)']])

# 3. Génération de la recommandation de commande
derniere_prediction = df['Prédiction (Tendance)'].iloc[-1]
stock_actuel = 15
commande_recommandee = max(0, int(derniere_prediction * 7) - stock_actuel) # Prévision pour 7 jours

st.subheader("Recommandation Automatique")
st.warning(f"Stock actuel : {stock_actuel} unités")
st.success(f"Action requise : Commander {commande_recommandee} unités pour éviter la rupture cette semaine.")