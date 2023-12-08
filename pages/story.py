
from streamlit.components.v1 import html
import pandas as pd
from ipyvizzu import Chart,Data, Config, Style,DisplayTarget
from streamlit.components.v1 import html
import streamlit as st
from st_vizzu import *
import ssl
from streamlit_extras.mention import mention


ssl._create_default_https_context = ssl._create_unverified_context
@st.cache_data
def load_data(data_path:str):
    ''' Load the data
    Parameter
    ---------
    data_path : String
        Path to Data File
    Returns
    -------
        Pandas.DataFrame
    '''
    return pd.read_csv(data_path,sep=';')

st.sidebar.title("Basic-Demo")
st.sidebar.button("Animate ♻️ ",type='primary')

with st.sidebar:
    st.header("Configuration")
    uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is None:
    st.info(" Upload a file through config", icon="ℹ️")
    st.stop()

#######################################
# DATA LOADING
#######################################


@st.cache_data
def load_data(path: str):
    df = pd.read_excel(path)
    return df

df = load_data(uploaded_file)
obj = create_vizzu_obj(df)

config_dict = {"channels": {"y": ["Academic_Year"],"x": ["Total_Paper","Paper_Teacher_Ratio"] }}
style_dict = {"plot":{"paddingLeft": "12em"}}

anim_obj = vizzu_animate(obj,config_dict=config_dict,style_dict=style_dict)

anim_obj1 = beta_vizzu_animate(anim_obj,
    x=None,y=None,size=["Academic_Year","Total_Paper"],
    label="Year", color="Quartile1",geometry="circle")


anim_obj2 = vizzu_animate(anim_obj1,
                {
                "y": "Total_Paper",
                "x": ["Academic_Year","Paper_Teacher_Ratio"],
                "label": None,
                "size" : None,
                "geometry": "rectangle"
            }

        )

anim_obj3 = vizzu_animate(anim_obj2,
            config_dict={
            "x": "Academic_Year",
            "label": "Total_Paper"
            })
with st.container():
    vizzu_plot(anim_obj3,width=800,height=800)
