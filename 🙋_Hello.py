import os

import streamlit as st
import streamlit.components.v1 as components
from static.statics import embed_component

# use full page width
st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# :star: Welcome to Playground 👋")
st.write("### Glad you make it here,")
st.write("### I were expecting you :smile: have fun!")

st.success("Choose what ever you want from sidebar!")


# energy = st.slider("Boost your energy!", 1, 10, 5, 1)
# if energy < 5:
#     st.error("Come on!")
# elif energy < 8:
#     st.success("You are doing very well!")
# else:
#     st.success("You are amazing!")
# with st.sidebar:
#     components.html(embed_component['linkedin'], height=310)



# st.markdown(
#     """
#     Streamlit is an open-source app framework built specifically for
#     Machine Learning and Data Science projects.
#     **👈 Select a demo from the sidebar** to see some examples
#     of what Streamlit can do!
#     ### Want to learn more?
#     - Check out [streamlit.io](https://streamlit.io)
#     - Jump into our [documentation](https://docs.streamlit.io)
#     - Ask a question in our [community
#         forums](https://discuss.streamlit.io)
#     ### See more complex demos
#     - Use a neural net to [analyze the Udacity Self-driving Car Image
#         Dataset](https://github.com/streamlit/demo-self-driving)
#     - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
# """
# )