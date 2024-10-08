from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from typing import List
from PIL import Image
import io
import numpy as np
import RandomAtt as rd
from tensorflow.keras.models import load_model
from fastapi.middleware.cors import CORSMiddleware
from databaseConnection import Database
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Gerekirse spesifik alan adları ile değiştir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#DatabaseConfiguration
db = Database(
    host="localhost",          
    user="root",               
    password="Huawei2024!",   
    database="tektokronik_db"    
)


# Modelinizi buraya yükleyin
model = load_model('model79_90_8.h5')
image_size = (256, 256)
channels = 1

ALLOWED_EXTENSIONS = {'.jpg', '.jpeg', '.png','.PNG'}

def allowed_file(filename: str) -> bool:
    return any(filename.endswith(ext) for ext in ALLOWED_EXTENSIONS)



@app.post("/upload-images/")
async def upload_images(files: List[UploadFile] = File(...)):
    results = []

    for file in files:
        if not allowed_file(file.filename):
            raise HTTPException(status_code=400, detail="Invalid file type. Only .jpg, .jpeg, and .png .PNG files are allowed.")

        rn = rd.random_number()
        image_data = await file.read()
        image = Image.open(io.BytesIO(image_data))
        image = image.convert("L")
        image = image.resize(image_size)

        img_array = np.array(image)
        img_array = np.expand_dims(img_array, axis=-1)
        img_array = img_array.astype(np.float32)

        x_input = np.zeros((1, image_size[0], image_size[1], channels), dtype=np.float32)
        x_input[0] = img_array

        predictions = model.predict(x_input)
        predicted_class = np.argmax(predictions, axis=1).tolist()

        #Locations Insert
        add,la,lo = rd.get_random_coordinate()
        la,lo = rd.get_add_random_cordinates(la,lo)
        dmg_string=rd.get_damage_status(predicted_class[0])
        #print(dmg_string)
        db.insert_location(la,lo,add,"Ankara",dmg_string)

        #Location ID found for another work
        location_id =db.select_locationid(la,lo,add,"Ankara",dmg_string)
        #print(location_id)

        #Image Insert
        directory_l = "btk/imageSave/edited/"  
        image_name_l = file.filename                                                          
        image_type_l= 'Drone'
        capture_date_G = datetime.now()
        capture_date_L = capture_date_G.strftime('%Y-%m-%d %H:%M:%S')
        #print(capture_date_L)
        file_path_l = rd.create_file_path(directory_l,image_name_l)
        #print(file_path_l)
        procedes_l = "1"
        db.insert_images(image_type_l,capture_date_L,file_path_l,la,lo,procedes_l)
        image_id = db.select_imagesid(image_type_l,capture_date_L,file_path_l,la,lo,procedes_l)
        #print(image_id)
        #Image Insert Final

        #Report Insert
        db.insert_report(image_id,location_id,"Bina",dmg_string)
        #Report Insert Fina

        #Genel Dönüş
        results.append({"predicted_class": predicted_class[0],"PeopleRandom": rn})



    return JSONResponse(content={"results": results})

def shutdown_event():
    db.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
