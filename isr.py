# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 16:27:55 2022

@author: THIS-LAPPY
"""

import streamlit as st,numpy as np
import streamlit.components.v1 as components
import requests,io,pandas as pd,gc

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
    #   ISR Processor
        Please provide your path containing only equifax peer wise csv's. 
    """)
    multiple_files = st.file_uploader(
    "Multiple File Uploader",
    accept_multiple_files=True
)
    pwd,pwp,pws=[],[],[]
    
    for file in multiple_files:
        file_container = st.expander(
            f"File name: {file.name} ({file.size})"
        )
        data = io.BytesIO(file.getbuffer())
        gg=pd.read_csv(data,header=1,sep='\t',encoding="utf-16").fillna(0)
        kk= "".join([ s[0] for s in file.name.split()]).lower()
        if kk[0:3]=='pwp':
            pwp=gg    
            pwp=pwp[0:len(pwp)-1]
            pwp['Pincode']=pwp['Pincode'].astype(int)
            cl=['O/S Balance.1','O/S Balance.4','O/S Balance.5','Active Loans.1','Active Loans.4','No. of Institutions..1','No. of Institutions..4','No. of Institutions..5','180+ Delinquency Balance.1','180+ Delinquency Balance.4','180+ Delinquency Balance.5']
            pwp[cl]=pwp[cl].astype(str)
            for i in range(len(cl)):
                try:
                    pwp[cl[i]]=pwp[cl[i]].apply(lambda x:x.replace(',','')).astype('int64')
                except:
                    pass
        if kk[0:3]=='pwd':
            pwd=gg
            pwd=pwd[0:len(pwd)-1]
            pwd['Pincode']=pwd['Pincode'].astype(int)
            cl=['1+ Delinquency Balance.1','1+ Delinquency Balance.4','1+ Delinquency Balance.5','30+ Delinquency Accounts.1','30+ Delinquency Accounts.4','30+ Delinquency Accounts.5','30+ Delinquency Balance.1','30+ Delinquency Balance.4','30+ Delinquency Balance.5','60+ Delinquency Balance.1','60+ Delinquency Balance.4','60+ Delinquency Balance.5','180+ Delinquency Balance.1','180+ Delinquency Balance.4','180+ Delinquency Balance.5']
            pwd[cl]=pwd[cl].astype(str)
            for i in range(len(cl)):
                try:
                    pwd[cl[i]]=pwd[cl[i]].apply(lambda x:x.replace(',','')).astype('int64')  
                except:
                    pass
        if kk[0:3]=='pws':
            cl=['Disbursed Amount.1','Disbursed Amount.4','Disbursed Amount.5', 'No. of Institutions.1', 'No. of Institutions.4', 'No. of Institutions.5','No. of Loans.1','No. of Loans.4','No. of Loans.5','Average Ticket Size.1','Average Ticket Size.4','Average Ticket Size.5']
            pws=gg
            pws=pws[0:len(pws)-1]
            pws['Pincode']=pws['Pincode'].astype(int)
            pws[cl]=pws[cl].astype(str)
            for i in range(len(cl)):
                try:
                    pws[cl[i]]=pws[cl[i]].apply(lambda x:x.replace(',','')).astype('int64')        
                except:
                    pass
                
    if st.button('Process'):        
        if (len(pwd)==0) or (len(pwp)==0) or (len(pws)==0):
           st.warning('Something is wrong with the file contents or Namespace') 
        else:
            if len(pwp)>1:
               try: 
                   gif_runner = st.image('light.gif')
                   pwp=pwp.merge(pws[['Pincode','Disbursed Amount.1','Disbursed Amount.4','Disbursed Amount.5', 'No. of Institutions.1', 'No. of Institutions.4', 'No. of Institutions.5','No. of Loans.1','No. of Loans.4','No. of Loans.5','Average Ticket Size.1','Average Ticket Size.4','Average Ticket Size.5']],on='Pincode', how='left').fillna(0)  
                   pwp=pwp.merge(pwd[['Pincode','1+ Delinquency Balance.1','1+ Delinquency Balance.4','1+ Delinquency Balance.5','30+ Delinquency Accounts.1','30+ Delinquency Accounts.4','30+ Delinquency Accounts.5','30+ Delinquency Balance.1','30+ Delinquency Balance.4','30+ Delinquency Balance.5','60+ Delinquency Balance.1','60+ Delinquency Balance.4','60+ Delinquency Balance.5','180+ Delinquency Balance.1','180+ Delinquency Balance.4','180+ Delinquency Balance.5']],on='Pincode', how='left').fillna(0)
                   
                   single1=pwp['1+ Delinquency Balance.1']+pwp['1+ Delinquency Balance.4']
                   single2=(pwp['O/S Balance.1']+pwp['O/S Balance.4'])+(pwp['180+ Delinquency Balance.1_x']+pwp['180+ Delinquency Balance.4_x'])
                   nae=pd.DataFrame({'State':pwp['State'],'District':pwp['District'],'Pincode':pwp['Pincode'],
                                     'ActiveMFIs':pwp['No. of Institutions..1'].astype(float)+pwp['No. of Institutions..4'].astype(float),'ActiveLNS':pwp['Active Loans.1']+pwp['Active Loans.4'],'POS':pwp['O/S Balance.1']+pwp['O/S Balance.4'],'180+DelBal':pwp['180+ Delinquency Balance.1_x']+pwp['180+ Delinquency Balance.4_x'],'RiskPOS':(pwp['O/S Balance.1']+pwp['O/S Balance.4'])+(pwp['180+ Delinquency Balance.1_x']+pwp['180+ Delinquency Balance.4_x']),
                                     'DisbMFI':pwp['No. of Institutions.1'].astype(float)+pwp['No. of Institutions.4'].astype(float),'DisbAcc':pwp['No. of Loans.1']+pwp['No. of Loans.4'],'DisbAmt':pwp['Disbursed Amount.1']+pwp['Disbursed Amount.4'],'DisbATS':pwp['Average Ticket Size.1']+pwp['Average Ticket Size.4'],
                                     '1-30DelBal':(pwp['1+ Delinquency Balance.1']-pwp['30+ Delinquency Balance.1'])+(pwp['1+ Delinquency Balance.4']-pwp['30+ Delinquency Balance.4']),'30-179DelBal':pwp['30+ Delinquency Balance.1']+pwp['30+ Delinquency Balance.4'],'30-60DelBal':(pwp['30+ Delinquency Balance.1']-pwp['60+ Delinquency Balance.1'])+(pwp['30+ Delinquency Balance.4']-pwp['60+ Delinquency Balance.4']),'60-179DelBal':pwp['60+ Delinquency Balance.1']+pwp['60+ Delinquency Balance.4'],'180+DelBal_1':pwp['180+ Delinquency Balance.1_y']+pwp['180+ Delinquency Balance.4_y'],'1-179DelBal':pwp['1+ Delinquency Balance.1']+pwp['1+ Delinquency Balance.4'],'1-179DPD%':(single1.div(single2.where(single2!= 0,0)))*100
                                     }).fillna(0).replace([np.inf, -np.inf], 0)
                    
                   pp=['1-179DPD%']
                   nae[pp]=np.where(nae[pp]>100,100,nae[pp])
                   
                   total1=pwp['1+ Delinquency Balance.5']
                   total2=pwp['O/S Balance.5']+pwp['180+ Delinquency Balance.5_x']
                   nae1=pd.DataFrame({'State':pwp['State'],'District':pwp['District'],'Pincode':pwp['Pincode'],
                                     'ActiveMFIs':pwp['No. of Institutions..5'],'ActiveLNS':pwp['Active Loans.5'],'POS':pwp['O/S Balance.5'],'180+DelBal':pwp['180+ Delinquency Balance.5_x'],'RiskPOS':pwp['O/S Balance.5']+pwp['180+ Delinquency Balance.5_x'],
                                     'DisbMFI':pwp['No. of Institutions.5'],'DisbAcc':pwp['No. of Loans.5'],'DisbAmt':pwp['Disbursed Amount.5'],'DisbATS':pwp['Average Ticket Size.5'],
                                     '1-30DelBal':pwp['1+ Delinquency Balance.5']-pwp['30+ Delinquency Balance.5'],'30-179DelBal':pwp['30+ Delinquency Balance.5'],'30-60DelBal':pwp['30+ Delinquency Balance.5']-pwp['60+ Delinquency Balance.5'],'60-179DelBal':pwp['60+ Delinquency Balance.5'],'180+DelBal_1':pwp['180+ Delinquency Balance.5_y'],'1-179DelBal':pwp['1+ Delinquency Balance.5'],'1-179DPD%':(total1.div(total2.where(total2!= 0,0)))*100
                                     }).fillna(0).replace([np.inf, -np.inf], 0)
                   

                   nae1[pp]=np.where(nae1[pp]>100,100,nae[pp])
                   st.write('Your File is ready to Download')
                   st.download_button(label='P1+P2',data=nae.to_csv(index=False),file_name='p1_p2.csv') 
                   st.download_button(label='Total',data=nae1.to_csv(index=False),file_name='total.csv')   
                   gif_runner.empty()  
               except:
                    st.write('Something gone wrong with ISR Processing') 
               
             
                
                
