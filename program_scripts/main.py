import streamlit as st
import utils

st.markdown(utils.title_style, unsafe_allow_html=True)

name_input = st.text_input('Nome', '?')

course = st.selectbox(
    'Curso',
    utils.course_options)

year = st.radio(
    "Ano",
    ["1°", "2°", "3°"])

st.markdown(utils.declaration_style, unsafe_allow_html=True)
st.markdown(f"<span style='font-size:20px'>Eu <b>{name_input}</b>, aluno do <b>{year}</b> ano do curso de <b>{course}</b>, aceito ser cadastrado no banco de dados deste trabalho.</span>", unsafe_allow_html=True)
if st.button('Salvar'):
    utils.save_student(name_input, year, course)