# import pymongo
from pymongo import MongoClient

from bson import ObjectId


client = MongoClient("mongodb+srv://Cluster35052:password@cluster0.vzzzx7s.mongodb.net/", tlsAllowInvalidCertificates=True)

# Database Name
db = client["ytmanager"]

# Collection
video_collection = db["videos"]
#print(video_collection)


# Function - List_Videos
def list_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name : {video['name']}, Time : {video['time']}")


# Function - add_video
def add_video(name, time):
    video_collection.insert_one({"name" : name, "time" : time})


# Function - update_video
def update_video(id, name, time):
    video_collection.update_one(
        {'_id' : ObjectId(id)}, 
        {
            "$set" : {
                "name" : name,
                "time" : time
            }
        }
        )


# Function - delete_video
def delete_video(id):
    video_collection.delete_one({'_id' : ObjectId(id)})


# Function - Main
def main():
    while True:
        print("\n Youtube Manager App MongoDB")
        print("1. List All Youtube Videos")
        print("2. Add a Youtube Video")
        print("3. Update a Youtube Video Details")
        print("4. Delete a Youtube Video")
        print("5. Exit the App")
        choice = input("Enter your choice : ")

        if choice == "1":
            list_videos()
        elif choice == "2":
            name = input("Enter Video Name : ")
            time = input("Enter Video Time/Duration : ")
            add_video(name=name, time=time)
        elif choice == "3":
            id = input("Enter Video Id to be updated : ")
            name = input("Enter Updated Video Name : ")
            time = input("Enter Updated Video Time/Duration : ")
            update_video(id=id, name=name, time=time)
        elif choice == "4":
            id = input("Enter Video Id to be updated : ")
            delete_video(id=id)
        elif choice == "5":
            break
        else:
            print("Invalid Choice!!")


# Main Entry Point
if __name__ == "__main__":
    main()