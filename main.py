import streamlit as st
st.title("Streamlit calculator 2.0📱")
st.header("Corvit")
# --- Step 1: Initialize session state ---
if 'expression' not in st.session_state:
    st.session_state.expression = ""
#if 'update_counter' not in st.session_state:
    #st.session_state.update_counter = 0

# --- Step 2: Define action functions ---
def press(val):
    st.session_state.expression += str(val)
   # st.session_state.update_counter += 1  # update counter to trigger re-render

def clear():
    st.session_state.expression = ""
   # st.session_state.update_counter += 1

def evaluate():
    try:
        st.session_state.expression = str(eval(st.session_state.expression))
    except:
        st.session_state.expression = "Error"
    #st.session_state.update_counter += 1

# --- Step 3: Create the calculator buttons ---
# (These buttons update the session state)
# Row 1: 7, 8, 9, /
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("7"):
        press("7")
with col2:
    if st.button("8"):
        press("8")
with col3:
    if st.button("9"):
        press("9")
with col4:
    if st.button("➗"):
        press("/")

# Row 2: 4, 5, 6, *
col5, col6, col7, col8 = st.columns(4)
with col5:
    if st.button("4"):
        press("4")
with col6:
    if st.button("5"):
        press("5")
with col7:
    if st.button("6"):
        press("6")
with col8:
    if st.button("✖️"):
        press("*")

# Row 3: 1, 2, 3, -
col9, col10, col11, col12 = st.columns(4)
with col9:
    if st.button("1"):
        press("1")
with col10:
    if st.button("2"):
        press("2")
with col11:
    if st.button("3"):
        press("3")
with col12:
    if st.button("➖"):
        press("-")

# Row 4: 0, C, =, +
col13, col14, col15, col16 = st.columns(4)
with col13:
    if st.button("0"):
        press("0")
with col14:
    if st.button("C"):
        clear()
with col15:
    if st.button("🟰"):
        evaluate()
with col16:
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
