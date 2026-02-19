import sys
from urllib import response
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton,QLineEdit
from PyQt5.QtCore import Qt
class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter City Name:", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temprature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.InitUI()
        
        
    def InitUI(self):
        self.setWindowTitle("Weather App")
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temprature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        
        self.setLayout(vbox)
        
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temprature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)
        
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temprature_label.setObjectName("temprature_label") 
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")
        
        self.setStyleSheet("""
                           QLabel,QPushButton {
                               font-family: Arial;}
                              QLabel#city_label {
                                  font-size: 45px;
                                  font-style: italic;
                                  }
                                QLineEdit#city_input {
                                    font-size: 45px;}
                                QPushButton#get_weather_button { 
                                font-size: 45px;
                                font-weight: bold;}
                                QLabel#temprature_label {
                                    font-size: 70px;
                                    font-weight: bold;
                                    } 
                                QLabel#emoji_label {
                                    font-size: 100px;
                                    font-family: "Segoe UI Emoji"; 
                                    }   
                                  QLabel#description_label {
                                      font-size: 45px;
                                  """)
        
        self.get_weather_button.clicked.connect(self.get_weather)
    
    def  get_weather(self):
        api_key = "e63d87d69b16c4aa5fb54e080317e4aa"
        city = self.city_input.text()
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        
        try:
            reponse = requests.get(url)
            reponse.raise_for_status()
            data = reponse.json()
            
            if data["cod"] == 200:
                self.display_weather(data)
            else:
                self.display_error("City not found")
                
                
        except requests.exceptions.HTTPError as http_error:
            match http_error.response.status_code:
                case 400:
                    print("Bad Request: City not found")
                case 401:
                    print("Unauthorized\ninvalid API key")
                case 403:
                    print("Forbidden\nAccess denied")
                case 404:
                    print("Not Found\nCity not found")
                case 500:
                    print("Internal Server Error\nTry again later")
                case 502:
                    print("Bad Gateway\nTry again later") 
                case 503:
                    print("Service Unavailable\nTry again later")
                case 504:
                    print("Gateway Timeout\nTry again later") 
                    
                case _:
                    print(f"HTTP Error\n {http_error}")                              
        except requests.exceptions.RequestException as e:
            pass    
           
    
    def display_error(self, message):
        pass
        
    def display_weather(self, data):
        print(data)    
        
        
        
        
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())        
    