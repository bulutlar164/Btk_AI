import random
import os

minValue = 10
maxValue = 50

coordinates = [
    ("Ankara,Kızılcahamam", 40.4694, 32.6478),
    ("Ankara,Çamlıdere", 40.4747, 32.4744),
    ("Ankara,Kalecik", 40.0963, 33.4094),
    ("Ankara,Çubuk", 40.2386, 33.0333),
    ("Ankara,Akyurt", 40.1339, 33.0861),
    ("Ankara,Ayaş", 40.0133, 32.3467),
    ("Ankara,Elmadağ", 39.9236, 33.2297),
    ("Ankara,Haymana", 39.4346, 32.4978),
    ("Ankara,Bala", 39.5509, 33.1238),
    ("Ankara,Polatlı", 39.5771, 32.1414),
    ("Ankara,Gölbaşı", 39.7896, 32.8139),
    ("Ankara,Beypazarı", 40.1672, 31.9217),
    ("Ankara,Nallıhan", 40.1865, 31.3548),
    ("Ankara,Çankaya", 39.9117, 32.8597),
    ("Ankara,Altındağ", 39.9441, 32.8634),
    ("Ankara,Yenimahalle", 39.9684, 32.7909),
    ("Ankara,Keçiören", 39.9833, 32.8666),
    ("Ankara,Mamak", 39.9205, 32.9489),
    ("Ankara,Etimesgut", 39.9316, 32.6691),
    ("Ankara,Sincan", 39.9619, 32.5609),
    ("Ankara,Evren", 39.0167, 33.7250)
]

AddLenghtMin = 0.001
AddLenghtMax = 0.005

def get_damage_status(damage_level):
    print()
    if damage_level == 2:
        return "Ağır"
    elif damage_level == 1:
        return "Orta"
    elif damage_level == 0:
        return "Hafif"
    else:
        return "Geçersiz Değer"
    
def get_random_coordinate():
    return random.choice(coordinates)


def random_number():
    return random.randint(minValue,maxValue)


def get_random_coordinate():
    return random.choice(coordinates)

def get_add_random_cordinates(latitude,longitude):
    rnla = latitude + random.uniform(AddLenghtMin,AddLenghtMax)
    rnlo = longitude + random.uniform(AddLenghtMin,AddLenghtMax)
    rnla = round(rnla,4)
    rnlo = round(rnlo,4)
    return rnla,rnlo

def create_file_path(directory, image_name):
    base_name = f"{image_name}"
 
    file_path = os.path.join(directory, base_name)
    return file_path

