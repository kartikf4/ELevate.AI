import os
import pandas as pd 
from dotenv import load_dotenv,find_dotenv
from streamlit_option_menu import option_menu
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain.tools import Tool

#llm falcon model
load_dotenv()
AI71_API_KEY = os.getenv("AI71_API_KEY")
AI71_BASE_URL = os.getenv("AI71_BASE_URL")
llm = ChatOpenAI(
    model="tiiuae/falcon-180B-chat",
    api_key=AI71_API_KEY,
    base_url=AI71_BASE_URL,
    streaming=True,
    temperature =0.3
)



import streamlit as st
st.title("AI DATA SCIENTIST")
st.write("Hello I'm your AI data scientist assistant and I'm here to help with your data science project to enhance your bussiness.")

with st.sidebar:
    st.write("*Unleash the power of your data with my AI assistance!*")
    st.caption("""I'm ready to dive deep into your numbers, uncover hidden patterns, and deliver actionable insights. But first, we need a solid foundation. 
             Please upload your CSV file 📂 so we can embark on this data-driven journey together. 
             Let's transform your raw information into valuable knowledge.Sounds fun right , let's go!!
             """)
    with st.expander("What are the steps for EDA"):
       st.write(
           #llm.invoke("What are the steps for EDA").content
           )
    st.divider()
    st.caption("<p style ='text-align:center'>Made with ❤️ by Kartikeya</p>",unsafe_allow_html=True)
#finalizing the key 
if 'clicked' not in st.session_state:
    st.session_state.clicked={1:False}
#funcn to update value
def clicked(button):
    st.session_state.clicked[button]=True
st.button("let's get started",on_click=clicked,args=[1])

if st.session_state.clicked[1]:
    st.header("Let's start with EDA")
    user_csv = st.file_uploader("upload your file here", type="csv")

    if user_csv is not None:
        user_csv.seek(0)
        df = pd.read_csv(user_csv,low_memory=False)


pandas_agent = create_pandas_dataframe_agent(llm,df,verbose=True,allow_dangerous_code=True)
question="what are the columns?"
try:
    columns_meaning =pandas_agent.invoke(question)
    col_names = ",".join(df.columns)
    st.write(f"The Columns of the dataframe are {col_names}")
except ValueError as e:
    st.write(f"an error ocuured:{e}")

def function_agent(df,pandas_agent):
    st.write("**Data Overview**")
    st.write("The firsy rows of your dataset look like this:")
    st.write(df.head())
    try:
        st.write("**Data Cleaning**")
        st.subheader("Missing Values")
        columns = "what are the missing values in the dataframe?"
        Columns_df = pandas_agent.invoke(columns)
        output = Columns_df.get("output","").strip()
        if output:
            st.write(output.replace("\n"," "))
        else:
            st.write("k")
    except Exception as e:
        st.write(f"An Error occured while getting column meaning:{e}")


function_agent(df,pandas_agent)