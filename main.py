import streamlit as st

# Streamlit app title
st.title("Favorite Animal App")

# Ask the user for their favorite animal
favorite_animal = st.text_input("What is your favorite animal?")

# Check if input is provided
if favorite_animal:
    # Display the formatted response using Markdown
    st.markdown(f"My favorite animal is also ***{favorite_animal}***!")
