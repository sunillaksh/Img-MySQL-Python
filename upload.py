import mysql.connector

def insert_image_into_database(image_path):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username',
            password='your_password',
            database='trydb'
        )

        cursor = connection.cursor()
        with open(image_path, 'rb') as file:
            image_data = file.read()
        sql = "INSERT INTO try (img) VALUES (%s)"
        values = (image_data,)
        cursor.execute(sql, values)
        connection.commit()

        print("Image inserted successfully!")

    except mysql.connector.Error as error:
        print("Failed to insert image into MySQL database: {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

insert_image_into_database("D:\my.jpg")

