import streamlit as st
import time

# Title
st.title("Business Dashboard with Streamlit Layouts")

# Objective
msg = "## Objective: To demonstrate the usage of columns, tabs, and dynamic containers in a business dashboard."
st.write(msg)


# Columns Layout
col1, col2, col3 = st.columns(3)

with col1:
  st.header("Header")
