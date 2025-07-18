%%writefile calculator_app.py
import streamlit as st

st.title("🧮 Python Calculator App")

# User input
num1 = st.number_input("Enter the first number", format="%.2f")
op = st.selectbox("Choose an operation", ["+", "-", "*", "/"])
num2 = st.number_input("Enter the second number", format="%.2f")

# Perform calculation
if st.button("Calculate"):
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "❌ Error: Division by zero!"
    else:
        result = "❌ Invalid operator!"

    st.success(f"Result: {result}")
