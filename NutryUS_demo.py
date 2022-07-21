import streamlit as st
import math as mt
st.title('NutryUS')
st.image('https://image.shutterstock.com/image-photo/best-menu-healthy-body-collage-260nw-1679266360.jpg')
st.header('Your new diet Dormitory Mother')
st.write("**Open the sidebar the type of meal on your left top corner to select **")
genre = st.sidebar.selectbox(
     "Meal:",
     ('None','Breakfast','Lunch','Dinner'))
### Calculating BMI of a person
weight = st.number_input('Enter your weight in kg')
height = st.number_input('Enter your height in m')
bmi = (weight)/(height**2)
### Calories based on bmi
if bmi == inf:
     st.write('Enter correct height and weight details')
elif bmi > 16.0 and bmi < 18.5:
     st.write('Based on your BMI, you need to consume 3000 Calories per day')
elif bmi > 18.5 and bmi < 25:
     st.write('Based on your BMI, you need to consume 2500 Calories per day')
elif bmi > 25 and bmi < 40:
     st.write('Based on your BMI, you need to consume 2300 Calories per day')
     
breakfast_calories, lunch_calories, dinner_calories = 0, 0, 0
st.write('**You selected:**', genre)
if genre == 'Breakfast':
  st.write('Idly')
  st.image('https://mk0geekrobocook3p2m6.kinstacdn.com/wp-content/uploads/2021/03/30_Idly.jpg')
  S1=st.slider('Idly Quantity',0,5,step=1)
  calories_idly = 78
  st.write('Dosa')
  #st.image('https://gepig.com/game_cover_460w/297.jpg')
  S2=st.slider('Dosa Quantity',0,5,step=1)
  calories_dosa = 154
  st.write('Breadtoast')
  #st.image('https://images-na.ssl-images-amazon.com/images/I/51-IGGUe5ZL.png')
  S3=st.slider('Breadtoast Quantity',0,5,step=1)
  calories_breadtoast = 97
  st.write('Poori')
  #st.image('https://i.ytimg.com/vi/detvL9SECGQ/maxresdefault.jpg')
  S4=st.slider('Poori Quantity',0,5,step=1)
  calories_poori = 134
  st.write('Omelet and Boiled Egg')
  #st.image('https://img.redbull.com/images/c_crop,w_1350,h_900,x_0,y_0,f_auto,q_auto/c_scale,w_1500/redbullcom/2017/06/01/1331859375452_2/tekken-7-heihachi-kazuya.jpg.jpg')
  S5=st.slider('Omelet Quantity',0,5,step=1)
  S6=st.slider('Boiled Egg Quantity', 0,5,step=1)
  calories_omelt = 127
  calories_boiledegg = 77
  st.write('Vada')
  #st.image('https://img.redbull.com/images/c_crop,w_1350,h_900,x_0,y_0,f_auto,q_auto/c_scale,w_1500/redbullcom/2017/06/01/1331859375452_2/tekken-7-heihachi-kazuya.jpg.jpg')
  S7=st.slider('Vada Quantity',0,5,step=1)
  calories_vada = 155
  breakfast_calories = S1*calories_idly + S2*calories_dosa + S3*calories_breadtoast + S4*calories_poori + S5*calories_omelt + S6*calories_boiledegg + S7*calories_vada
  st.write('Breakfast Calories = {}'.format(breakfast_calories)) 

# LUNCH SECTION ( To be edited )

