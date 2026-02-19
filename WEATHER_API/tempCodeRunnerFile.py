def display_weather(self, data):
        temperature_k= data["main"]["temp"] 
        print(temperature_k) 
        temperature_c = temperature_k - 273.15
        temp_f = (temperature_k * 9/5) - 459.67 
        print(temperature_c)