# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 14:33:13 2022

@author: THIS-LAPPY
"""

import streamlit as st,numpy as np
import streamlit.components.v1 as components
import requests

def app():
    
    
    st.header("""
    Welcome to Annapurna Finance Pvt Ltd - Branch Split Dashboard
    """)
    # streamlit_app.py
    
    
    def set_bg_hack_url():
         '''
         A function to unpack an image from url and set as bg.
         Returns
         -------
         The background.
         '''
             
         st.markdown(
              f"""
              <style>
              .stApp {{
                  background: url("https://wallpaper.dog/large/20361140.jpg");
                  background-size: cover
              }}
              </style>
              """,
              unsafe_allow_html=True
          )
    set_bg_hack_url() 
    st.header('')
    st.write("""
    #  Excel Sheet
     * Contains all covered and uncovered villages
     * Has the client coverage percentage along with number of households in each village
    """)
    import pandas as pd  
    df = pd.read_csv(r"C:\Users\THIS-LAPPY\Desktop\gis\sharable_link_for_mail\bpm_excel_shareable_links.csv")
    image_list = df.iloc[:, 1].unique().tolist()
    item_list = df.iloc[:, 0].unique().tolist()
    images = dict(zip(item_list, image_list))

    user_option = st.selectbox('Choose your Branch',item_list)
    gg=df[df['Filename']==user_option].reset_index(drop=True)
    
    st.markdown('For Download Excel Sheet = '+gg['link'][0], unsafe_allow_html=True)
    gif_runner = st.image('loading.gif')
    st.dataframe(pd.read_excel(gg['link'][0].replace('dl=0','raw=1')))
    gif_runner.empty()

    
