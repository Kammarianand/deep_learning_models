import streamlit as st
from transformers import pipeline
import time

st.title("Sentiment Classifier")
with st.expander("About this project"):
     st.markdown('''
            Hey there! I'm working on this project for fun. The project is built using Python programming language, incorporating modules like Streamlit and TensorFlow, among others. I'll be adding more features to this site, such as text summarization, text translation, text classification, and context recognition within text, soon. I'm undertaking this project as part of fine-tuning my skills,
            I'm doing my level best to develop this application. Stay tuned! 🚧✨
                 
            [![LinkedIn](https://img.shields.io/badge/LinkedIn-Kammari%20Anand-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/kammari-anand-504512230/)

''')
usr_text = st.chat_input("Enter Your Text Here")

def toast():
    st.toast("woah! 🎉")
    st.balloons()

def analyzer(usr_text):
    cls = pipeline('sentiment-analysis')
    output = cls(usr_text)
    dict_op = output[0]
    lable = dict_op['label']
    score = dict_op['score']
    score = score * 1000
    org_output = "Text Entered by you is "+str(score)[0:2]+"% "+lable
    op = " "
    with  st.chat_message("assistant"):
        with st.spinner("Thinking...."):
            time.sleep(1)
            with st.container(border=True,height=250):
                st.write("Your text: "+usr_text)
                for i in org_output.split():
                    op = i + " "
                    yield op + " "
                    time.sleep(0.2)





if usr_text:
        st.write_stream(analyzer(usr_text))
        toast()







