# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 10:18:10 2023

@author: THIS-LAPPY
"""

import streamlit as st,numpy as np
import streamlit.components.v1 as components
import requests,io,pandas as pd,gc,time

def app():
    
    
    st.header("""
    Welcome to Annapurna Finance Pvt Ltd-Dashboard
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
    #   Branch Split Processor
        Please provide your path containing only Branch Split csv's. 
    """)
    multiple_files = st.file_uploader(
    "Multiple File Uploader",
    accept_multiple_files=True
)
    
    for file in multiple_files:
        file_container = st.expander(
            f"File name: {file.name} ({file.size})"
        )
        data = io.BytesIO(file.getbuffer())
        df=pd.read_csv(data)
    
    try:
        sl=df.groupby(['Parent Branch'],as_index=False).agg({'clients':'sum','pos':'sum','Par amount':'sum','Od Members':'sum','No. households':'sum','Census ID':'count','No_groups':lambda x: x.notnull().sum()})
        sl1=df.groupby(['Parent Branch','Proposed Branch'],as_index=False).agg({'clients':'sum','pos':'sum','Par amount':'sum','Od Members':'sum','No. households':'sum','Census ID':'count','No_groups':lambda x: x.notnull().sum()})
        slp=df.groupby(['Proposed Branch'],as_index=False).agg({'clients':'sum','pos':'sum','Par amount':'sum','Od Members':'sum','No. households':'sum','Census ID':'count','No_groups':lambda x: x.notnull().sum()})
        if sl1['Proposed Branch'][0]=='' or sl1['Proposed Branch'][0] is np.nan:
            slf=sl1[sl1['Proposed Branch']==''].reset_index(drop=True)
        
            
        
        smry=pd.DataFrame()    
        smry=smry.append({'Branch Type':'Split Branch','Name':slp['Proposed Branch'][1],'Total No. of Villages':slp['Census ID'][1],'Total No. of Villages with Portfolio':slp['No_groups'][1],
                          'Total POS':slp['pos'][1],'Total Clients':slp['clients'][1],'Total PAR(LKH)':slp['Par amount'][1],'Total OD Clients':slp['Od Members'][1],'No.of Household':slp['No. households'][1]},ignore_index=True)
        
        
        for i in range(len(sl)):
            for j in range(0,2):
                if j==0:
                    smry=smry.append({'Branch Type':f'Parent {i+1}(Before Splitting)','Name':sl['Parent Branch'][i],'Total No. of Villages':sl['Census ID'][i],'Total No. of Villages with Portfolio':sl['No_groups'][i],
                                      'Total POS':sl['pos'][i],'Total Clients':sl['clients'][i],'Total PAR(LKH)':sl['Par amount'][i],'Total OD Clients':sl['Od Members'][i],'No.of Household':sl['No. households'][i]},ignore_index=True)
                else:
                    smry=smry.append({'Branch Type':f'Parent {i+1}(After Splitting)','Name':sl['Parent Branch'][i],'Total No. of Villages':slf['Census ID'][i],'Total No. of Villages with Portfolio':slf['No_groups'][i],
                                      'Total POS':slf['pos'][i],'Total Clients':slf['clients'][i],'Total PAR(LKH)':slf['Par amount'][i],'Total OD Clients':slf['Od Members'][i],'No.of Household':slf['No. households'][i]},ignore_index=True)
                
           
                    
        smry['Total POS']=smry['Total POS']/10000000
        smry['Total PAR(LKH)']=smry['Total PAR(LKH)']/100000    
        st.write('Your File is ready to Download')
        st.download_button(label='Summary Table',data=smry.to_csv(index=False),file_name='summary_table.csv') 
        
    except:
        st.write('Something is wrong with the column names or data error')
