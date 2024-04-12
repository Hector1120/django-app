import requests
import os

def get_data(category):
    os.system("clear") #Clear screen
    print("::: SOLAR SYSTEM INFORMATION:::")
    if category == '1':
        api_url = "https://api.le-systeme-solaire.net/rest/bodies/lune"
    elif category == '2':
        api_url = ""  # Pon la URL correcta para obtener información sobre las lunas
    elif category == '3':
        api_url = ""  # Pon la URL correcta para obtener información sobre las estrellas
    elif category == '4':
        api_url = ""  # Pon la URL correcta para obtener información sobre los asteroides
    elif category == '5':
        api_url = ""  # Pon la URL correcta para obtener información sobre los cometas
    else:
        print("Invalid option")
        return None
    
    try:
        #Solicitud a la API
        response = requests.get(api_url)
        response.raise_for_status() #si hay un error   
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"API error {e}")

def print_menu():
    print("[1] Planets")
    print("[2] Moons")
    print("[3] Stars")
    print("[4] Asteroid")
    print("[5] Comets")
    

#Principal
while True:
    print_menu()
    choice = input("Choose an option (1/2/3/4/5): ")
    info = get_data(choice)
    if info:
        if 'name' in info:
            print("EnglishName:", info['englishName'])
        else:
            print("Name not found in data.")
        if 'name' in info:
            print("Gravity:", info['gravity'])
        else:
            print("Gravity not found in data.")
    input("Press Enter to continue...")
