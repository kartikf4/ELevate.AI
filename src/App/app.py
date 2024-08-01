#import required libraries
import streamlit as st
#Main page 

about_Page = st.Page(
    page="/ElEVATE.AI/src/app/About.py",
    title="About",
    icon="🎈",
    default=True
)
about_ai_data_page = st.Page(
    page ="/ELevate.AI/src/App/AIDataScientist.py",
    title="AI Data Scientist Agent",
    icon="🤖",
)

#naviagtion stepup 
pg =st.navigation({
    "INFO":[about_Page],
    "AI TOOLS":[about_ai_data_page]
})
pg.run()

