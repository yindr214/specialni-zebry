import streamlit as st

dt = {"lat": [49.593777, 49.5984577], "long": [17.250879, 17.2313347], "col": ["#ffffff", "#4726FF"]}

st.map(dt, latitude="lat", longitude="long", zoom=10, color="col")