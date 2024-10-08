import mysql.connector
import mysql

class Database:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def insert_prediction(self, predicted_class: int, people_random: int):
        insert_query_prediction = "INSERT INTO tbl_prediction (Prediction, PeopleRandom) VALUES (%s, %s)"

        self.cursor.execute(insert_query_prediction, (predicted_class, people_random))
        self.connection.commit()

    def insert_location(self,latitude,longitude,address,region,location_type):
        insert_query_location = "INSERT INTO locations (latitude,longitude,address,region,location_type) VALUES (%s, %s, %s, %s,%s)"

        self.cursor.execute(insert_query_location,(latitude,longitude,address,region,location_type))
        self.connection.commit()

    def insert_images(self,image_type,capture_date,file_path,latitude,longitude,processed):
        insert_query_location = "INSERT INTO images (image_type,capture_date,file_path,latitude,longitude,processed) VALUES (%s, %s, %s, %s, %s, %s)"

        self.cursor.execute(insert_query_location,(image_type,capture_date,file_path,latitude,longitude,processed))
        self.connection.commit()

    def select_locationid(self,latitude,longitude,address,region,location_type):
        select_query_locationid = "SELECT location_id FROM locations WHERE latitude = %s AND longitude = %s AND address = %s AND region = %s AND location_type = %s"

        self.cursor.execute(select_query_locationid,(latitude,longitude,address,region,location_type))
        result = self.cursor.fetchone()
        #print(result[0])
        return result[0]
    
    def select_imagesid(self,image_type,capture_date,file_path,latitude,longitude,processed):
        select_query_imagesid = "SELECT image_id FROM images WHERE image_type = %s AND capture_date = %s AND file_path = %s AND latitude = %s AND longitude = %s AND processed = %s"

        self.cursor.execute(select_query_imagesid,(image_type,capture_date,file_path,latitude,longitude,processed))
        result = self.cursor.fetchone()
        #print(result[0])
        return result[0]

    def insert_report(self,image_id,location_id,damage_type,severity):
        insert_query_report = "INSERT INTO damage_reports (image_id, location_id, damage_type, severity) VALUES (%s, %s, %s, %s)"
        
        self.cursor.execute(insert_query_report,(image_id,location_id,damage_type,severity))
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()
