import ai21
import time
import playsound
from gtts import gTTS
import os
import streamlit as st

ai21.api_key = '6NfBFYWVvcxXYmzZozNQWDkmPeeAC2Vf'
st.text_input("let's start : what art piece are you looking for? ", key="art_piece")
st.text_input("how many minutes do you want to spend on it?", key="audio_lenght")
print('retrieving answer')

if ((st.session_state.art_piece == "")  | (st.session_state.audio_lenght == "")): 
    st.stop()
else : 
    text = ai21.Completion.execute(
        model="j2-ultra",
        prompt="""Context: you're an art expert and will describe all the details of a painting. You will also describe the history of the artist, when he made the paintings, the historical period. You will also give other similar painting he made
        Question: """+ st.session_state.art_piece +"""?
        Answer:""",
        numResults=1,
        maxTokens=(float(st.session_state.audio_lenght)*60*1.75),
        temperature=0,
        topKReturn=0
    )
    # The text that you want to convert to audio
    mytext = text['completions'][0]['data']['text']

    # Language in which you want to convert
    language = 'en'
    print('creating mp3 file')
    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed
    myobj = gTTS(text=mytext, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome 
    myobj.save("welcome.mp3")

    print('starting to play')
    # wait for the sound to finish playing?
    st.audio("welcome.mp3")
