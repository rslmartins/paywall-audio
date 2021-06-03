import streamlit as st
import nltk
from newspaper import Article
nltk.download('punkt')
from langdetect import detect
import datetime
from gtts import gTTS

st.title("Outline")

web_page = st.text_input(label='Read & annotate without distractions')
if st.button("Create Outline"):
#	web_page = 'https://oglobo.globo.com/opiniao/a-anarquia-militar-de-bolsonaro-25043771'
	article=Article(web_page)
	article.download()
	article.parse()
	article.nlp()

	tts = gTTS(text = article.text, lang = detect(article.text))
	filename = str(datetime.datetime.now())+'.mp3'
	tts.save(filename)
	audio_file = open(filename, 'rb')
	audio_bytes = audio_file.read()
	st.audio(audio_bytes, format='audio/mp3')

	st.success(article.text)
