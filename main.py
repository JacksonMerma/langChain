import langchain_helper as lch
import streamlit as st

st.title("Pets name generator")
pets = ["Cat", "Dog", "Cow", "Hamster"]

animal_type = st.sidebar.selectbox("What is your pet?", pets)

for pet in pets:
    if animal_type == pet:
        pet_color = st.sidebar.text_area(label=f"What color is your {pet}?", max_chars=15)

if pet_color:
    response = lch.generate_pet_name(animal_type=animal_type, pet_color=pet_color)
    st.text(response.content)

