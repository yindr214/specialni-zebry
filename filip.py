import streamlit as st
cords = {"latitude":[49.6009864,49.5925828], "longitude":[17.2368431,17.2783775]}

st.map(cords, latitude="latitude", longitude="longitude", color="#375A97")

#49.5925828N, 17.2783775E