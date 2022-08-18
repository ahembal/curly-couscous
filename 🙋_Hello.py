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
with open(f"{cur_dir}/static/docs/Balsever.pdf", "rb") as f:
    data = f.read()

st.sidebar.download_button("Download CV in PDF format", data=data, file_name="EmreBalsever.pdf")
# with st.sidebar:
components.html(embed_linkedin['linkedin'], scrolling=True, height=277)

# st.write("### What is this page for?")
st.markdown(
    """
    Welcome to interactive CV page.
    
    I created this page as a visualization of my works to follow up easily, to find connections between each other, and to make collaborations easier.
    
    I think this page can make recruitment [process easier](https://www.theguardian.com/careers/2015/nov/11/why-you-dont-need-a-cv-to-get-your-next-job) for [recruiters](https://www.linkedin.com/business/talent/blog/talent-strategy/what-is-recruitment), 
    because it is [almost impossible to explain](https://blog.recright.com/cvs-are-less-relevant-for-recruiters) 
    my works in [few pages of PDFs](https://thrivemap.io/6-reasons-we-should-stop-asking-for-cvs/).
    
    ------------------------------------------------------------------------------------
    
    #### Usage
    Past projects is sorted by date via timeline tool in [Projects](https://www.emre.balsever.com/Projects) page.
    
    Degrees, Experiences, Certificates, Courses, and even Hobbies can be found in [Background](https://www.emre.balsever.com/Background) page.
    
    Demo version of some of my works can be found in [Demos](https://www.emre.balsever.com/Demos) page. 
    
    Latest Pdf version of my CV can be downloadable via the button in the sidebar. 
    
    You can reach out to me via LinkedIn profile badge above.
    
    Best wishes!
    
    """
)