elif genre == 'Lunch':
  st.text('Quantity is taken in terms of Bowls')
  st.write('Chicken Biryani Bowl')
  #st.image('https://mk0geekrobocook3p2m6.kinstacdn.com/wp-content/uploads/2021/03/30_Idly.jpg')
  S1=st.slider('Biryani Bowl Quantity',0,5,step=1)
  calories_Biryani = 389
  st.write('Rice and Dal Bowl')
  #st.image('https://gepig.com/game_cover_460w/297.jpg')
  S2=st.slider('Rice and Dal Bowl Quantity',0,5,step=1)
  calories_Dal = 298
  st.write('Panner Rice Bowl')
  #st.image('https://images-na.ssl-images-amazon.com/images/I/51-IGGUe5ZL.png')
  S3=st.slider('Panner Rice Bowl Quantity',0,5,step=1)
  calories_Panner_rice = 380
  st.write('Mutton Rice Bowl')
  #st.image('https://i.ytimg.com/vi/detvL9SECGQ/maxresdefault.jpg')
  S4=st.slider('Mutton Rice Bowl Quantity',0,5,step=1)
  calories_Mutton = 388
  st.write('Grilled Fish')
  #st.image('https://img.redbull.com/images/c_crop,w_1350,h_900,x_0,y_0,f_auto,q_auto/c_scale,w_1500/redbullcom/2017/06/01/1331859375452_2/tekken-7-heihachi-kazuya.jpg.jpg')
  S5=st.slider('Grilled Fish',0,5,step=1)
  calories_Grilled_Fish = 186
  st.write('Soya Curry with Rice Bowl')
  #st.image('https://img.redbull.com/images/c_crop,w_1350,h_900,x_0,y_0,f_auto,q_auto/c_scale,w_1500/redbullcom/2017/06/01/1331859375452_2/tekken-7-heihachi-kazuya.jpg.jpg')
  S6=st.slider('Soya Curry with Rice Bowl',0,5,step=1)
  calories_Soya = 350
  st.write('Apricot Delight for dessert')
  #st.image('')
  S7=st.slider('Apricot Delight Quantity', 0,5,step=1)
  calories_apricot = 97
  lunch_calories = S1*calories_Biryani + S2*calories_Dal + S3*calories_Panner_rice + S4*calories_Mutton + S5*calories_Grilled_Fish + S6*calories_Soya + S7*calories_apricot
  st.write('Lunch Calories = {}'.format(lunch_calories))
     
 # DINNER SECTION  (To be edited)
  
elif genre == 'Dinner':
  st.text('Quantity is taken in terms of Bowls')
  st.write('Jeera Rice')
  st.image('https://mk0geekrobocook3p2m6.kinstacdn.com/wp-content/uploads/2021/03/30_Idly.jpg')
  S1=st.slider('Jeera Rice Quantity',0,5,step=1)
  calories_Jeera = 296
  st.write('Curd Rice')
  #st.image('https://gepig.com/game_cover_460w/297.jpg')
  S2=st.slider('Curd Rice Quantity',0,5,step=1)
  calories_Curd = 283
  st.write('Butter Naan')
  #st.image('https://images-na.ssl-images-amazon.com/images/I/51-IGGUe5ZL.png')
  S3=st.slider('Butter Naan Quantity',0,5,step=1)
  calories_Naan = 271
  st.write('Roti')
  #st.image('https://i.ytimg.com/vi/detvL9SECGQ/maxresdefault.jpg')
  S4=st.slider('Roti Quantity',0,5,step=1)
  calories_Roti = 150
  st.write('Chapati')
  #st.image('https://img.redbull.com/images/c_crop,w_1350,h_900,x_0,y_0,f_auto,q_auto/c_scale,w_1500/redbullcom/2017/06/01/1331859375452_2/tekken-7-heihachi-kazuya.jpg.jpg')
  S5=st.slider('Chapati Quantity',0,5,step=1)
  #S6=st.slider('Boiled Egg Quantity', 0,5,step=1)
  calories_Chapati = 85
  #calories_boiledegg = 1
  st.write('Panner curry')
  #st.image('https://img.redbull.com/images/c_crop,w_1350,h_900,x_0,y_0,f_auto,q_auto/c_scale,w_1500/redbullcom/2017/06/01/1331859375452_2/tekken-7-heihachi-kazuya.jpg.jpg')
  S6=st.slider('Panner curry Quantity',0,5,step=1)
  calories_Panner_curry = 205
  st.write('Chicken curry')
  #st.image('https://img.redbull.com/images/c_crop,w_1350,h_900,x_0,y_0,f_auto,q_auto/c_scale,w_1500/redbullcom/2017/06/01/1331859375452_2/tekken-7-heihachi-kazuya.jpg.jpg')
  S7=st.slider('Chicken curry Quantity',0,5,step=1)
  calories_Chicken_curry = 271
  st.write('Mutton curry')
  #st.image('https://img.redbull.com/images/c_crop,w_1350,h_900,x_0,y_0,f_auto,q_auto/c_scale,w_1500/redbullcom/2017/06/01/1331859375452_2/tekken-7-heihachi-kazuya.jpg.jpg')
  S8=st.slider('Mutton curry Quantity',0,5,step=1)
  calories_Mutton_curry = 301
  dinner_calories = S1*calories_Jeera + S2*calories_Curd + S3*calories_Naan + S4*calories_Roti + S5*calories_Chapati + S6*calories_Panner_curry + S7*calories_Chicken_curry +S8*calories_Mutton_curry
  st.write('Dinner Calories = {}'.format(dinner_calories))
