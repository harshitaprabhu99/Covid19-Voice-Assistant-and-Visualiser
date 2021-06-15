import requests
import json
import pyttsx3
import speech_recognition as sr
import re
import threading
import time
import streamlit as st

API_KEY="teOJidBCBon7"
PROJECT_TOKEN="tuzXGLpYPbU6"
RUN_TOKEN="tThdNaP_v9a3"

def app():
    st.title("""
Covid-19 Voice Search Done in realtime.""")
    st.write("""The data is updated on a daily baisis. The data is collected from official website used by India.""")
    st.markdown("""
This page works like your personal assistant in speaking out to you the number of Vaccination doses given over different states in India .""")
    st.markdown("""For example you can ask it questions like "What is the nummber of first dose given in Karnataka?", "What is the total number of samples tested?",What is the number of second dose given in Delhi?", "What is number of total vaccines given in Maharashtra?" etc. Finally use the phrase "stop" to exit.""")
    
    class Data:
        def __init__(self, api_key,project_token):
            self.api_key=api_key
            self.project_token=project_token
            self.params={
                  "api_key":self.api_key
            }
            self.data=self.get_data()

        def get_data(self):
            response=requests.get(f'https://www.parsehub.com/api/v2/projects/{self.project_token}/last_ready_run/data',params=self.params)
            data=json.loads(response.text)
            return data

        def get_total_vaccines(self):
            data=self.data['total']
            for content in data:
                if content['name']=="Total Vaccination Doses":
                    return content['value']


        def get_total_samples(self):
            data=self.data['total']
            for content in data:
                if content['name']=="TOTAL SAMPLES TESTED":
                    return content['value']

        

        def get_states_data(self,vaccines):
            data=self.data['vaccines']
            for content in data:
                if content['name'].lower()==vaccines.lower():
                    return content
            return "0"
    
        def get_list_of_states(self):
            states_array=[]
            for vaccines in self.data['vaccines']:
                states_array.append(vaccines['name'].lower())
            return states_array

    

        def update_data(self):
            response=requests.get(f'https://www.parsehub.com/api/v2/projects/{self.project_token}/run',params=self.params)
        

            def poll():
                time.sleep(0.1)
                old_data=self.data
                while True:
                    new_data=self.get_data()
                    if new_data!=old_data:
                        self.data=new_data
                        print("Data updated")
                        break
                    time.sleep(5)

            

    def speak(text):
        engine=pyttsx3.init()
        engine.say(text)
        engine.runAndWait()


    def get_audio():
        r=sr.Recognizer()
        with sr.Microphone() as source:
            audio=r.listen(source)
            said=""

            try:
                said=r.recognize_google(audio)
            except Exception as e:
                st.write("Ask me something different please...", str(e))
        return said.lower()
    def main():
        st.write("started to listen.")
        data=Data(API_KEY,PROJECT_TOKEN)
        END_PHRASE="stop"
        state_list=set(data.get_list_of_states())
    
        TOTAL_PATTERNS={
        re.compile("[\w\s]+total [\w\s]+vaccines"):data.get_total_vaccines,
        re.compile("[\w\s]+total Vaccination"):data.get_total_vaccines,
        re.compile("[\w\s]+total [\w\s]+samples"):data.get_total_samples,
        re.compile("[\w\s]+total samples"):data.get_total_samples
        }
    
        STATE_PATTERNS={
        re.compile("[\w\s]+total vaccines[\w\s]+"):lambda vaccines: data.get_states_data(vaccines)['total_vaccines']
        }

    
        UPDATE_COMMAND="update"
        while True:
            st.write("Listening...")
            text=get_audio()
            st.write(text)
            result=None
            for pattern, func in STATE_PATTERNS.items():
                if pattern.match(text):
                    words=set(text.split(' '))
                    for vaccines in state_list:
                        if vaccines in words:
                            result=func(vaccines)
                            break
            for pattern, func in TOTAL_PATTERNS.items():
                if pattern.match(text):
                    result=func()
                    break
            if text==UPDATE_COMMAND:
                result="data is being updated.This may take a moment"
                data.update_data()
            if result:
                speak(result)
                st.write(result)

            if text.find(END_PHRASE)!=-1: #stop loop
                speak("Hope I was useful!")
                break 
    main()