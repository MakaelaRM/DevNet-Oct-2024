import streamlit as st
import altair as alt
import csv_methods
import get_file

#gets file data
file_id = '1eARZ0iioA7GDm1fb_b5Vc9gLhVxxxibf'
csv_name = 'downloaded_file.csv'

csv_file = get_file.download_csv(file_id, csv_name)
    
#sets page up
st.set_page_config(
    page_title='Plant Dashboard',
    page_icon='🌱',
    layout='wide',
    initial_sidebar_state='expanded'
)

st.title('𓋼𓍊 Plant Dashboard 𓍊𓋼')
    
#displays data
st.markdown('MCR Scottsdale LLC')
col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)

#add units?
#first input is last data entry second input gets difference between that value and second to last one
col1.metric("Date & Time:", csv_methods.get_value(csv_name, 'date_time'))
col2.metric("pH:", csv_methods.get_value(csv_name, ' pH'), csv_methods.get_value_diff(csv_name, ' pH'))
col3.metric("EC:", csv_methods.get_value(csv_name, 'EC'), int(csv_methods.get_value_diff(csv_name, 'EC')))
col4.metric("PPM:", csv_methods.get_value(csv_name, 'PPM'), int(csv_methods.get_value_diff(csv_name, 'PPM')))
col5.metric("Temprature:", csv_methods.get_value(csv_name, 'Temp'), float(csv_methods.get_value_diff(csv_name, 'Temp')))
col6.metric("Humidity:", csv_methods.get_value(csv_name, 'Humidity'), int(csv_methods.get_value_diff(csv_name, 'Humidity')))