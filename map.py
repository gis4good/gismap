# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 10:37:34 2022

@author: THIS-LAPPY
"""

import streamlit as st,msme,main
import streamlit.components.v1 as components

# >>> import plotly.express as px
# >>> fig = px.box(range(10))
# >>> fig.write_html('test.html')

# st.set_page_config(layout="wide")

def check_password():
    """Returns `True` if the user had the correct password."""
    st.write("""
    # Map Dashboard 
    """)

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        st.write("""
        """)
        # Password correct.
        return True
st.write("""
 # 
 """) 
if check_password():  
    st.sidebar.image(['https://media.giphy.com/media/uShpe8u5laTlB19yFk/giphy.gif'], width=280, output_format="GIF")
    
    def sidebar_bg():

    
       st.markdown(
          f"""
          <style>
          [data-testid="stSidebar"] > div:first-child {{
              background: url("https://theworkflowacademy.com/wp-content/uploads/2020/11/Learning-path-banner-1.png");
          }}
          </style>
          """,
          unsafe_allow_html=True,
          )

 
    sidebar_bg()



    PAGES = {
    "Main Page": main,
    "MSME Branches": msme
    }
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    page = PAGES[selection]
    page.app()
    
    st.write("""
    # 
    """)  
    
   
    
   
    
   
    
   
    

    

