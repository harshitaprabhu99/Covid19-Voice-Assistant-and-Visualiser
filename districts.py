import requests
import json
import pyttsx3
import speech_recognition as sr
import re
import threading
import time
import streamlit as st

API_KEY="teOJidBCBon7"
PROJECT_TOKEN="tFiBHTCSbt5-"
RUN_TOKEN="tVrKSUUajfwc"

def app():
    st.title("""
Covid-19 Voice Search Done in realtime just for you.""")
    st.markdown("""The data is updated on a daily baisis. The data is collected from Karnataka's official Covid 19 report website.""")
    st.markdown("""
This page works like your personal assistant in speaking out to you the Coronavirus Cases in Karnataka. For example you can just ask it questions like "What is the number of covid cases in Mysuru?", "What is the number of active cases in Udupi?", "What is number of recovered cases in Shimoga?", "What is the number of deaths in Hassan?" etc. Finally use the phrase "stop" to exit. 
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

        def get_dk_cases(self):
            data=self.data['total']
            for content in data:
                if content['name']=="Dakshina Kannada":
                    return content['value']


        def get_uk_cases(self):
            data=self.data['total']
            for content in data:
                if content['name']=="Uttara Kannada":
                    return content['value']

        def get_bu_cases(self):
            data=self.data['total']
            for content in data:
                if content['name']=="Bangalore Urban":
                    return content['value'] 

        def get_br_cases(self):
            data=self.data['total']
            for content in data:
                if content['name']=="Bangalore Rural":
                    return content['value']

        def get_districts_data(self,districts):
            data=self.data['districts']
            for content in data:
                if content['name'].lower()==districts.lower():
                    return content
            return "0"
        
    
        def get_list_of_districts(self):
            districts_array=[]
            for districts in self.data['districts']:
                districts_array.append(districts['name'].lower())
            return districts_array

    

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
        districts_list=set(data.get_list_of_districts())
    
        TOTAL_PATTERNS={
        re.compile("[\w\s]+DakshinaKannada [\w\s]+"):data.get_dk_cases,
        re.compile("[\w\s]+Uttara Kannada [\w\s]+"):data.get_uk_cases,
        re.compile("[\w\s]+Bangalore Urban [\w\s]+"):data.get_bu_cases,
        re.compile("[\w\s]+Bangalore Rural"):data.get_br_cases
        }
    
        DISTRICTS_PATTERNS={
        re.compile("[\w\s]+cases[\w\s]+"):lambda districts :data.get_districts_data(districts)['total_cases'],
        re.compile("[\w\s]+recovered[\w\s]+"):lambda districts: data.get_districts_data(districts)['total_recovered'],
        re.compile("[\w\s]+active[\w\s]+"):lambda districts: data.get_districts_data(districts)['active_cases'],
        re.compile("[\w\s]+deaths[\w\s]+"):lambda districts: data.get_districts_data(districts)['total_deaths']
            
        }

    
        UPDATE_COMMAND="update"
        while True:
            st.write("Listening...")
            text=get_audio()
            st.write(text)
            result=None
            for pattern, func in DISTRICTS_PATTERNS.items():
                if pattern.match(text):
                    words=set(text.split(' '))
                    for districts in districts_list:
                        if districts in words:
                            result=func(districts)
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