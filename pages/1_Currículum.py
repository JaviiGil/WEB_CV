import streamlit as st

# Configurar el ancho de la página
st.set_page_config(layout="wide")

# Encabezado con foto de perfil
st.write("# Javier Gil Domínguez")
st.write("**Científico de Datos**")
st.image('foto_cv_05_2023.jpg', width=170)

# Información de contacto
st.write("**gildominguezjavier@gmail.com**")
st.write('**(+34) 692 10 90 52**')
st.write('**Madrid, España**')
st.write('[**GitHub**](https://github.com/JaviiGil)')
st.write('[**LinkedIn**](https://www.linkedin.com/in/javier-gil-dom%C3%ADnguez-753745293/)')


# Experiencia Laboral
st.write("## Experiencia Laboral")
st.write("**Viewnext Prácticas (Mayo 2024 - Junio 2024)**, Madrid: Becario")
col_11, col_22 = st.columns(2)
col_11.write("Trabajé dentro del grupo de colaboración con Vodafone en el departamento del Data Warehouse de Viewnext. Desarrollé métodos de automatización de procesos y trabajé en etapas de desarrollo de procesos reales como la creación de evidencias o la definición de universos y tablas de datos.")

# Proyectos
st.write("## Proyectos")
st.write("- **Algoritmo A estrella en el metro de Kiev**")
col_111, col_222 = st.columns(2)
col_111.write("**Objetivo**: calcular la ruta óptima para desplazarse por la ciudad de Kiev usando el metro.")
col_222.write("**Implementación**: usando conocimientos de Inteligencia Artificial sobre el lenguaje de Python.")
st.write("- **ETL en la máquina virtual triqui**")
col_111, col_222 = st.columns(2)
col_111.write("**Objetivo**: aumentar los conocimientos sobre la infraestructura de Big Data ETL.")
col_222.write("**Implementación**: usando Docker con el lenguaje Kafka.")
st.write("- **Deep Neural Network**")
col_111, col_222 = st.columns(2)
col_111.write("**Objetivo**: construcción de un modelo de red de neuronas.")
col_222.write("**Implementación**: en Jupyter Notebook en el lenguaje de Python.")
st.write("- **Wall Following Pioneer P3DX**")
col_111, col_222 = st.columns(2)
col_111.write("**Objetivo**: desarrollo de una simulación en la que se consigue que el Pioneer P3DX evite obstáculos.")
col_222.write("**Implementación**: en Coppelia Sim con el lenguaje de Python.")

# Formación
st.write("## Formación")
st.write("- **Universidad Politécnica de Madrid (2020 - 2024)**: *Grado en Ciencia de Datos e Inteligencia Artificial*")

# Competencias
st.write("## Competencias")
st.write("Capacidad de adaptación")
st.write("Ganas de aprender")
st.write("Conocimiento de herramientas: Python, AWS, Matlab, MongoDB, OpenCV, MySQL, Coppelia Sim")

# Idiomas
st.write("## Idiomas")
st.write("**Español:** Nativo")
st.write("**Catalán:** Nativo")
st.write("**Inglés:** C1 (Cambridge)")
st.write("**Francés:** B2")
st.write("**Alemán:** A2")

# Descargar CV
st.write("## Conóceme más:")
with open("CV.pdf", "rb") as pdf_file:
    cv_tradicional = pdf_file.read()

with open("CV_Infografico.pdf", "rb") as pdf_file:
    cv_infografico = pdf_file.read()

st.download_button("Descargar CV Tradicional", data=cv_tradicional, file_name= 'CV.pdf', mime='pdf')
st.download_button("Descargar CV Infográfico", data=cv_infografico, file_name= 'CV Infografico.pdf', mime='pdf')
st.link_button("Vídeo Currículum", "https://drive.google.com/drive/u/0/home")