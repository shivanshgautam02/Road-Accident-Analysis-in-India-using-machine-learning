import streamlit as st
import leafmap.foliumap as leafmap
import pickle
import pandas as pd
import subprocess


#st.title('Road Accident Analysis') 
    
with open(r'random_forest_model.pkl', 'rb') as f:
        model = pickle.load(f)

input_features = ['age_band_of_driver', 'vehicle_type', 'age_of_vehicle', 'weather_conditions', 'day_of_week', 'road_surface_conditions', 'light_conditions', 'sex_of_driver','season','speed_limit']


weather_map = {
        'Fine no high winds': 1,
        'Raining no high winds': 5,
        'Snowing no high winds': 7,
        'Fine + high winds': 0,
        'Raining + high winds': 4,
        'Snowing + high winds': 6,
        'Fog or mist': 2,
        'Unknown': 3,
        'Other': 3
    }

light_map = {
        'Daylight': 3,
        'Darkness - lights lit': 0,
        'Darkness - lights unlit': 1,
        'Darkness - no lighting': 2
    }

season_map = {
        'Winter': 3,
        'Summer': 2,
        'Rainy': 1,
        'Autumn': 0
    }

vehicle_map = {
        'Car': 1,
        'Goods Vehicle': 2,
        'Motorcycle': 3,
        'Other Vehicle': 4,
        'Bus':0
    }
age_map = {
        'Under 16': 4,
        '16-25': 0,
        '26-45': 1,
        '46-65': 2,
        'Over 65':3
    }
road_sufrace_condition_map = {
        'Dry': 1,
        'Wet or damp': 5,
        'Snow': 4,
        'Frost or ice': 3,
        'Flood over 3cm. deep':2,
        'Mud':0  ##mud
    }
week_map = {
        'Sunday': 3,
        'Monday': 1,
        'Tuesday': 5,
        'Wednesday': 6,
        'Thursday': 4,
        'Friday': 0,
        'Saturday': 2
    }
def preprocess_input(input_df):
        input_df['weather_conditions'] = input_df['weather_conditions'].map(weather_map)
        input_df['light_conditions'] = input_df['light_conditions'].map(light_map)
        input_df['season'] = input_df['season'].map(season_map)
        input_df['vehicle_type'] = input_df['vehicle_type'].map(vehicle_map)
        input_df['sex_of_driver'] = input_df['sex_of_driver'].apply(lambda x: 1 if x=='Male' else 0)
        input_df['road_surface_conditions'] = input_df['road_surface_conditions'].map(road_sufrace_condition_map)
        input_df['age_band_of_driver'] = input_df['age_band_of_driver'].map(age_map)
        input_df['day_of_week'] = input_df['day_of_week'].map(week_map)
        return input_df

    # Define the web application

    # Run the web application


def app():
        st.markdown("<h1 style='text-align: center;'>Road Accident Prediction</h1>", unsafe_allow_html=True)
        
    
        # Create the input form for the user
        age_band_of_driver = st.selectbox('Age Band of Driver', options=list(age_map.keys()))
        vehicle_type = st.selectbox('Vehicle Type', options=['Car', 'Goods Vehicle', 'Motorcycle', 'Other Vehicle', 'Bus'])
        age_of_vehicle = st.number_input('Age of Vehicle', min_value=0, step=1)
        weather_conditions = st.selectbox('Weather Conditions', options=list(weather_map.keys()))
        day_of_week = st.selectbox('Week Days', options=list(week_map.keys()))
        road_surface_conditions = st.selectbox('Road Surface Conditions',options=list(road_sufrace_condition_map.keys()) )
        light_conditions = st.selectbox('Light Conditions', options=list(light_map.keys()))
        sex_of_driver = st.selectbox('Sex of Driver', options=['Male', 'Female'])
        season = st.selectbox('Season', options=list(season_map.keys()))
        speed_limit = st.number_input('Speed Limit', min_value=10, step=10)
    # Prepare the inputs
        if st.button("Predict"):
            inputs = pd.DataFrame({
                'age_band_of_driver': [age_band_of_driver],
                'vehicle_type': [vehicle_type],
                'age_of_vehicle': [age_of_vehicle],
                'weather_conditions': [weather_conditions],
                'day_of_week': [day_of_week],
                'road_surface_conditions': [road_surface_conditions],
                'light_conditions': [light_conditions],
                'sex_of_driver': [sex_of_driver],
                'season': [season],
                'speed_limit': [speed_limit]
                })
            inputs = preprocess_input(inputs)
            inputs = inputs.reindex(columns=input_features, fill_value=0)
    
            # Predict the accident seriousness using the loaded model
            prediction = model.predict(inputs)[0]
            #st.write(prediction)
            # Display the prediction
            # st.write('## Prediction')
    
            if prediction == 1:
                st.write("The accident is not serious.")
            elif prediction == 2:
                st.write("The accident is serious.")
            elif prediction == 0:
                st.write("The accident is fatal.")






