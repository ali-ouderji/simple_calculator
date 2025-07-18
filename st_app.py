import streamlit as st

st.set_page_config(page_title="Python Calculator", layout="centered")
st.title("🧮 Python Calculator App")

# Store the current expression in session state
if "expression" not in st.session_state:
    st.session_state.expression = ""

# Display the current expression
st.text_input("Display", st.session_state.expression, key="display", disabled=True)

# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "C", "+"],
    ["=",]
]

# Function to update expression
def press(button):
    if button == "C":
        st.session_state.expression = ""
    elif button == "=":
        try:
            result = eval(st.session_state.expression)
            st.session_state.expression = str(round(result, 6))
        except ZeroDivisionError:
            st.session_state.expression = "❌ Division by zero!"
        except:
            st.session_state.expression = "❌ Error"
    else:
        st.session_state.expression += button

# Create the buttons
for row in buttons:
    cols = st.columns(len(row))
    for i, button in enumerate(row):
        if cols[i].button(button):
            press(button)

