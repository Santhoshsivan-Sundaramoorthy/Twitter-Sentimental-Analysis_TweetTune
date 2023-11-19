import pickle
import streamlit as st

model = None
def load_saved_resources():
    global model
    print('Loading Saved Resources...Start')
    with open("UI/Resource/Positive_Negative_Feedback_Model.pickle", 'rb') as f:
        model = pickle.load(f)
    print('Loading Saved Resources...Done')

st.set_page_config(
    page_title="TweetTune: EmoScan Edition",
    layout="wide"
)


st.write(
    '<div style="text-align:center; font-size:80px; color:#00b4d8;"><b>TweetTune</b></div>'
    '<div style="text-align:center; font-size:20px; color:white;">EmoScan Edition</div>',
    unsafe_allow_html=True)
input_text = st.text_input("Type the sentence here")
col1, col2, col3 = st.columns([3.8, 2, 2.5])
with col2:
    pressed = st.button("Analyse", key="centered_button")

if pressed and input_text and len(input_text.split()) >= 2:
    load_saved_resources()
    result = model.predict([input_text])

    if result == 0:
        st.write('<div style="text-align:center; font-size:40px; color:Red;">Negative 👎🏻</div>',
                 unsafe_allow_html=True)
    elif result == 2:
        st.write('<div style="text-align:center; font-size:40px; color:Green;">Positive 👍🏻</div>',
                 unsafe_allow_html=True)
    else:
        st.write("Neutral")
elif pressed:
    st.warning("Please enter at least two words in the input.")
