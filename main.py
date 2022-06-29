# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 12:39:38 2022

@author: THIS-LAPPY
"""

import streamlit as st

def app():
    st.write("""
    # 
    """) 
    st.header("Welcome to Annapurna Map DashBoard")
    
    
    import base64    
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
                 background: url("https://static.vecteezy.com/system/resources/previews/002/849/000/original/modern-dark-background-with-gradient-geometric-shape-themes-vector.jpg");
                 background-size: cover
             }}
             </style>
             """,
             unsafe_allow_html=True
         )
    set_bg_hack_url() 