import sqlite3

# Connection to Database
con = sqlite3.connect("youtube_videos.db")

# Cursor
cursor = con.cursor()

# Create Table
cursor.execute("CREATE TABLE IF NOT EXISTS videos (id INTEGER PRIMARY KEY, name TEXT NOT NULL, time TEXT NOT NULL)")


# Method - list_videos
def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)


# Method - add_video
def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    con.commit()


# Method - update_video
def update_video(id, name, time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, id))
    con.commit()


# Method - delete_video
def delete_video(id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (id,))
    con.commit()



# Main Method
def main():
    while True:
        print("\n Youtube Manager App with DB")
        print("1. List All Youtube Videos")
        print("2. Add a Youtube Video")
        print("3. Update a Youtube Video Details")
        print("4. Delete a Youtube Video")
        print("5. Exit the App")
        choice = input("Enter your choice : ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter Video Name : ")
            time = input("Enter Video Time/Duration : ")
            add_video(name=name, time=time)
        elif choice == '3':
            id = int(input("Enter Video ID to Update Details : "))
            name = input("Enter Video Name : ")
            time = input("Enter Video Time/Duration : ")
            update_video(id=id, name=name, time=time)
        elif choice == '4':
            id = int(input("Enter Video ID to Delete : "))
            delete_video(id=id)
        elif choice == '5':
            break
        else:
            print("Invalid Choice!!")
    
    con.close()             # Database Connection Close

            

# Entry Point
if __name__ == "__main__":
    main()
