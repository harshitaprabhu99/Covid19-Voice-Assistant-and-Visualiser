import requests
import json
import pyttsx3
import speech_recognition as sr
import re
import threading
import time
import streamlit as st

API_KEY="teOJidBCBon7"
PROJECT_TOKEN="t-EjNbhT5Gza"
RUN_TOKEN="tt8heBYjdpqY"

def app():
    st.title("""
Covid-19 Voice Search Done in realtime just for you.""")
    st.write("""The data is updated on a daily baisis. The data is collected from Official website used by India.""""")
    st.markdown("""
This page works like your personal assistant in speaking out to you the Coronavirus Cases in India. For example you can just ask it questions like "What is the number of covid cases in Maharashtra?", "What is the number of confirmed cases in Karnataka?", "What is number of recovered cases in Delhi?", "What is the number of deaths in Maharashtra?" etc. Finally use the phrase "stop" to exit. 
""")

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

        def get_total_cases(self):
            data=self.data['total']
            for content in data:
                if content['name']=="Active Cases:":
                    return content['value']


        def get_total_deaths(self):
            data=self.data['total']
            for content in data:
                if content['name']=="Deaths:":
                    return content['value']

        def get_total_recovered(self):
            data=self.data['total']
            for content in data:
                if content['name']=="Cured/Discharged:":
                    return content['value'] 

        def get_states_data(self,states):
            data=self.data['states']
            for content in data:
                if content['name'].lower()==states.lower():
                    return content
            return "0"
    
        def get_list_of_states(self):
            states_array=[]
            for states in self.data['states']:
                states_array.append(states['name'].lower())
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
        re.compile("[\w\s]+total [\w\s]+cases"):data.get_total_cases,
        re.compile("[\w\s]+total cases"):data.get_total_cases,
        re.compile("[\w\s]+total [\w\s]+deaths"):data.get_total_deaths,
        re.compile("[\w\s]+total deaths"):data.get_total_deaths,
        re.compile("[\w\s]+total [\w\s]+recovered"):data.get_total_recovered,
        re.compile("[\w\s]+total recovered"):data.get_total_recovered
        }
    
        STATE_PATTERNS={
        re.compile("[\w\s]+cases[\w\s]+"):lambda states :data.get_states_data(states)['total_confirmed'],
        re.compile("[\w\s]+deaths[\w\s]+"):lambda states: data.get_states_data(states)['total_deaths'],
            re.compile("[\w\s]+recovered[\w\s]+"):lambda states: data.get_states_data(states)['total_recovered']
            
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
                    for states in state_list:
                        if states in words:
                            result=func(states)
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