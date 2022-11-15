# -*- coding: utf-8 -*-
"""

Created on Mon Nov 14 14:33:13 2022

@author: THIS-LAPPY
"""


import streamlit as st,numpy as np
import streamlit.components.v1 as components
import urllib,base64,requests

def show_pdf(file_path):
    with open(file_path,"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        base64_pdf=base64_pdf
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
    print('reached')
    st.markdown(pdf_display, unsafe_allow_html=True)

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
    #  Industry Scenario Map (ISM)
    Shows the Microfinance industry scenario in terms of
    * Disbursed loans
    * PAR (Portfolio at Risk)   
    """)
    import pandas as pd  
    df = pd.read_csv("ism_sharable_link.csv")
    image_list = df.iloc[:, 1].unique().tolist()
    item_list = df.iloc[:, 0].unique().tolist()
    images = dict(zip(item_list, image_list))

    user_option = st.selectbox('Choose your Branch',item_list)
    gg=df[df['Filename']==user_option].reset_index(drop=True)
    # st.image(gg['link'][0], width = 400)
    # st.components.v1.iframe(gg['link'][0], width = 1500, height = 800, scrolling = True)
    # st.image(gg['link'][0].replace('dl=0','raw=1'))
    st.markdown('For downloading or viewing pdf please click this link = '+gg['link'][0], unsafe_allow_html=True)
    # st.markdown('For Download High Res = '+gg['link'][0], unsafe_allow_html=True)
    # with urllib.request.urlopen('https://www.dropbox.com/s/22sl7cbk29tt1m2/Abu%20Road_ISM.pdf?dl=0') as f:
    #     base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    # ff=requests.get(gg['link'][0])
    # with open('metadata.pdf', 'wb') as f:
    #       f.write(ff.content)
   
    # show_pdf(r"C:\Users\THIS-LAPPY\Downloads\Cropin_Annapurna Finance Pvt Ltd.pdf")

