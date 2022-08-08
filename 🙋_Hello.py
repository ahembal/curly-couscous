import os
from data.embed_data import embed_linkedin
import streamlit as st
import streamlit.components.v1 as components
cur_dir = os.getcwd()

# use full page width
st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)
with open(f"{cur_dir}/static/docs/Emre.Balsever.pdf", "rb") as f:
    data = f.read()

st.sidebar.download_button("Download CV in PDF format", data=data, file_name="EmreBalsever.pdf")
with st.sidebar:
    components.html(embed_linkedin['linkedin'], scrolling=True, height=500)

st.write("## What is this page for?")
st.markdown(
    """
    After spending few months with sending CVs to the 
    [*lovely recruiters*](https://www.linkedin.com/business/talent/blog/talent-strategy/what-is-recruitment),
    I **realized** it is [almost impossible to explain](https://blog.recright.com/cvs-are-less-relevant-for-recruiters) 
    my works in [few pages of PDFs](https://thrivemap.io/6-reasons-we-should-stop-asking-for-cvs/) , 
    because CVs look
    [messy](https://www.theguardian.com/careers/2015/nov/11/why-you-dont-need-a-cv-to-get-your-next-job). 👾 
    
    At the end, I decided to make this 'report page' to summarize my works. So to speak, all these things done for you 😊
    
    .
    
    .
    
    Anyway, before jumping into pages, I would like to question something here:
    """
)
if st.button("Click on me :)"):
    img_path = cur_dir + '/static/imgs/1658862996704.jpg'
    st.image(img_path)
    st.success("If you find the answer, please let me know :) Good luck!")
    st.write("# :star: Welcome to Playground 🙋")
    st.write("#### I'm so glad you made it here!")
    st.write("#### I was expecting you :smile: have fun!")

    st.success("Choose what ever you want from the sidebar!")
