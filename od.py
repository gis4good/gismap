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
    #  Over Due Map (OD)
     * The instance of OD has been shown village wise for every branch.
     * The villages with OD have been color coded according to the PAR %
     * Villages with no instance of OD are shown in white.
     The OD map can be used to identify the areas that are risky from operational point of view. Henceforth, necessary measures can be taken to plan the future operation of AFPL.
      
    """)
    import pandas as pd  
    df = pd.read_csv("od_maps_shareable_links.csv")
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
    st.markdown('For Download High Res = '+gg['link'][0], unsafe_allow_html=True)
    gif_runner = st.image('loading.gif')
    st.image(gg['link'][0].replace('dl=0','raw=1'))
    gif_runner.empty()



