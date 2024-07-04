import streamlit as st

# Configurar el ancho de la página
# st.set_page_config(layout="wide")


# # Añadir el fondo de pantalla usando CSS

# page_element = """
# <style>
# [data-testid="stAppViewContainer"] {
#   background-image: url("https://digitalpm.es/wp-content/uploads/2017/11/3881153-big-data-wallpaper.jpg");
#   background-size: cover;
#   background-attachment: fixed;
# }
# .content-box {
#   background-color: rgba(255, 255, 255, 0.8);
#   padding: 20px;
#   border-radius: 10px;
#   box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
#   margin: 20px;
# }
# </style>
# """

# st.markdown(page_element, unsafe_allow_html=True)
# st.markdown('<div class="content-box">', unsafe_allow_html=True)

# Encabezado con foto de perfil
st.title('Javier Gil Domínguez')
st.write("**Científico de Datos**")
st.image('foto_cv_05_2023.jpg', width=170)

# Información de contacto
st.write("**gildominguezjavier@gmail.com**")
st.write('**(+34) 692 10 90 52**')
st.write('**Madrid, España**')
st.write('[**GitHub**](https://github.com/JaviiGil)')
st.write('[**LinkedIn**](https://www.linkedin.com/in/javier-gil-dom%C3%ADnguez-753745293/)')


st.write("## Sobre Mi")
st.write('Soy estudiante del último curso en el grado de Ciencia de Datos e Inteligencia Artificial. Estoy interesado en poner en práctica los conocimientos teóricos que he adquirido. Me gustaría colaborar con una compañía donde pudiera aprender y, asimismo, ayudar a desarrollar este campo.')
st.write('Durante estos últimos cuatro meses, he ralizado un periodo de prácticas en la empresa de consultoría tecnológica Viewnext. Aquí, he tenido la oportunidad de aplicar mis conocimientos en proyectos reales, fortaleciendo mis competencias técnicas y aprendiendo a trabajar en un entorno profesional.')
st.write('Me considero una persona responsable, social, organizada y sobre todo con muchas ganas de aprender en esta primera etapa laboral de mi vida.')

st.write("\n")
st.write("\n")
st.write("## Carta de Motivación Amazon Student Program")
with open("CartaPresentacion.pdf", "rb") as pdf_file:
    carta_presentacion = pdf_file.read()
st.download_button("Descargar Carta de Presentacion", data=carta_presentacion, file_name='Carta de Presentacion.pdf', mime='application/pdf')

# Contacto
st.markdown('<div class="contact-me">', unsafe_allow_html=True)
st.markdown('<div class="section-title">📨 Contacta conmigo!</div>', unsafe_allow_html=True)

contact_form = """
<style>
form {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.1);
}
input, textarea, button {
    width: 100%;
    padding: 12px;
    margin-bottom: 10px;
    border: 1px solid #ddd;
    border-radius: 10px;
}
input:focus, textarea:focus {
    border-color: #6a1b9a;
    outline: none;
}
button {
    background-color: #6a1b9a;
    color: white;
    border: none;
    cursor: pointer;
    transition: background-color 0.3s;
}
button:hover {
    background-color: #4a148c;
}
</style>
<form action="https://formsubmit.co/nicovegamunoz1@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Tu nombre" required>
    <input type="email" name="email" placeholder="Tu email" required>
    <textarea name="message" placeholder="Tu mensaje aquí" required></textarea>
    <button type="submit">Enviar</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
