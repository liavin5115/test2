import streamlit as st
from gtts import gTTS
import docx2txt
import PyPDF2
from translate import Translator

#define fungsi
def text_to_speech(text, language="id"):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("output.mp3")
    st.audio("output.mp3")

# Mappings for language options
language_mappings = {
    "Bahasa Inggris": "en",
    "Indonesia": "id",
    "Mandarin Tradisional": "zh-TW",
    "Italia": "it",
    "Belanda": "nl",
    "Mandarin China": "zh-CN"
}

#user interface
st.title("Merubah Tulisan ke Suara dengan Terjemahan")
option = st.radio("Pilih opsi:", ("Masukkan Teks", "Unggah File Word", "Unggah File PDF"))

if option == "Masukkan Teks":
    text = st.text_input("Silahkan masukkan teks")
    from_language = st.selectbox("Pilih bahasa sumber:", list(language_mappings.keys()))
    to_language = st.selectbox("Pilih bahasa tujuan:", list(language_mappings.keys()))
    translator = Translator(to_lang=language_mappings[to_language], from_lang=language_mappings[from_language])
    translated_text = translator.translate(text)
    if st.button("Mainkan"):
        text_to_speech(translated_text, language_mappings[to_language])
elif option == "Unggah File Word":
    uploaded_file = st.file_uploader("Unggah file Word (.docx)", type=["docx"])
    if uploaded_file is not None:
        text = docx2txt.process(uploaded_file)
        from_language = st.selectbox("Pilih bahasa sumber:", list(language_mappings.keys()))
        to_language = st.selectbox("Pilih bahasa tujuan:", list(language_mappings.keys()))
        translator = Translator(to_lang=language_mappings[to_language], from_lang=language_mappings[from_language])
        translated_text = translator.translate(text)
        if st.button("Mainkan"):
            text_to_speech(translated_text, language_mappings[to_language])
elif option == "Unggah File PDF":
    uploaded_file = st.file_uploader("Unggah file PDF (.pdf)", type=["pdf"])
    if uploaded_file is not None:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        from_language = st.selectbox("Pilih bahasa sumber:", list(language_mappings.keys()))
        to_language = st.selectbox("Pilih bahasa tujuan:", list(language_mappings.keys()))
        translator = Translator(to_lang=language_mappings[to_language], from_lang=language_mappings[from_language])
        translated_text = translator.translate(text)
        if st.button("Mainkan"):
            text_to_speech(translated_text, language_mappings[to_language])