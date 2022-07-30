import itertools
import json
from streamlit_timeline import timeline
import streamlit as st

st.set_page_config(page_title="Background", page_icon="🗂", layout="wide")
if 'focus_time' not in st.session_state:
    st.session_state['focus_time'] = None

st.markdown("# Timeline version of my Background")
st.write("""This page shows most of my works but not all! """)
st.sidebar.header("Interactive CV:")
st.sidebar.markdown("### Layers")

# load data
file_name = 'data/background.json'
with open(file_name, "r") as f:
    values = json.load(f)

ALL_LAYERS = values.keys()
# ALL_LAYERS = {"University & Collage Degree": "",
#               "Experiences": "",
#               "Certificates": "",
#               "Courses": ""}
selected_layers = [
    layer
    for layer in ALL_LAYERS
    if st.sidebar.checkbox(layer, False)
]


def load_data(selected_layers):
    selected_data = [values[i]['events'] for i in selected_layers]
    selected_data = list(itertools.chain.from_iterable(selected_data))
    selected_data_dict = {"events": selected_data}
    # render timeline
    timeline(selected_data_dict, height=600)


# Streamlit Timeline Component Example
if selected_layers:
    load_data(selected_layers)

else:
    st.error("Please choose at least one layer from sidebar.")
