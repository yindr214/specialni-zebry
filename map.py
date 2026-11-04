import streamlit as st

# souradnice namesti hrdinu v Olomouci
dt = {"lat": [49.593777,], "long": [17.250879,],}

st.map(dt, latitude="lat", longitude="long", zoom=10,)