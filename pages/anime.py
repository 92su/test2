# pip install openpyxl
import pandas as pd
import streamlit as st
import zipfile
import base64
import os
import datetime as dt
import plotly.express as px  # pip install plotly-express
from dateutil.relativedelta import relativedelta # to add days or years
from datetime import datetime, date ,time
from PIL import Image
import matplotlib.pyplot as plt
from st_vizzu import *
from st_pages import Page,show_pages,add_page_title


st.sidebar.subheader('Upload Excel File')
uploaded_file = st.sidebar.file_uploader("Choose a XLSX file", type="xlsx")
if uploaded_file:
    df = pd.read_excel(uploaded_file,sheet_name=1)
    st.dataframe(df)

    obj = create_vizzu_obj(df)


    bar_obj = bar_chart(df,
                x="academicyear",
                y="TotalPaper",
                title="1.Using preset plot function 'bar_chart()'")

    anim_obj = beta_vizzu_animate(bar_obj,
        x = "academicyear",
        y = ["Quartile1","Quartile2","Quartile3","Quartile4","No Quartile"],
        title = "2.Animate with",
        label="Paper Publication",
        color = "academicyear",
        legend="color",
        sort="byValue",
        reverse=True,
        align="center",
        split=False,
    )

    _dict={"size":{"set":"TotalPaper"},
        "geometry":"circle",
        "coorSystem":"polar",
        "title":"3.Animate with: generic dict-based 'vizzu_animate'",}

    anim_obj2 = vizzu_animate(anim_obj,_dict)

    with st.container():
        vizzu_plot(anim_obj2)
        st.button("Animate ♻️",type='primary')



    obj = create_vizzu_obj(df)
    config_dict = {"channels":{"y":["academicyear"],"x":["Quartile1","Quartile2","Quartile3","Quartile4","TotalPaper"]}}
    style_dict={"plot":{"paddingLeft":"12em"}}

            # animate with general dict based arguements
    anim_obj = vizzu_animate(obj,config_dict=config_dict,style_dict=style_dict)
            # animate with arguement based
    anim_obj1 = beta_vizzu_animate(anim_obj,
        x=None,y=None,size=["academicyear","TotalPaper"],
        label="Total Paper",color="TotalPaper",geometry="circle")

    anim_obj2 = vizzu_animate(anim_obj1,
                    {
                    "y":"TotalPaper",
                    "x":["academicyear","Quartile1"],
                    "label":None,
                    "size":None,
                    "geometry":"rectangel"
                }
            )


    anim_obj3 = vizzu_animate(anim_obj2,
                config_dict={"x":"TotalPaper",
                "label":"Total Paper"
                })

    with st.container():
        vizzu_plot(anim_obj3,width=800,height=800)
