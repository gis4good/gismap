# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 14:36:37 2022

@author: THIS-LAPPY
"""

# -*- coding: utf-8 -*-

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
    #  Business Potential Map (BPM)
     * The villages that are colored Green are vacant villages which have no clients from AFPL.
     * The Villages with existing clients are colored in Red according to Client coverage %
      (Client coverage percent is the percentage of AFPL's clients to the total no of households of that village)
     * The House icon represents the no of Households present in that village and the woman icon represents the no of Annapurna's clients.
     From the BPM we can see the potential areas for expanding operations in the existing boundary.   
    """)
    import pandas as pd  
    df = pd.read_csv(r"C:\Users\THIS-LAPPY\Desktop\gis\sharable_link_for_mail\bpm_maps_shareable_links.csv")
    image_list = df.iloc[:, 1].unique().tolist()
    item_list = df.iloc[:, 0].unique().tolist()
    images = dict(zip(item_list, image_list))

    user_option = st.selectbox('Choose your Branch',item_list)
    gg=df[df['Filename']==user_option].reset_index(drop=True)
    # st.image(gg['link'][0], width = 400)
    # st.components.v1.iframe(gg['link'][0], width = 1500, height = 800, scrolling = True)
    # st.image(gg['link'][0].replace('dl=0','raw=1'))
    # st.markdown(gg['link'][0], unsafe_allow_html=True)
    st.markdown('For Download High Res = '+gg['link'][0], unsafe_allow_html=True)
    gif_runner = st.image('loading.gif')
    st.image(gg['link'][0].replace('dl=0','raw=1'))
    gif_runner.empty()



