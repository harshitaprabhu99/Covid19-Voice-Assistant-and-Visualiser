import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from PIL import Image


def app():
  
  st.title("COVID-19 DASHBOARD")
  st.markdown('The dashboard will help you visualize the Covid-19 Situation across the globe')
  
  st.sidebar.title("Visualization Selector")
  st.sidebar.markdown("Select the Charts/Plots accordingly:")


  df = pd.read_csv("C:/Users/Harshita/AppData/Local/Programs/Python/Python39/multi-page-app/apps/covid dataset.csv")

  select = st.sidebar.selectbox('Visualization type', ['Bar plot'], key='1')
  if not st.sidebar.checkbox("Hide", True, key='1'):
   if select=='Bar plot':
             st.title("Country wise Total Cases and Total Deaths")
             fig = go.Figure(data=[
          go.Bar(name='Deaths', x=df['country_name'][:10], y=df['country_total_deaths'][:10]),
          go.Bar(name='Total', x=df['country_name'][:10], y=df['country_total_cases'][:10]),
          go.Bar(name='Recovered', x=df['country_name'][:10], y=df['country_total_recovered'][:10])])
             st.plotly_chart(fig)



  df2 = pd.read_csv("C:/Users/Harshita/AppData/Local/Programs/Python/Python39/multi-page-app/apps/covid dataset.csv")
  select1 = st.sidebar.selectbox('Select', ['Death', 'total','Recovered'], key='3')
  if not st.sidebar.checkbox("Hide", True, key='3'):
    if select1 == 'Death':
      fig = px.line(df2, x="country_name", y="country_total_deaths")
      st.plotly_chart(fig)
    elif select1 == 'total':
      fig = px.line(df2, x="country_name", y="country_total_cases")
      st.plotly_chart(fig)
    elif select1=='Recovered':
      fig=px.line(df2,x="country_name",y="country_total_recovered")
      st.plotly_chart(fig)



  df = pd.read_csv("C:/Users/Harshita/AppData/Local/Programs/Python/Python39/multi-page-app/apps/state_level_latest.csv")

  select = st.sidebar.selectbox('Visualization type', ['Bar plot'], key='4')
  if not st.sidebar.checkbox("Hide", True, key='5'):
   if select=='Bar plot':
             st.title("State wise Confirmed cases, Recovered cases and Death cases")
             fig = go.Figure(data=[
          go.Bar(name='Confirmed', x=df['State'][:10], y=df['Confirmed'][:10]),
          go.Bar(name='Recovered', x=df['State'][:10], y=df['Recovered'][:10]),
          go.Bar(name='Deaths', x=df['State'][:10], y=df['Deaths'][:10])])
             st.plotly_chart(fig)
                   


  df2 = pd.read_csv("C:/Users/Harshita/AppData/Local/Programs/Python/Python39/multi-page-app/apps/state_level_latest.csv")
  select1 = st.sidebar.selectbox('Select', ['Confirmed', 'Recovered','Deaths'], key='6')
  if not st.sidebar.checkbox("Hide", True, key='7'):
    if select1 == 'Confirmed':
      fig = px.line(df2, x="State", y="Confirmed")
      st.plotly_chart(fig)
    elif select1 == 'Recovered':
      fig = px.line(df2, x="State", y="Recovered")
      st.plotly_chart(fig)
    elif select1=='Deaths':
      fig=px.line(df2,x="State",y="Deaths")
      st.plotly_chart(fig)



  df2 = pd.read_csv("C:/Users/Harshita/AppData/Local/Programs/Python/Python39/multi-page-app/apps/State wise ratio.csv")
  select = st.sidebar.selectbox('Visualization type', ['state ratios'], key='8')
  if not st.sidebar.checkbox("Hide", True, key='9'):
    if select=='state ratios':
      st.title("State wise cases in ratio")
      fig = go.Figure(data=[
          go.Bar(name='active', x=df2['states_name'][:10], y=df2['states_active_ratio'][:10]),
          go.Bar(name='discharged', x=df2['states_name'][:10], y=df2['states_discharged_ratio'][:10]),
          go.Bar(name='death', x=df2['states_name'][:10], y=df2['states_death_ratio'][:10])])
      st.plotly_chart(fig)


  df2 = pd.read_csv("C:/Users/Harshita/AppData/Local/Programs/Python/Python39/multi-page-app/apps/State wise ratio.csv")
  select1 = st.sidebar.selectbox('Select', ['active', 'discharged','Deaths'], key='10')
  if not st.sidebar.checkbox("Hide", True, key='11'):
    if select1 == 'active':
      fig = px.line(df2, x="states_name", y="states_active_ratio")
      st.plotly_chart(fig)
    elif select1 == 'discharged':
      fig = px.line(df2, x="states_name", y="states_discharged_ratio")
      st.plotly_chart(fig)
    elif select1=='Deaths':
      fig=px.line(df2,x="states_name",y="states_death_ratio")
      st.plotly_chart(fig)
