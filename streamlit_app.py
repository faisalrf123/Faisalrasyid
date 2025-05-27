import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

st.image("17477052906911695653576004249561.jpg", width=200) 

st.title("Sman 20 Bandung") 
st.header("Aplikasi Mengecek Nilai Genap/Ganjil") 
angka = st.number_input("tulis sebuah angka:", value=0, step=1) 

if (angka % 2) ==0:
 st.write(f"{angka} adalah Bilangan Genap") 
else:
 st.write(f"{angka}adalah Bilangan Ganjil") 
