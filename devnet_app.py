import streamlit as st
import altair as alt
import csv_methods
import get_file

#gets file data
file_id = '1eARZ0iioA7GDm1fb_b5Vc9gLhVxxxibf'
csv_name = 'downloaded_file.csv'
folder_id = '1PNm562W_IqKJ8Zxl8bz03p_yiEZoh88W'
image_name = 'plant_image.jpg'

csv_file = get_file.download_csv(file_id, csv_name)
plant_image = get_file.download_last_image_in_folder(folder_id, image_name)
    
#sets page up
st.set_page_config(
    page_title='Plant Dashboard',
    page_icon='🌱',
    layout='wide',
    initial_sidebar_state='expanded'
)

st.title('Plant Dashboard 🌱')

#sidebar
with st.sidebar:
    st.header("Settings")
    
    dates = csv_methods.get_column(csv_name, 'date_time')
    
    graph_data = st.selectbox("Select Graph:",
                                   ("pH", "EC", 'PPM', "Temprature", "Humidity"))
    
#displays data
st.markdown('MCR Scottsdale LLC')
col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)
col7 = st.columns(1)

#values
pH = csv_methods.get_value(csv_name, ' pH')
temp = (f'{csv_methods.get_value(csv_name, 'Temp')} °F')
ec = (f'{csv_methods.get_value(csv_name, 'EC')} µS/cm')
ppm = (f'{csv_methods.get_value(csv_name, 'PPM')} ppm')
humidity = (f'{csv_methods.get_value(csv_name, 'Humidity')} g/kg')

#first input is last data entry second input gets difference between that value and second to last one
col1.metric("Date & Time:", csv_methods.get_value(csv_name, 'date_time'))
col2.metric("pH:", pH, csv_methods.get_value_diff(csv_name, ' pH'))
col3.metric("EC:", ec, int(csv_methods.get_value_diff(csv_name, 'EC')))
col4.metric("PPM:", ppm, int(csv_methods.get_value_diff(csv_name, 'PPM')))
col5.metric("Temprature:", temp, float(csv_methods.get_value_diff(csv_name, 'Temp')))
col6.metric("Humidity:", humidity, int(csv_methods.get_value_diff(csv_name, 'Humidity')))

#data graphs
df = csv_methods.get_data(csv_name)
if(graph_data == "pH"):
    st.line_chart(data=df, x='date_time', y=' pH', x_label='Date', y_label='pH')
    
elif(graph_data == "EC"):
    st.line_chart(data=df, x='date_time', y='EC', x_label='Date', y_label='EC (µS/cm)')

elif(graph_data == "PPM"):
    st.line_chart(data=df, x='date_time', y='PPM', x_label='Date', y_label='PPM')
    
elif(graph_data == "Temprature"):
    st.line_chart(data=df, x='date_time', y='Temp', x_label='Date', y_label='Temprature (°F)')

elif(graph_data == "Humidity"):
    st.line_chart(data=df, x='date_time', y='Humidity', x_label='Date', y_label='Humidity (g/kg)')
    

#image
col7 = st.image(image_name)