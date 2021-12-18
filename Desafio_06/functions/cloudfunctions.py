import json
import sys
import requests

def requestPrevisaoTempo():
    response_API = requests.get('https://api.weather.com/v3/wx/forecast/daily/15day?geocode=-21.170401,-47.810326&format=json&units=m&language=pt-BR&apiKey=29d0c2b003114c4790c2b003115c479c')
    data = response_API.text
    parse_json = json.loads(data)
    return parse_json  

def requestAgricultura(crop):
    response_API = requests.get(f'https://api.weather.com/v3/wx/forecast/hourly/agriculture/15day?geocode=-21.170401,-47.810326&format=json&units=m&apiKey=cffd036144be47edbd036144be47ed02&crop={crop}:50')
    data = response_API.text
    parse_json = json.loads(data)
    return parse_json  
    
def main(dict):
    try:
        tempo = requestPrevisaoTempo()    
        temperaturas = "Minimas: " + str(tempo['temperatureMin']) + " / Maximas: " + str(tempo['temperatureMax'])
        velVento     = "Velocidade do Vento: " + str(tempo['daypart'][0]['windSpeed'])
        dirVento     = "Direcao do Vento: " + str(tempo['daypart'][0]['windDirection'])
    
        agricultura = requestAgricultura('coffee')    
        evapoCoffee = "Evapotranspiração da próxima hora para o cultivo de café: " + str(agricultura['forecasts1Hour']['evapotranspirationCrop'][0])
    
        agricultura = requestAgricultura('corn')    
        evapoCorn = "Evapotranspiração da próxima hora para o cultivo de milho: " + str(agricultura['forecasts1Hour']['evapotranspirationCrop'][0])
    
        agricultura = requestAgricultura('soybeans')    
        evapoSoybeans = "Evapotranspiração da próxima hora para o cultivo de soja: " + str(agricultura['forecasts1Hour']['evapotranspirationCrop'][0])
        
        return { 'temperaturas': temperaturas, 
                 'velVento': velVento, 
                 'dirVento': dirVento, 
                 'evapoCoffee': evapoCoffee, 
                 'evapoCorn': evapoCorn, 
                 'evapoSoybeans': evapoSoybeans} 
    except:
        result = []
        
    return { 'result': result }         

if __name__ == "__main__":
    dict = {}
    result = main(dict)    
    print(result)