import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from PIL import Image


def app():
  st.title("COVID-19 DATA ANALYSIS")
  st.markdown('The dashboard will help you visualize the Covid-19 Situation across people of various age groups,gender,districts etc.')
  
  st.sidebar.title("Visualization Selector")
  st.sidebar.markdown("Select the Charts/Plots accordingly:")

  df = pd.read_csv("C:/Users/Harshita/AppData/Local/Programs/Python/Python39/multi-page-app/apps/gender-wise-cases.csv")
  select = st.sidebar.selectbox('Visualization type', ['Bar plot'], key='1')
  if not st.sidebar.checkbox("Hide", True, key='1'):
    if select=='Bar plot':
      st.title("CASES ON BASIS OF GENDER")
      fig = go.Figure(data=[
        go.Bar(name='Gender', x=df['Category'][:15], y=df['Series 1'][:15])] )
      st.plotly_chart(fig)



  df = pd.read_csv("C:/Users/Harshita/AppData/Local/Programs/Python/Python39/multi-page-app/apps/number-of-covid-positive.csv")
  select2 = st.sidebar.selectbox('Select', ['Age'], key='12')
  if not st.sidebar.checkbox("Hide", True, key='13'):
    if select2 == 'Age':
      st.title("Covid cases based on age group")
      fig = px.area(df, x="Category", y="Number of Cases")
      st.plotly_chart(fig)


  df = pd.read_csv("C:/Users/Harshita/AppData/Local/Programs/Python/Python39/multi-page-app/apps/district-wise-patients-w.csv")
  select2 = st.sidebar.selectbox('Select', ['District wise'], key='14')
  if not st.sidebar.checkbox("Hide", True, key='15'):
    if select2 == 'District wise':
      st.title("District wise covid cases")
      fig = px.area(df, x="Category", y="Number of Cases")
      st.plotly_chart(fig)


  


  df = pd.read_csv("C:/Users/Harshita/AppData/Local/Programs/Python/Python39/multi-page-app/apps/districts_covid.csv")
  select = st.sidebar.selectbox('Visualization type', ['covid positive'], key='18')
  if not st.sidebar.checkbox("Hide", True, key='19'):
    if select=='covid positive':
      st.title("Number of covid positive")
      fig = go.Figure(data=[
          go.Bar(name='Deaths', x=df['districts_name'][:20], y=df['districts_total_cases'][:20]),
          go.Bar(name='Total', x=df['districts_name'][:20], y=df['districts_total_recovered'][:20]),
          go.Bar(name='Recovered', x=df['districts_name'][:20], y=df['districts_total_deaths'][:20])])
      st.plotly_chart(fig)

  
  


  df = pd.read_csv("C:/Users/Harshita/AppData/Local/Programs/Python/Python39/multi-page-app/apps/districts_covid.csv")
  select = st.sidebar.selectbox('Visualization type', ['recovered district wise'], key='22')
  if not st.sidebar.checkbox("Hide", True, key='23'):
    if select=='recovered district wise':
      st.title("Total recovered covid cases in districts")
      fig = px.area(df, x="districts_name", y="districts_total_recovered")
      st.plotly_chart(fig)

  
  df = pd.read_csv("C:/Users/Harshita/AppData/Local/Programs/Python/Python39/multi-page-app/apps/districts_covid.csv")
  select = st.sidebar.selectbox('Visualization type', ['deaths district wise'], key='24')
  if not st.sidebar.checkbox("Hide", True, key='25'):
    if select=='deaths district wise':
      st.title("Total deaths covid cases in districts")
      fig = px.area(df, x="districts_name", y="districts_total_deaths")
      st.plotly_chart(fig)


  df = pd.read_csv("C:/Users/Harshita/AppData/Local/Programs/Python/Python39/multi-page-app/apps/districts_covid.csv")
  select = st.sidebar.selectbox('Visualization type', ['active district wise'], key='26')
  if not st.sidebar.checkbox("Hide", True, key='27'):
    if select=='active district wise':
      st.title("Total active covid cases in districts")
      fig = px.area(df, x="districts_name", y="districts_active_cases")
      st.plotly_chart(fig)

  

  df = pd.read_csv("C:/Users/Harshita/AppData/Local/Programs/Python/Python39/multi-page-app/apps/transmission-type-total.csv")
  select = st.sidebar.selectbox('Visualization type', ['transmission'], key='28')
  if not st.sidebar.checkbox("Hide", True, key='29'):
    if select=='transmission':
      st.title("Type of Transmissions")
      fig = px.area(df, x="Category", y="Series 1")
      st.plotly_chart(fig)



  df = pd.read_csv("C:/Users/Harshita/AppData/Local/Programs/Python/Python39/multi-page-app/apps/district-wise-symptomati.csv")
  select = st.sidebar.selectbox('Visualization type', ['district wise symptamatic'], key='32')
  if not st.sidebar.checkbox("Hide", True, key='33'):
    if select=='district wise symptamatic':
      st.title("District wise people symptomatic")
      fig = px.area(df, x="Category", y="Symptomatic")
      st.plotly_chart(fig)


  df = pd.read_csv("C:/Users/Harshita/AppData/Local/Programs/Python/Python39/multi-page-app/apps/district-wise-symptomati.csv")
  select = st.sidebar.selectbox('Visualization type', ['district wise asymptamatic'], key='34')
  if not st.sidebar.checkbox("Hide", True, key='35'):
    if select=='district wise asymptamatic':
      st.title("District wise people asymptomatic")
      fig = px.area(df, x="Category", y="Asymptomatic")
      st.plotly_chart(fig)
