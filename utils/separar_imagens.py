import streamlit as st
import cv2
import os

def listar_imagens(base_path):
    return [f for f in os.listdir(base_path) if f.endswith(('png', 'jpg', 'jpeg'))]

def main(base_path):

    if not os.path.exists(base_path):
        st.error("A pasta de imagens não existe.")
        return

    imagens = listar_imagens(base_path)
    if not imagens:
        st.error("Não foram encontradas imagens na pasta.")
        return

    if 'imagem_atual' not in st.session_state:
        st.session_state.imagem_atual = 0

    col1, col2, col3, col4, col5 = st.columns([2, 2, 2, 2, 5])

    with col1:
        if st.button("Anterior"):
            if st.session_state.imagem_atual > 0:
                st.session_state.imagem_atual -= 1

    with col2:
        if st.button("Próxima"):
            if st.session_state.imagem_atual < len(imagens) - 1:
                st.session_state.imagem_atual += 1

    with col4:
        pasta1 = st.button("Pasta 1")
    
    with col5:
        pasta2 = st.button("Pasta 2")

    st.write(f"Imagem {st.session_state.imagem_atual + 1} de {len(imagens)}")

    img_path = os.path.join(base_path, imagens[st.session_state.imagem_atual])
    image = cv2.imread(img_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    st.image(image_rgb, caption=imagens[st.session_state.imagem_atual], use_container_width=True)

    if pasta1:
        pasta1_path = os.path.join(base_path, 'pasta1')
        if not os.path.exists(pasta1_path):
            os.makedirs(pasta1_path)

        dest_path = os.path.join(pasta1_path, imagens[st.session_state.imagem_atual])
        cv2.imwrite(dest_path, image)

    if pasta2:
        pasta2_path = os.path.join(base_path, 'pasta2')
        if not os.path.exists(pasta2_path):
            os.makedirs(pasta2_path)

        dest_path = os.path.join(pasta2_path, imagens[st.session_state.imagem_atual])
        cv2.imwrite(dest_path, image)

    if pasta1:
        st.success(f"Imagem salva na Pasta 1")
    if pasta2:
        st.success(f"Imagem salva na Pasta 2")

    st.markdown(
        """
        <style>
            section[data-testid="stSidebar"] {
                width: 425px !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

if __name__ == "__main__":
    base_path = "dataset"
    main(base_path)
