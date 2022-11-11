# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 09:38:09 2022

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
                  background: url("http://bizrak.com/images/bgs/bg.jpg");
                  background-size: cover
              }}
              </style>
              """,
              unsafe_allow_html=True
          )
    set_bg_hack_url() 
    st.header('')
    st.write("""
    # OPerational Map
    Image depecting villages covered by Branches. 
    """)
    import pandas as pd  
    df = pd.read_csv("om_maps_pincodes.csv")
    image_list = df.iloc[:, 1].unique().tolist()
    item_list = df.iloc[:, 0].unique().tolist()
    images = dict(zip(item_list, image_list))

    user_option = st.selectbox('Choose your Branch',item_list)
    print(user_option)
    gg=df[df['Filename']==user_option].reset_index(drop=True)
    # st.image(gg['link'][0], width = 400)
    # st.components.v1.iframe(gg['link'][0], width = 1500, height = 800, scrolling = True)
    # st.image(gg['link'][0].replace('dl=0','raw=1'))
    # st.markdown(gg['link'][0], unsafe_allow_html=True)
    st.markdown('For Download High Res = '+gg['link'][0].replace('raw=1','dl=0'), unsafe_allow_html=True)
    st.image(gg['link'][0].replace('dl=0','raw=1'))


