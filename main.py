import streamlit as st
import time

st.markdown("""
    <style>
    /* Make all st.button elements full width, and set a standard height/font size */
    div.stButton > button {
        width: 100%;
        height: 60px;
        font-size: 24px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Streamlit calculator 2.0📱")
st.text("By Anas")

if 'expression' not in st.session_state:
    st.session_state.expression = ""
if 'error' not in st.session_state:
    st.session_state.error = 0

if 'calc_input' not in st.session_state:
    st.session_state.calc_input = ""


def warning():
    st.warning('Look at the top right corner')

def add(val):
    st.session_state.expression += str(val)
    st.session_state.calc_input = st.session_state.expression

def clear():
    st.session_state.expression = ""
    st.session_state.calc_input = ""

def evaluate():
    try:
        result = eval(st.session_state.expression)
        st.session_state.expression = str(round(result, 2))
    except:
        st.session_state.error += 1
        st.session_state.expression = " "
    # After evaluation, push the result into the text input
    st.session_state.calc_input = st.session_state.expression



cols = st.columns(4)
with cols[0]:
    if st.button("7️⃣"):
        add("7")
with cols[1]:
    if st.button("8️⃣"):
        add("8")
with cols[2]:
    if st.button("9️⃣"):
        add("9")
with cols[3]:
    if st.button("➗"):
        add("/")


cols = st.columns(4)
with cols[0]:
    if st.button("4️⃣"):
        add("4")
with cols[1]:
    if st.button("5️⃣"):
        add("5")
with cols[2]:
    if st.button("6️⃣"):
        add("6")
with cols[3]:
    if st.button("✖️"):
        add("*")


cols = st.columns(4)
with cols[0]:
    if st.button("1️⃣"):
        add("1")
with cols[1]:
    if st.button("2️⃣"):
        add("2")
with cols[2]:
    if st.button("3️⃣"):
        add("3")
with cols[3]:
    if st.button("➖"):
        add("-")


cols = st.columns(4)
with cols[0]:
    if st.button("0️⃣"):
        add("0")
with cols[1]:
    if st.button("."):
        add(".")
with cols[2]:
    if st.button("🟰"):
        evaluate()
with cols[3]:
    if st.button("➕"):
        add("+")

if st.button("Clear🧹"):
    clear()


def evaluate_input():
    st.session_state.expression = st.session_state.calc_input
    evaluate()

input_val = st.text_input(
    "Calculator Input (Press Enter to Evaluate)",
    key="calc_input",
    on_change=evaluate_input
)

st.write("Current Entry by user:", st.session_state.expression)

if st.session_state.error >= 1:
    warning()
    time.sleep(1.5)
    msg = st.toast("Running the complex algorithm you entered...")
    time.sleep(1.5)
    msg.toast("Still Loading...")
    time.sleep(1.5)
    msg.toast("Bro doesn't even know basic maths", icon="😒")
    st.session_state.error = 0

