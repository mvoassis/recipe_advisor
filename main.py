import streamlit as st
from PIL import Image
import io

import predictor
from predictor import *

st.set_page_config(layout="wide")


def main():
    key = st.secrets["GEMINI_KEY"]
    head1, head2, head3 = st.columns([3, 2, 11], vertical_alignment="bottom")
    with head1:
        st.image("files/robo.png", width = 250)
    with head2:
        st.image("files/logo-simplificai.png", width=120)
    with head3:
        st.title(":violet[RECEITA BOT]" )
        st.subheader("O seu ajudante virtual para criar receitas! ")


    col1, col2 = st.columns([2, 2])

    with col1:
        st.header("Faça upload de uma foto")
        uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            imagem_pil = Image.open(io.BytesIO(uploaded_file.read()))
            st.image(imagem_pil, caption='Imagem enviada', use_column_width=True)

        if uploaded_file is not None:
            with st.spinner('O Receita Bot está dando uma olhada...'):
                if st.button('Detectar Ingredientes'):
                    st.session_state.ingredientes_detectados = predictor.get_ingredients(imagem_pil, key)
                    st.session_state.receitas = get_possible_recipes(st.session_state.ingredientes_detectados.split(','), key)

        if 'ingredientes_detectados' in st.session_state:
            st.write(f":violet[Ingredientes detectados:] {st.session_state.ingredientes_detectados.split(',')}")
            st.write(":violet[Receitas possíveis:]")
            for i, receita in enumerate(st.session_state.receitas.split(',')):
                st.write(f"{i+1}. {receita}")

    with col2:
        st.header("Escolha uma Receita")
        if 'receitas' in st.session_state:
            receita_selecionada = st.selectbox("", st.session_state.receitas.split(','))
            with st.spinner('O Receita Bot está criando a receita...'):
                if st.button('Ver Receita'):
                    print(st.session_state.ingredientes_detectados.split(','))
                    receita_full = get_full_recipes(st.session_state.ingredientes_detectados.split(','), receita_selecionada, key)
                    st.write(receita_full)

if __name__ == "__main__":
    main()
