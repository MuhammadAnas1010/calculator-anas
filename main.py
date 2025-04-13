import streamlit as st
st.title("Streamlit calculator 2.0📱")

if 'expression' not in st.session_state:
    st.session_state.expression = ""

def add(val):
    st.session_state.expression += str(val)

def clear():
    st.session_state.expression = ""

def evaluate():
    try:
        st.session_state.expression = str(eval(st.session_state.expression))
    except:
        warning()
        st.session_state.expression = " "


col1 = st.columns(4)
with col1[0]:
    if st.button("7"):
        add("7")
with col1[1]:
    if st.button("8"):
        add("8")
with col1[2]:
    if st.button("9"):
        add("9")
with col1[3]:
    if st.button("➗"):
        add("/")

# Row 2: 4, 5, 6, *
col2= st.columns(4)
with col2[0]:
    if st.button("4"):
        add("4")
with col2[1]:
    if st.button("5"):
        add("5")
with col2[2]:
    if st.button("6"):
        add("6")
with col2[3]:
    if st.button("✖️"):
        add("*")

# Row 3: 1, 2, 3, -
col3= st.columns(4)
with col3[0]:
    if st.button("1"):
        add("1")
with col3[1]:
    if st.button("2"):
        add("2")
with col3[2]:
    if st.button("3"):
        add("3")
with col3[3]:
    if st.button("➖"):
        add("-")

# Row 4: 0, C, =, +
col4 = st.columns(4)
with col4[0]:
    if st.button("0"):
        add("0")
with col4[1]:
    if st.button("C"):
        clear()
with col4[2]:
    if st.button("🟰"):
        evaluate()
with col4[3]:
    if st.button("➕"):
        add("+")


input_val = st.text_input("Calculator Input", key="expression")


if input_val != st.session_state.expression:
    st.session_state.expression = input_val
def warning():
    st.warning('Seems like you don\'t know basic math😒')

st.write("Current Entry by user:", st.session_state.expression)
