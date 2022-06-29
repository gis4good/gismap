# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 12:29:32 2022

@author: THIS-LAPPY
"""

import streamlit as st
import streamlit.components.v1 as components

def app():
    st.write("""
    # 
    """) 
    st.header("Dynamic Map Displaying MSME Branches Location")
    
    HtmlFile = open("msme.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code,height =800,width=600)
    
    page_bg_img = '''
    <style>
    body {
    background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
    background-size: cover;
    }
    </style>
    '''
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
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
                 background: url("https://wallpapercave.com/wp/wp2174011.jpg");
                 background-size: cover
             }}
             </style>
             """,
             unsafe_allow_html=True
         )
    set_bg_hack_url() 
    
    