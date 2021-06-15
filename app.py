import streamlit as st
from multiapp import MultiApp
from apps import home, finalyearcode, covidprojectss, states, districts, city, analysis # import your app modules here
from PIL import Image
app = MultiApp()
st.title('Covid-19 Voice Assistant and Visualizer')
img = Image.open("C:/Users/Harshita/AppData/Local/Programs/Python/Python39/multi-page-app/apps/covid19.jpg")
st.image(img,width=750,)

st.markdown('Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus. Most people infected with the COVID-19 virus will experience mild to moderate respiratory illness. Hence it is required to wear masks and keep ourseleves sanitized.')
# Add all your application here
app.add_app("Home", home.app)
app.add_app("Voice Search Worldwide Cases", finalyearcode.app)
app.add_app("Voice Search India State wise Cases", states.app)
app.add_app("Voice Search Karanataka City wise Cases", city.app)
app.add_app("Voice Search District wise Cases", districts.app)
app.add_app("Visualise Covid Cases Worldwide and India", covidprojectss.app)
app.add_app("Visualise Covid Cases in Karanataka", analysis.app)


# The main app
app.run()