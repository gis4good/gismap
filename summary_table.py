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
        df=pd.read_csv(data,header=1,sep='\t',encoding="utf-16").fillna(0)
    
    try:
        sl=df.groupby(['Parent Branch'],as_index=False).agg({'clients':'sum','pos':'sum','Par amount':'sum','Od Members':'sum','No. households':'sum','Gp Name':'count','No_groups':lambda x: x.notnull().sum()})
        sl1=df.groupby(['Parent Branch','Proposed Branch'],as_index=False).agg({'clients':'sum','pos':'sum','Par amount':'sum','Od Members':'sum','No. households':'sum','Gp Name':'count','No_groups':lambda x: x.notnull().sum()})
        
            
        
        smry=pd.DataFrame()    
        smry=smry.append({'Branch Type':'Split Branch','Name':sl1['Proposed Branch'][0],'Total No. of Villages':sl1['Gp Name'].sum(),'Total No. of Villages with Portfolio':sl1['No_groups'].sum(),
                          'Total POS':sl1['pos'].sum(),'Total Clients':sl1['clients'].sum(),'Total PAR(LKH)':sl1['Par amount'].sum(),'Total OD Clients':sl1['Od Members'].sum(),'No.of Household':sl1['No. households'].sum()},ignore_index=True)
        
        
        for i in range(len(sl)):
            for j in range(0,2):
                if j==0:
                    smry=smry.append({'Branch Type':f'Parent {i+1}(Before Splitting)','Name':sl['Parent Branch'][i],'Total No. of Villages':sl['Gp Name'][i].sum(),'Total No. of Villages with Portfolio':sl['No_groups'][i].sum(),
                                      'Total POS':sl['pos'][i].sum(),'Total Clients':sl['clients'][i].sum(),'Total PAR(LKH)':sl['Par amount'][i].sum(),'Total OD Clients':sl['Od Members'][i].sum(),'No.of Household':sl['No. households'][i].sum()},ignore_index=True)
                else:
                    smry=smry.append({'Branch Type':f'Parent {i+1}(After Splitting)','Name':sl['Parent Branch'][i],'Total No. of Villages':sl['Gp Name'][i].sum()-sl1['Gp Name'][i].sum(),'Total No. of Villages with Portfolio':sl['No_groups'][i].sum()-sl1['No_groups'][i].sum(),
                                      'Total POS':sl['pos'][i].sum()-sl1['pos'][i].sum(),'Total Clients':sl['clients'][i].sum()-sl1['clients'][i].sum(),'Total PAR(LKH)':sl['Par amount'][i].sum()-sl1['Par amount'][i].sum(),'Total OD Clients':sl['Od Members'][i].sum()-sl1['Od Members'][i].sum(),'No.of Household':sl['No. households'][i].sum()-sl1['No. households'][i].sum()},ignore_index=True)
                
                    
        smry['Total POS']=smry['Total POS']/10000000
        smry['Total PAR(LKH)']=smry['Total PAR(LKH)']/100000    
        st.write('Your File is ready to Download')
        st.download_button(label='Summary Table',data=smry.to_csv(index=False),file_name='summary_table.csv') 
        
    except:
        st.write('Something is wrong with the column names or data error')