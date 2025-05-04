import streamlit as st

def main():
    st.title("Simple Adder App")
    st.write("This app adds two numbers.")

    num1 = st.text_input("Enter first number:", "")
    num2 = st.text_input("Enter second number:", "")

    if st.button("Add"):
        try:
            total = int(num1) + int(num2)
            st.success(f"The total is {total}.")
        except ValueError:
            st.error("Please enter valid integers.")

if __name__ == "__main__":
    main()
