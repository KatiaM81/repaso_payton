import streamlit as st

st.set_page_config(page_title="Quiz de Python", page_icon="🐍")

st.title("🐍 Quiz de Python: Sintaxis y estructuras básicas")

st.markdown("Responde las siguientes preguntas para repasar funciones, listas, bucles y condicionales en Python.")

# Preguntas del quiz
questions = [
    {
        "question": "¿Cómo se define una función en Python?",
        "options": ["func mi_funcion():", "function mi_funcion():", "def mi_funcion():", "define mi_funcion():"],
        "answer": "def mi_funcion():"
    },
    {
        "question": "¿Cuál de las siguientes es una lista válida en Python?",
        "options": ["{1, 2, 3}", "(1, 2, 3)", "[1, 2, 3]", "<1, 2, 3>"],
        "answer": "[1, 2, 3]"
    },
    {
        "question": "¿Qué hace un bucle FOR en Python?",
        "options": [
            "Ejecuta código mientras una condición es verdadera",
            "Permite ejecutar código una sola vez",
            "Itera sobre elementos de una secuencia",
            "Detiene la ejecución del programa"
        ],
        "answer": "Itera sobre elementos de una secuencia"
    },
    {
        "question": "¿Qué palabra clave se usa para una condición en Python?",
        "options": ["when", "for", "if", "elif"],
        "answer": "if"
    },
    {
        "question": "¿Qué imprimirá el siguiente código?\n\n```python\nlista = [1, 2, 3]\nfor x in lista:\n    print(x*2)\n```",
        "options": ["1 2 3", "2 4 6", "1 4 9", "Error"],
        "answer": "2 4 6"
    },
]

# Variables para respuestas del usuario
user_answers = []
score = 0

with st.form("quiz_form"):
    for i, q in enumerate(questions):
        st.markdown(f"**{i+1}. {q['question']}**")
        user_choice = st.radio("", q["options"], key=f"q{i}")
        user_answers.append(user_choice)

    submitted = st.form_submit_button("Verificar respuestas")

if submitted:
    for i, q in enumerate(questions):
        if user_answers[i] == q["answer"]:
            score += 1

    st.success(f"Obtuviste {score} de {len(questions)} puntos.")

    if score == len(questions):
        st.balloons()
