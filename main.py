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
                 background: url("https://images.unsplash.com/photo-1535478044878-3ed83d5456ef?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8Mnx8fGVufDB8fHx8&w=1000&q=80");
                 background-size: cover
             }}
             </style>
             """,
             unsafe_allow_html=True
         )
    set_bg_hack_url() 
