import numpy as np 
import random
import panda as pd

def fuzzy_weather(temp):
    if temp > 30:
        return 'Very Sunny'
    elif 20 <= temp <= 30:
        return  'Sunny'
    else:
        return 'Cloudy'
    
def transition_probability(current_weather):
    if current_weather == 'Very Sunny' :
        return[0.0, 1.0, 0.0] #[cloud, sunny, very sunny]
    elif current_weather ==  'Sunny':
        return[0.0, 0.8, 0.2]
    else:
        return [0.4, 0.6, 0.0]

def simulate_weather(num_days, initial_temp):
    weather_states = ['Cloudy','Sunny', 'Very Sunny']
    current_weather = fuzzy_weather(initial_temp)

    weather_sequence = []

    for _ in range(num_days):
        weather_sequence.append(current_weather)

    probality = transition_probability(current_weather)

    current_weather = random.choices(weather_states, weight=probality)[0]
    weather_sequence.append(current_weather)
    
    return weather_sequence


def save_to_excel(weather_sequence, filename)
    df = pd.DataFrame(weather_sequence, columns=["Weather"])
    df.to_excel(filename, index=False)

weather_sequence = simulate_weather(10, 25)
print("weater forecast for the next day : ",weather_sequence)

#save to excel
save_to_excel(weather_sequence, "weather_forecast.xlsx")
print("weather forecast saved")
