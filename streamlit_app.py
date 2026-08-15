import streamlit as st
import random
import time
from gtts import gTTS
import os
from io import BytesIO

st.set_page_config(page_title="CEREBRO RABINO 👑", page_icon="🧠", layout="centered")

st.title("🧠 CEREBRO RABINO")
st.subheader("Mutación + Clonación + Voz + Beats + Letras")

# MENU
menu = st.sidebar.selectbox("Elige una función",
    ["Generar Letras", "Mutar Letra", "Clonar Estilo", "Grabar Voz", "Generar Beat"])

# 1. GENERAR LETRAS
if menu == "Generar Letras":
    st.header("✍️ Generador de Letras")
    tema = st.text_input("¿De qué quieres la letra?", "Fe y superación")
    estilo = st.selectbox("Estilo", ["Rap Cristiano", "Trap", "Dembow", "Reggaeton"])
    if st.button("Crear Letra"):
        with st.spinner("CEREBRO pensando..."):
            time.sleep(2)
            letra = f"""[Intro]
Yo soy {tema}
Con Dios por delante

[Verso 1]
Luchando día a día {estilo} en la mente
No me rindo aunque la cosa esté caliente
RABINO en la casa, palabra diferente
Subiendo pa' arriba, siempre pa' la gente

[Coro]
Dale que se puede, dale que se logra
Con fe y con fuerza nada nos derrota"""
            st.text_area("Tu Letra:", letra, height=300)

# 2. MUTACIÓN
if menu == "Mutar Letra":
    st.header("🧬 Mutación de Letra")
    letra_original = st.text_area("Pega tu letra aquí")
    if st.button("Mutar"):
        palabras = ["fuego", "level", "rey", "luz", "bendición", "corona"]
        letra_mutada = letra_original
        for _ in range(3):
            letra_mutada = letra_mutada.replace(random.choice(letra_mutada.split()), random.choice(palabras))
        st.success("Letra Mutada:")
        st.text_area("", letra_mutada, height=300)

# 3. CLONACIÓN
if menu == "Clonar Estilo":
    st.header("🎭 Clonación de Estilo")
    artista = st.selectbox("¿A quién quieres clonar?", ["Redimi2", "Alejandro Alonso", "Funky", "Emanuel"])
    tema_clone = st.text_input("Tema")
    if st.button("Clonar Estilo"):
        st.info(f"Clonando estilo de {artista}...")
        st.text_area("Resultado:", f"[Estilo {artista}]\nHablando de {tema_clone}\nCon barras y flow profético\nDios en el centro, eso es lo único", height=200)

# 4. GRABACIÓN DE VOZ
if menu == "Grabar Voz":
    st.header("🎙️ Grabar Voz con TTS")
    texto_voz = st.text_area("Escribe lo que quieres que CEREBRO diga")
    if st.button("Convertir a Voz"):
        tts = gTTS(texto_voz, lang='es')
        fp = BytesIO()
        tts.write_to_fp(fp)
        st.audio(fp.getvalue(), format="audio/mp3")
        st.success("Listo! Dale play")

# 5. BEATS
if menu == "Generar Beat":
    st.header("🥁 Generador de Beats")
    bpm = st.slider("BPM", 70, 140, 90)
    tipo = st.selectbox("Tipo de Beat", ["Boom Bap", "Trap", "Dembow"])
    if st.button("Crear Beat"):
        st.warning("Para beats reales necesitamos instalar librerías. Por ahora te dejo la estructura:")
        st.code(f"Beat {tipo} a {bpm} BPM\nKick - - - -\nSnare - - Clap -")
