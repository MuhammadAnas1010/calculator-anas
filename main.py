import streamlit as st
import time

st.title("Streamlit calculator 2.0📱")
st.text("By Anas")

if 'expression' not in st.session_state and 'error' not in st.session_state:
    st.session_state.expression = ""
    st.session_state.error=0
def warning():
    st.warning('Look at the top right corner')
def add(val):
    st.session_state.expression += str(val)

def clear():
    st.session_state.expression = ""

def evaluate():
    try:
        result = eval(st.session_state.expression)
        st.session_state.expression = str(round(result, 2))
    except:
        st.session_state.error+=1
        st.session_state.expression = " "


col1 = st.columns(4)
with col1[0]:
    if st.button("7️⃣"):
        add("7")
with col1[1]:
    if st.button("8️⃣"):
        add("8")
with col1[2]:
    if st.button("9️⃣"):
        add("9")
with col1[3]:
    if st.button("➗"):
        add("/")

# Row 2: 4, 5, 6, *
col2= st.columns(4)
with col2[0]:
    if st.button("4️⃣"):
        add("4")
with col2[1]:
    if st.button("5️⃣"):
        add("5")
with col2[2]:
    if st.button("6️⃣"):
        add("6")
with col2[3]:
    if st.button("✖️"):
        add("*")

# Row 3: 1, 2, 3, -
col3= st.columns(4)
with col3[0]:
    if st.button("1️⃣"):
        add("1")
with col3[1]:
    if st.button("2️⃣"):
        add("2")
with col3[2]:
    if st.button("3️⃣"):
        add("3")
with col3[3]:
    if st.button("➖"):
        add("-")

# Row 4: 0, C, =, +
col4 = st.columns(4)
with col4[0]:
    if st.button("0️⃣"):
        add("0")
with col4[1]:
    if st.button("."):
        add('.')
with col4[2]:
    if st.button("🟰"):
        evaluate()
with col4[3]:
    if st.button("➕"):
        add("+")

if st.button('C'):
    clear()
input_val = st.text_input("Calculator Input", key="expression")


if input_val != st.session_state.expression:
    st.session_state.expression = input_val


st.write("Current Entry by user:", st.session_state.expression)
if st.session_state.error >=1:
    warning()
    time.sleep(1.5)
    msg = st.toast('Running the complex algorithm you entered...')
    time.sleep(1.5)
    msg.toast('Still Loading...')
    time.sleep(1.5)
    msg.toast('Bro does\'t even know basic maths', icon="😒")
    st.session_state.error=0