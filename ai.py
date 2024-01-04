# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 15:03:13 2022

@author: aman_
"""
import streamlit as st
import folium,requests
from streamlit_folium import st_folium




def app():
    
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
                  background: url("https://www.dropbox.com/s/jlx09kphsjz9rq7/ai.jpg?raw=1");
                  background-size: cover
              }}
              </style>
              """,
              unsafe_allow_html=True
          )
    set_bg_hack_url() 
    
    
    st.header('')
    st.write("""
    # AI Field Detection 
    """)
    
   
    
    uniquestate= ['Punjab']
    sidebar = st.sidebar
    a = sidebar.selectbox(
        "Select a State",
        uniquestate
)
   
    
    
    def get_pos(lat, lng):
        return lat, lng

        
   
    m =  folium.Map(location=[31.02564, 75.3719],
               zoom_start=8
             )
    
    folium.TileLayer(
        tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        attr = 'Esri',
        name = 'Esri Satellite',
        overlay = False,
        control = True
       ).add_to(m)
    
    map = st_folium(m, height=480, width=700)

    data = None
    st.markdown(f"<span style='color: red;'>Please click on the map to get coordinates/Currently Viewing State of {a}</span>", unsafe_allow_html=True)
    data = None
    if map.get("last_clicked"):
        data = get_pos(map["last_clicked"]["lat"], map["last_clicked"]["lng"])
    
    if data is not None:
        data = st.text_input('Your last clicked or Enter Coordinates',str(data)[1:-1])
    
    if st.button('Process'):  
       gif_runner = st.image('https://media.giphy.com/media/dwaeIbBnF6HBu/giphy.gif') 
       data=data.split(',')
       lat=data[0]
       long=data[1] 
       vv=requests.get(f'https://de60c7fe9a09fd312d33f322aa0b345d.serveo.net/ai/?x1={long}&y1={lat}') 
       # image = Image.open(r"D:\heroku\demo.jpg")
       # st.image(image, caption=str(vv.content),use_column_width=True)
       # st.write('The given coordinate is a'+vv.content)
       pp=str(float(long)+float(lat))+'.gif'
       st.components.v1.html(vv.text.replace(f'<img src="/static/images/{pp}"',f'<img src="https://de60c7fe9a09fd312d33f322aa0b345d.serveo.net/static/images/{pp}"').replace(f'<img src="/static/images/{pp1}"',f'<img src="https://de60c7fe9a09fd312d33f322aa0b345d.serveo.net/static/images/{pp1}"'),height=800)
       gif_runner.empty()
        
        

   
    # map = st_folium(m, height=350, width=700)
    # print(map['bounds'])



 
