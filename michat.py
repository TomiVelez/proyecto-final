import streamlit as st
from groq import Groq
st.set_page_config(page_title="Mi chat de IA", page_icon="👍")
st.title("Mi primera aplicacion con Streamlit")

nombre = st.text_input("Cual es tu nombre?")
if st.button("Saludar!"):
    st.write(f"Hola {nombre}! Bienvenido a talento tech")

MODELOS = ['llama3-8b-8192', 'llama3-70b-8192', 'mixtral-8x7b-32768']

def configurar_pagina():
    st.title("Mi Chat de IA")
    st.sidebar.title("Configuracion de la IA")

    elegirModelo = st.sidebar.selectbox(
        "Elegi un modelo",
        options = MODELOS,
        index = 0
    )

    return elegirModelo
def crear_usuario_groq():
   clave_secreta = st.secrets["CLAVE_API"]
   return Groq(api_key=clave_secreta)

def configurar_modelo(cliente, modelo, mensajeDeEntrada):
    return cliente.chat.completions.create(
        model = modelo,
        messages = [{"role":"user", "content": mensajeDeEntrada}],
        stream = False
    )

def inicializar_estado():
    if "mensajes" not in st.session_state:
        st.session_state.mensajes = []
def actualizar_historial(rol, contenido, avatar):
    st.session_state.mensajes.append({"role": rol, "content": contenido, "avatar": avatar})

def mostrar_historial():
    for mensaje in st.session_state.mensajes:
        with st.chat_message(mensaje["role"], avatar= mensaje["avatar"]) : st.markdown(mensaje["content"])

def area_chat():
    contenedorDelChat = st.container(height=400, border= True)
    with contenedorDelChat: mostrar_historial()


clienteUsuario = crear_usuario_groq()
inicializar_estado()
area_chat()
modelo = configurar_pagina()
mensaje = st.chat_input("Escribi tu mensaje:")
if mensaje:
    actualizar_historial("user", mensaje, "😁")
    chat_completo = configurar_modelo(clienteUsuario, modelo, mensaje)
    actualizar_historial("assistant", chat_completo, "🤖")
    st.rerun()


if mensaje:
    configurar_modelo(clienteUsuario, modelo, mensaje)
    print(mensaje)



modelo = configurar_pagina()
mensaje = st.chat_input("Escribi tu mensaje")
st.set_page_config("Tu propio chatbot")
st.title("Tu primer chat de Streamlit")
st.sidebar.title("Mi chat del cole")
