# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 12:26:18 2022

@author: THIS-LAPPY
"""
import streamlit as st,numpy as np
import streamlit.components.v1 as components
import requests,io,pandas as pd

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
    #   Equifax Processor
        Please provide your path containing equifax csv's. 
    """)
    multiple_files = st.file_uploader(
    "Multiple File Uploader",
    accept_multiple_files=True
)
    cwp,cws,pwd,pwd,pwp,pws=[],[],[],[],[],[]
    for file in multiple_files:
        file_container = st.expander(
            f"File name: {file.name} ({file.size})"
        )
        data = io.BytesIO(file.getbuffer())
        gg=pd.read_csv(data,header=1,sep='\t',encoding="utf-16").fillna(0)
        kk= "".join([ s[0] for s in file.name.split()]).lower()
        if kk[0:3]=='cwp':
            cwp=gg
        if kk[0:3]=='cws':
            cws=gg
        if kk[0:3]=='cwd':
            cwd=gg
        if kk[0:3]=='pwd':
            pwd=gg
            pwd=pwd[0:len(pwd)-1]
            pwd['Pincode']=pwd['Pincode'].astype(int)
            cl=['1+ Delinquency Balance','1+ Delinquency Balance.1','1+ Delinquency Balance.2','1+ Delinquency Balance.3','1+ Delinquency Balance.4',
                '30+ Delinquency Balance','30+ Delinquency Balance.1','30+ Delinquency Balance.2','30+ Delinquency Balance.3','30+ Delinquency Balance.4',
                '180+ Delinquency Balance','180+ Delinquency Balance.1','180+ Delinquency Balance.2','180+ Delinquency Balance.3','180+ Delinquency Balance.4'
                ]
            pwd[cl]=pwd[cl].astype(str)
            for i in range(len(cl)):
                pwd[cl[i]]=pwd[cl[i]].apply(lambda x:x.replace(',','')).astype('int64')
            
        if kk[0:3]=='pwp':
            pwp=gg    
            pwp=pwp[0:len(pwp)-1]
            pwp['Pincode']=pwp['Pincode'].astype(int)
            cl=['O/S Balance','O/S Balance.1','O/S Balance.2','O/S Balance.3','O/S Balance.4','O/S Balance.5']
            pwp[cl]=pwp[cl].astype(str)
            for i in range(len(cl)):
                pwp[cl[i]]=pwp[cl[i]].apply(lambda x:x.replace(',','')).astype('int64')    
            
        if kk[0:3]=='pws':
            cl=['Average Ticket Size','Average Ticket Size.1','Average Ticket Size.2','Average Ticket Size.3','Average Ticket Size.4','No. of Loans','No. of Loans.1','No. of Loans.2','No. of Loans.3','No. of Loans.4','Disbursed Amount','Disbursed Amount.1','Disbursed Amount.2','Disbursed Amount.3','Disbursed Amount.4']
            pws=gg
            pws=pws[0:len(pws)-1]
            pws['Pincode']=pws['Pincode'].astype(int)
            pws[cl]=pws[cl].astype(str)
            for i in range(len(cl)):
                pws[cl[i]]=pws[cl[i]].apply(lambda x:x.replace(',','')).astype('int64')
            
    if st.button('Process'):        
        if (len(cwp)==0) or (len(cws)==0) or (len(cwd)==0) or (len(pwd)==0) or (len(pwp)==0) or (len(pws)==0):
           st.warning('Something is wrong with the file contents or Namespace') 
        else:
            pass
            st.write('Your File is ready to Download')
            if len(cwp)>1:
               pwp=pwp.merge(pws[['Pincode','Average Ticket Size','Average Ticket Size.1','Average Ticket Size.2','Average Ticket Size.3','Average Ticket Size.4','No. of Loans','No. of Loans.1','No. of Loans.2','No. of Loans.3','No. of Loans.4','Disbursed Amount','Disbursed Amount.1','Disbursed Amount.2','Disbursed Amount.3','Disbursed Amount.4']],on='Pincode', how='left').fillna(0)  
               pwp=pwp.merge(pwd[['Pincode','1+ Delinquency Balance','1+ Delinquency Balance.1','1+ Delinquency Balance.2','1+ Delinquency Balance.3','1+ Delinquency Balance.4',
                   '30+ Delinquency Balance','30+ Delinquency Balance.1','30+ Delinquency Balance.2','30+ Delinquency Balance.3','30+ Delinquency Balance.4',
                   '180+ Delinquency Balance','180+ Delinquency Balance.1','180+ Delinquency Balance.2','180+ Delinquency Balance.3','180+ Delinquency Balance.4']],on='Pincode', how='left').fillna(0)
               
               nae=pd.DataFrame({'State':pwp['State'],'District':pwp['District'],'Pincode':pwp['Pincode'],
                                'p1_p':pwp['O/S Balance'],'p2_p':pwp['O/S Balance.1'],'p3_p':pwp['O/S Balance.2'],'p4_p':pwp['O/S Balance.3'],'p5_p':pwp['O/S Balance.4'],
                                'p1_t':pwp['Average Ticket Size'],'p2_d':pwp['Average Ticket Size.1'],'p3_d':pwp['Average Ticket Size.2'],'p4_d':pwp['Average Ticket Size.3'],'p5_d':pwp['Average Ticket Size.4'],
                                'p1_d':pwp['No. of Loans'],'p2_t':pwp['No. of Loans.1'],'p3_t':pwp['No. of Loans.2'],'p4_t':pwp['No. of Loans.3'],'p5_t':pwp['No. of Loans.4'],
                                'p1_do%':(pwp['Disbursed Amount'].div(pwp['O/S Balance'].where(pwp['O/S Balance'] != 0,0)))*100,'p2_do%':(pwp['Disbursed Amount.1'].div(pwp['O/S Balance.1'].where(pwp['O/S Balance.1'] != 0,0)))*100,'p3_do%':(pwp['Disbursed Amount.2'].div(pwp['O/S Balance.2'].where(pwp['O/S Balance.2'] != 0,0)))*100,'p4_do%':(pwp['Disbursed Amount.3'].div(pwp['O/S Balance.3'].where(pwp['O/S Balance.3'] != 0,0)))*100,'p5_do%':(pwp['Disbursed Amount.4'].div(pwp['O/S Balance.4'].where(pwp['O/S Balance.4'] != 0,0)))*100,
                                'p1_1%':(pwp['1+ Delinquency Balance'].div(pwp['O/S Balance'].where(pwp['O/S Balance'] != 0,0)))*100,'p2_1%':(pwp['1+ Delinquency Balance.1'].div(pwp['O/S Balance.1'].where(pwp['O/S Balance.1'] != 0,0)))*100,'p3_1%':(pwp['1+ Delinquency Balance.2'].div(pwp['O/S Balance.2'].where(pwp['O/S Balance.2'] != 0,0)))*100,'p4_1%':(pwp['1+ Delinquency Balance.3'].div(pwp['O/S Balance.3'].where(pwp['O/S Balance.3'] != 0,0)))*100,'p5_1%':(pwp['1+ Delinquency Balance.4'].div(pwp['O/S Balance.4'].where(pwp['O/S Balance.4'] != 0,0)))*100,
                                'p1_3%':(pwp['30+ Delinquency Balance'].div(pwp['O/S Balance'].where(pwp['O/S Balance'] != 0,0)))*100,'p2_3%':(pwp['30+ Delinquency Balance.1'].div(pwp['O/S Balance.1'].where(pwp['O/S Balance.1'] != 0,0)))*100,'p3_3%':(pwp['30+ Delinquency Balance.2'].div(pwp['O/S Balance.2'].where(pwp['O/S Balance.2'] != 0,0)))*100,'p4_3%':(pwp['30+ Delinquency Balance.3'].div(pwp['O/S Balance.3'].where(pwp['O/S Balance.3'] != 0,0)))*100,'p5_3%':(pwp['30+ Delinquency Balance.4'].div(pwp['O/S Balance.4'].where(pwp['O/S Balance.4'] != 0,0)))*100,
                                'p1_8%':(pwp['180+ Delinquency Balance_y'].div(pwp['O/S Balance'].where(pwp['O/S Balance'] != 0,0)))*100,'p2_8%':(pwp['180+ Delinquency Balance.1_y'].div(pwp['O/S Balance.1'].where(pwp['O/S Balance.1'] != 0,0)))*100,'p3_8%':(pwp['180+ Delinquency Balance.2_y'].div(pwp['O/S Balance.2'].where(pwp['O/S Balance.2'] != 0,0)))*100,'p4_8%':(pwp['180+ Delinquency Balance.3_y'].div(pwp['O/S Balance.3'].where(pwp['O/S Balance.3'] != 0,0)))*100,'p5_8%':(pwp['180+ Delinquency Balance.4_y'].div(pwp['O/S Balance.4'].where(pwp['O/S Balance.4'] != 0,0)))*100
                                }).fillna(0)
                
               st.download_button(label='Download New_Area_Expansion',data=nae.to_csv(index=False),file_name='New_Area_Expansion.csv')   
           
               
    st.write("### Code")

