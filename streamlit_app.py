import streamlit

streamlit.title('My parents new healthy dinner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 omega 3 & blueberry oatmeal')
streamlit.text('🥗 kale,spinach & rocket smoothie')
streamlit.text('🐔 hard-boiled free-range egg')
streamlit.text(' 🥑🍞 avocado toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)


fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

#new display

streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +fruit_choice)
#streamlit.text(fruityvice_response.json())

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")



my_data_row = my_cur.fetchall()
streamlit.header("The Fruit load list contains:")
streamlit.dataframe(my_data_row)

streamlit.header("Fruityvice Fruit Advice!")
add_my_fruit= streamlit.text_input('What fruit would you like information about?','jackfruit')
streamlit.write('Thanks for adding', add_my_fruit)
