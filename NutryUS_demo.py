import streamlit as st
st.title('NutryUS')
st.image('https://image.shutterstock.com/image-photo/best-menu-healthy-body-collage-260nw-1679266360.jpg')
st.header('Your new diet Dormitory Mother')
st.write("**Open the sidebar the type of meal on your left top corner to select **")
genre = st.sidebar.selectbox(
     "Meal:",
     ('None','Breakfast','Lunch','Dinner'))
st.write('**You selected:**', genre)
if genre == 'Breakfast':
  #st.subheader('Device:- ',genre)
  st.write('Idly')
  st.image('https://mk0geekrobocook3p2m6.kinstacdn.com/wp-content/uploads/2021/03/30_Idly.jpg')
  S1=st.slider('Idly Quantity',0,5,step=1)
  calories_idly = 1
  st.write('Dosa')
  #st.image('https://gepig.com/game_cover_460w/297.jpg')
  S2=st.slider('Dosa Quantity',0,5,step=1)
  calories_dosa = 1
  st.write('Breadtoast')
  #st.image('https://images-na.ssl-images-amazon.com/images/I/51-IGGUe5ZL.png')
  S3=st.slider('Breadtoast Quantity',0,5,step=1)
  calories_breadtoast = 1
  st.write('Poori')
  #st.image('https://i.ytimg.com/vi/detvL9SECGQ/maxresdefault.jpg')
  S4=st.slider('Poori Quantity',0,5,step=1)
  calories_poori = 1
  st.write('Omelet and Boiled Egg')
  #st.image('https://img.redbull.com/images/c_crop,w_1350,h_900,x_0,y_0,f_auto,q_auto/c_scale,w_1500/redbullcom/2017/06/01/1331859375452_2/tekken-7-heihachi-kazuya.jpg.jpg')
  S5=st.slider('Omelet Quantity',0,5,step=1)
  S6=st.slider('Boiled Egg Quantity', 0,5,step=1)
  calories_omelt = 1
  calories_boiledegg = 1
  st.write('Vada')
  #st.image('https://img.redbull.com/images/c_crop,w_1350,h_900,x_0,y_0,f_auto,q_auto/c_scale,w_1500/redbullcom/2017/06/01/1331859375452_2/tekken-7-heihachi-kazuya.jpg.jpg')
  S7=st.slider('Vada Quantity',0,5,step=1)
  calories_vada = 1
  breakfast_calories = S1*calories_idly + S2*calories_dosa + S3*calories_breadtoast + S4*calories_poori + S5*calories_omelt + S6*calories_boiledegg + S7*calories_vada
  st.write('Breakfast Calories = {}'.format(breakfast_calories)) 

# LUNCH SECTION ( To be edited )

elif genre == 'Lunch':
  st.write('Idly')
  st.image('https://mk0geekrobocook3p2m6.kinstacdn.com/wp-content/uploads/2021/03/30_Idly.jpg')
  S1=st.slider('Idly Quantity',0,5,step=1)
  calories_idly = 1
  st.write('Dosa')
  #st.image('https://gepig.com/game_cover_460w/297.jpg')
  S2=st.slider('Dosa Quantity',0,5,step=1)
  calories_dosa = 1
  st.write('Breadtoast')
  #st.image('https://images-na.ssl-images-amazon.com/images/I/51-IGGUe5ZL.png')
  S3=st.slider('Breadtoast Quantity',0,5,step=1)
  calories_breadtoast = 1
  st.write('Poori')
  #st.image('https://i.ytimg.com/vi/detvL9SECGQ/maxresdefault.jpg')
  S4=st.slider('Poori Quantity',0,5,step=1)
  calories_poori = 1
  st.write('Omelet and Boiled Egg')
  #st.image('https://img.redbull.com/images/c_crop,w_1350,h_900,x_0,y_0,f_auto,q_auto/c_scale,w_1500/redbullcom/2017/06/01/1331859375452_2/tekken-7-heihachi-kazuya.jpg.jpg')
  S5=st.slider('Omelet Quantity',0,5,step=1)
  S6=st.slider('Boiled Egg Quantity', 0,5,step=1)
  calories_omelt = 1
  calories_boiledegg = 1
  st.write('Vada')
  #st.image('https://img.redbull.com/images/c_crop,w_1350,h_900,x_0,y_0,f_auto,q_auto/c_scale,w_1500/redbullcom/2017/06/01/1331859375452_2/tekken-7-heihachi-kazuya.jpg.jpg')
  S7=st.slider('Vada Quantity',0,5,step=1)
  calories_vada = 1
  breakfast_calories = S1*calories_idly + S2*calories_dosa + S3*calories_breadtoast + S4*calories_poori + S5*calories_omelt + S6*calories_boiledegg + S7*calories_vada
  st.write('Breakfast Calories = {}'.format(breakfast_calories))
     
 # DINNER SECTION  (To be edited)
  
elif genre == 'Dinner':
  st.write('Idly')
  st.image('https://mk0geekrobocook3p2m6.kinstacdn.com/wp-content/uploads/2021/03/30_Idly.jpg')
  S1=st.slider('Idly Quantity',0,5,step=1)
  calories_idly = 1
  st.write('Dosa')
  #st.image('https://gepig.com/game_cover_460w/297.jpg')
  S2=st.slider('Dosa Quantity',0,5,step=1)
  calories_dosa = 1
  st.write('Breadtoast')
  #st.image('https://images-na.ssl-images-amazon.com/images/I/51-IGGUe5ZL.png')
  S3=st.slider('Breadtoast Quantity',0,5,step=1)
  calories_breadtoast = 1
  st.write('Poori')
  #st.image('https://i.ytimg.com/vi/detvL9SECGQ/maxresdefault.jpg')
  S4=st.slider('Poori Quantity',0,5,step=1)
  calories_poori = 1
  st.write('Omelet and Boiled Egg')
  #st.image('https://img.redbull.com/images/c_crop,w_1350,h_900,x_0,y_0,f_auto,q_auto/c_scale,w_1500/redbullcom/2017/06/01/1331859375452_2/tekken-7-heihachi-kazuya.jpg.jpg')
  S5=st.slider('Omelet Quantity',0,5,step=1)
  S6=st.slider('Boiled Egg Quantity', 0,5,step=1)
  calories_omelt = 1
  calories_boiledegg = 1
  st.write('Vada')
  #st.image('https://img.redbull.com/images/c_crop,w_1350,h_900,x_0,y_0,f_auto,q_auto/c_scale,w_1500/redbullcom/2017/06/01/1331859375452_2/tekken-7-heihachi-kazuya.jpg.jpg')
  S7=st.slider('Vada Quantity',0,5,step=1)
  calories_vada = 1
  breakfast_calories = S1*calories_idly + S2*calories_dosa + S3*calories_breadtoast + S4*calories_poori + S5*calories_omelt + S6*calories_boiledegg + S7*calories_vada
  st.write('Breakfast Calories = {}'.format(breakfast_calories))
