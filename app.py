import streamlit as st 

#-------------------------------------------------------------------------------------------------------------------------
st.sidebar.title("calculadora de IMC")
st.sidebar.image("logo_imc.png")

#----------------------------------------------------------------------------------------------------------------------------
st.title("calculadora de IMC")


peso = st.text_input("Digite o seu pesso: ")
altura = st.text_input("Digite a sua altura: ")

if st.button("calcular"):
    peso = float(peso)
    altura = float(altura)

    imc = peso / (altura ** 2)

    if imc < 18.5:
        class_imc = "abaixo_peso"
        st.warning(F"seu IMC é {imc:.1f}! você esta abaixo do peso! 🩻")

    elif imc < 24.9:
        class_imc = "peso_normal"
        st.success(f"seu IMC é {imc:.1f}! vovê esta com o pessp saldadvel parabens 👍 ")

    elif imc < 29.9:
        class_imc = "sobrepeso"
        st.warning(f"seu IMC é {imc:.1f} você esta com sobre peso! 🫤")
        
    elif imc < 34.9:
        class_imc = "obesidade1"
        st.warning(f"seu IMC é {imc:.1f} você esta com obesidade grau 1 !!!!!!!!!!!!!!!!!!!! 🫤")  
    elif imc < 39.9:
        class_imc = "obesidade2"
        st.error(f"seu IMC é {imc:.1f} você esta com obesidade grau 2 !!!!!!!!!!!!!!!!!!!! 😱")  

    else:
        class_imc = "obesidade3"
        st.error(f"seu IMC é {imc:.1f} você esta com obesidade grau 3  😱!!!!!!!!!!!!!!")  

    st.markdown("---")
    st.image(f"{class_imc}.png")


    with open(f"{class_imc}.txt", "r", encoding="utf-8") as f:
        texto = f.read()

        st.markdown(texto)
