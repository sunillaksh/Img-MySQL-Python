import mysql.connector
from mysql.connector import Error
from PIL import Image

# Function to retrieve and save the image
def retrieve_image():
    try:
        # Connect to MySQL database
        connection = mysql.connector.connect(host='localhost',
                                             database='trydb',
                                             user='your_username',
                                             password='your_password')

        if connection.is_connected():
            # Create a cursor object
            cursor = connection.cursor()

            # Execute the query to retrieve the image
            cursor.execute("SELECT img FROM try LIMIT 1")
            result = cursor.fetchone()

            if result is not None:
                # Save the image to a file
                image_data = result[0]
                with open('retrieved_image.jpg', 'wb') as file:
                    file.write(image_data)

                print("Image retrieved and saved successfully.")
            else:
                print("No image found in the database.")

    except Error as e:
        print("Error while connecting to MySQL database:", e)

    finally:
        # Close database connection
        if connection.is_connected():
            cursor.close()
            connection.close()

# Call the function to retrieve the image
retrieve_image()
