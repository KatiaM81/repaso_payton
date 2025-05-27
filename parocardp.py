# archivo: rcp_cuestionario.py
import streamlit as st

st.set_page_config(page_title="Cuestionario RCP", layout="centered")

st.title("🩺 Cuestionario de Reanimación Cardiopulmonar (RCP)")
st.write("Responde las siguientes 10 preguntas seleccionando la alternativa correcta.")

# Lista de preguntas
preguntas = [
    {
        "pregunta": "¿Cuál es el primer paso al encontrar a una persona inconsciente?",
        "opciones": ["Llamar a emergencias", "Verificar si responde", "Iniciar RCP", "Buscar ayuda"],
        "respuesta": "Verificar si responde"
    },
    {
        "pregunta": "¿Cuál es el número de compresiones por minuto recomendadas en adultos?",
        "opciones": ["60-80", "100-120", "120-140", "80-100"],
        "respuesta": "100-120"
    },
    {
        "pregunta": "¿Qué relación compresiones/ventilaciones se recomienda para adultos?",
        "opciones": ["15:2", "30:2", "5:1", "20:2"],
        "respuesta": "30:2"
    },
    {
        "pregunta": "¿Qué se debe hacer si la víctima respira pero está inconsciente?",
        "opciones": ["Dejarla en el lugar", "Realizar compresiones", "Colocarla en posición lateral de seguridad", "Esperar a que despierte"],
        "respuesta": "Colocarla en posición lateral de seguridad"
    },
    {
        "pregunta": "¿Qué significa RCP?",
        "opciones": ["Reacción Cardiopulmonar", "Respuesta de Emergencia", "Reanimación Cardiopulmonar", "Recuperación Clínica de Paciente"],
        "respuesta": "Reanimación Cardiopulmonar"
    },
    {
        "pregunta": "¿A qué profundidad deben hacerse las compresiones en adultos?",
        "opciones": ["1-2 cm", "2-4 cm", "5-6 cm", "más de 7 cm"],
        "respuesta": "5-6 cm"
    },
    {
        "pregunta": "¿Qué hacer si el DEA indica una descarga?",
        "opciones": ["Seguir con RCP", "Retirar los electrodos", "Aplicar descarga y no tocar a la persona", "Llamar a un médico"],
        "respuesta": "Aplicar descarga y no tocar a la persona"
    },
    {
        "pregunta": "¿Qué frecuencia respiratoria es normal en un adulto?",
        "opciones": ["10-12 por minuto", "12-20 por minuto", "20-30 por minuto", "30-40 por minuto"],
        "respuesta": "12-20 por minuto"
    },
    {
        "pregunta": "¿Qué debe hacerse antes de iniciar RCP?",
        "opciones": ["Buscar un desfibrilador", "Verificar que el entorno sea seguro", "Tomar los signos vitales", "Esperar a que llegue ayuda"],
        "respuesta": "Verificar que el entorno sea seguro"
    },
    {
        "pregunta": "¿Qué instrumento se utiliza para administrar una descarga eléctrica en casos de paro cardíaco?",
        "opciones": ["Marcapasos", "Electrocardiograma", "Desfibrilador", "Cardioversor"],
        "respuesta": "Desfibrilador"
    }
]

# Resultados
correctas = 0
respuestas_usuario = []

for i, p in enumerate(preguntas):
    st.subheader(f"Pregunta {i+1}")
    seleccion = st.radio(p["pregunta"], p["opciones"], key=i)
    respuestas_usuario.append((seleccion, p["respuesta"]))
    if seleccion == p["respuesta"]:
        correctas += 1

# Mostrar resultados
if st.button("Enviar respuestas"):
    st.success(f"¡Obtuviste {correctas} de {len(preguntas)} respuestas correctas!")
    for i, (resp_user, resp_correcta) in enumerate(respuestas_usuario):
        if resp_user == resp_correcta:
            st.markdown(f"✅ Pregunta {i+1}: Correcta")
        else:
            st.markdown(f"❌ Pregunta {i+1}: Incorrecta (Correcta: **{resp_correcta}**)")

