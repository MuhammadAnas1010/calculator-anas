import streamlit as st
st.title("Streamlit calculator 2.0📱")

# --- Step 1: Initialize session state ---
if 'expression' not in st.session_state:
    st.session_state.expression = ""

# --- Step 2: Define action functions ---
def press(val):
    st.session_state.expression += str(val)

def clear():
    st.session_state.expression = ""

def evaluate():
    try:
        st.session_state.expression = str(eval(st.session_state.expression))
    except:
        st.session_state.expression = "Error"

# --- Step 3: Create the calculator buttons ---
# (These buttons update the session state)
# Row 1: 7, 8, 9, /
#col11=[]
col1 = st.columns(4)
with col1[0]:
    if st.button("7"):
        press("7")
with col1[1]:
    if st.button("8"):
        press("8")
with col1[2]:
    if st.button("9"):
        press("9")
with col1[3]:
    if st.button("➗"):
        press("/")

# Row 2: 4, 5, 6, *
col2= st.columns(4)
with col2[0]:
    if st.button("4"):
        press("4")
with col2[1]:
    if st.button("5"):
        press("5")
with col2[2]:
    if st.button("6"):
        press("6")
with col2[3]:
    if st.button("✖️"):
        press("*")

# Row 3: 1, 2, 3, -
col3= st.columns(4)
with col3[0]:
    if st.button("1"):
        press("1")
with col3[1]:
    if st.button("2"):
        press("2")
with col3[2]:
    if st.button("3"):
        press("3")
with col3[3]:
    if st.button("➖"):
        press("-")

# Row 4: 0, C, =, +
col4 = st.columns(4)
with col4[0]:
    if st.button("0"):
        press("0")
with col4[1]:
    if st.button("C"):
        clear()
with col4[2]:
    if st.button("🟰"):
        evaluate()
with col4[3]:
    if st.button("➕"):
        press("+")

# --- Step 4: Render the input display AFTER the button presses ---
# We use a dynamic key here to force re-rendering of the input widget.
#input_key = f"calc_input_{st.session_state.update_counter}"
input_val = st.text_input("Calculator Input", key="expression")

# If the user changes the text input manually, update our session state.
if input_val != st.session_state.expression:
    st.session_state.expression = input_val

# --- Step 5: Show the current expression (for debugging/display) ---
st.write("Current Expression:", st.session_state.expression)
