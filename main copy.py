# import the streamlit library
import streamlit as st

# give a title to our app
st.title('Welcome to Basic Numerical Calculator(Anas))')

# TAKE WEIGHT INPUT in kgs
num_1 = st.number_input("Enter 1st Number: ")
num_2 = st.number_input("Enter 2st Number: ")

# TAKE HEIGHT INPUT
# radio button to choose height format
status = st.radio('Choose Operation to Perform: ',
                  ('Addition', 'Subtraction', 'multiplication','Division'))
st.button('2')
if st.button('Answer'):
# compare status value
    if (status == 'Addition'):
        FinalNum=num_1+num_2
        st.write('Result for addition is',FinalNum)

    elif (status == 'Subtraction'):
        FinalNum =num_1-num_2
        st.write('Result for subtraction is',FinalNum)
    elif  (status == 'multiplication'):
        FinalNum = num_1 * num_2
        st.write('Result for multiplication is: ', FinalNum)
    elif  (status == 'Division'):
        try:
            FinalNum = num_1 / num_2
            st.write('Result for Division is: ', FinalNum)
        except:
            st.error('Enter A non-zero Value for division Purposes')

