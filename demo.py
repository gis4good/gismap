# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 15:03:13 2022

@author: aman_
"""
import streamlit as st,numpy as np
import matplotlib.pyplot as plt
#import plotly.graph_objects as go
#import plotly.express as px
import base64
import folium
from streamlit_folium import st_folium,folium_static
import folium.plugins as plugins
from folium.plugins import MarkerCluster
import streamlit.components.v1 as components
#import bar_chart_race as bcr



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
                  background: url("https://i.pinimg.com/originals/b9/c8/f8/b9c8f893c9a782033a01f47e0c0b1d6e.jpg");
                  background-size: cover
              }}
              </style>
              """,
              unsafe_allow_html=True
          )
    set_bg_hack_url() 
    
    
    st.header('')
    st.write("""
    # Branch Split Dashboard
    Branches reaching splittable size as per POS. 
    """)
    
    import pandas as pd  
    df = pd.read_csv("data.csv")
    df.sort_values(by=['Value (in Cr)'], ascending=False)
    
    uniquestate= df['State'].unique()
    uniquestate=np.insert(uniquestate,0,'India')
    print('xyz')
    # a = st.sidebar.radio('Select State:',uniquestate)
    sidebar = st.sidebar
    a = sidebar.selectbox(
        "Select a State",
        uniquestate
)
   
    
    
    if a=='India':
       df=df.dropna().reset_index(drop=True)
       df['color']=0
       df['size']=0

    else:
    # df=df.query('State' == a)
        df=df[df['State']==a]
        df=df.sort_values(by=['Value (in Cr)'], ascending=False)
        df=df.dropna().reset_index(drop=True)
        df['color']=0
        df['size']=0

    def highlight_survived(s):
        return ['background-color: red']*len(s) if s['Value (in Cr)']>=10 else ['background-color: green']*len(s)
    
    def color_survived(val):
        if val>=10:
            color='red'
        elif val>=7 and val<10:
            color='#ff9900'
        else:
            color='green'
        
        return f'background-color: {color}'
    def color(val):
        if val>=10:
            color='red'
            size=6*1.5
        elif val>=7 and val<10:
            color='#ff9900'
            size=4*1.5
        else:
            color='green'
            size=4.5
        return color,size
    
    col5, col6 = st.columns((1,1))
    dff=df[['Branch', 'Value (in Cr)', 'Zone', 'State']]

    with col5:
        st.write(dff.style.hide_index().applymap(color_survived, subset=['Value (in Cr)']),height=450)

    with col6:
        m1=df[df['Value (in Cr)']>=10].count()[0]  
        m2=df[(df['Value (in Cr)']>=7) & (df['Value (in Cr)']<10)].count()[0]  
        m3=df[df['Value (in Cr)']<7].count()[0]  
        em=pd.DataFrame()
        em=em.append({'Level':'Max','Count':m1},ignore_index=True)
        em=em.append({'Level':'Moderate','Count':m2},ignore_index=True)
        em=em.append({'Level':'Low','Count':m3},ignore_index=True)
        fig = px.bar(
                em,
                x="Level",
                y="Count",
                color="Count",
                text="Count",
                title='Branch Portfolio',
                width=400,
                
            )
        
        fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor':'rgba(0, 0, 0, 0)','yaxis':dict(showgrid=False)})
        st.plotly_chart(fig)
        


    # fig_target = go.Figure(data=[go.Pie(labels=df['branch_2'][0:10],
    #                                 values=df['Value (in Cr)'][0:10],
    #                                 hole=.2)])
    # fig_target.update_layout(showlegend=False,
    #                           height=350,
    #                           margin={'l': 20, 'r': 60, 't': 20, 'b': 0},
    #                           plot_bgcolor= 'rgba(0, 0, 0, 0)',
    #                           paper_bgcolor= 'rgba(0, 0, 0, 0)')
    # fig_target.update_traces(textposition='inside', textinfo='label+percent')
    
    
    st.sidebar.markdown("## Top 10 Target Branches")
    # st.sidebar.plotly_chart(fig_target, use_container_width=True)
   
    th_props = [
   ('font-size', '14px'),
   ('text-align', 'center'),
   ('font-weight', 'bold'),
   ('color', 'blue'),
   ('background-color','rgba(0, 0, 0, 0)')
   ]

                                    
    td_props = [
   ('font-size', '12px')
   ]
                                 

    styles = [
   dict(selector="th", props=th_props),
   dict(selector="td", props=td_props)
   ]


    styler = dff[['Branch','Value (in Cr)']][0:9].style.hide_index().format(subset=['Value (in Cr)'], decimal=',', precision=2).bar(subset=['Value (in Cr)'], align="mid").set_table_styles(styles)


    st.sidebar.write(styler.to_html(), unsafe_allow_html=True)
    
    
    def add_categorical_legend(folium_map, title, colors, labels):
        if len(colors) != len(labels):
            raise ValueError("colors and labels must have the same length.")
    
        color_by_label = dict(zip(labels, colors))
        
        legend_categories = ""     
        for label, color in color_by_label.items():
            legend_categories += f"<li><span style='background:{color}'></span>{label}</li>"
            
  
    for j in range(len(df)):
        df['color'][j],df['size'][j]=color(df['Value (in Cr)'][j])
    
    if a=='India':
        m = folium.Map(location=[21.152280852164264, 79.07285347273053],
                  zoom_start=5,
                  preferCanvas=True,
                  tiles='cartodbdark_matter'
                )
    else:
        
        m = folium.Map(location=[df['lat'][0],df['lon'][0]],
                  zoom_start=8,
                  tiles='cartodbdark_matter'
                )
    pkobp_layer = folium.FeatureGroup(name="PKO BP SA")
    marker_cluster = MarkerCluster().add_to(pkobp_layer)
    for i in range(len(df)):
        html = f'''<body style="background-color:{df['color'][i]};"><p style="color:blue;">{df['Branch'][i]}</p>
        <p>Zone:{df['Zone'][i]}</p></body>'''
        
        iframe = folium.IFrame(html,
                               width=200,
                               height=80)
        # folium.CircleMarker([df['lat'][i], df['lon'][i]], radius=int(df['size'][i]), color=df['color'][i],popup= folium.Popup(iframe)).add_to(m)
        
        icon_url='https://media.giphy.com/media/Y0slbp1Hr4C8lUA5UG/giphy.gif'
        icon = folium.features.CustomIcon(icon_url,icon_size=(22, 22))  # Creating a custom Icon
        if df['Value (in Cr)'][i]>=10:
            folium.Marker(location=[df['lat'][i],df['lon'][i]],icon=icon,popup= folium.Popup(iframe),tooltip=folium.Tooltip(df['Branch'][i], permanent=True,style=("background-color: orange; color:white; font-family: arial; font-size: 10px; padding: 0px;fillColor:green;")
)).add_to(marker_cluster)   
        else:
            folium.CircleMarker([df['lat'][i], df['lon'][i]], radius=int(df['size'][i]), color=df['color'][i],popup= folium.Popup(iframe),tooltip=folium.Tooltip(df['Branch'][i], permanent=True,style=("background-color: green; color:white; font-family: arial; font-size: 10px; padding: 0px;")
)).add_to(marker_cluster)
        
    # folium.TileLayer('cartodbdark_matter').add_to(m)    
    m.add_child(pkobp_layer)
    # print(m.get_bounds())
    # m.add_child(folium.LatLngPopup())
    
    folium_static(m,width=762) 
    # map = st_folium(m, height=350, width=700)
    # print(map['bounds'])



 
