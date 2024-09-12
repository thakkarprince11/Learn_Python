
import json                         # Importing json

# Function load_data
def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            test_data = json.load(file)
            #print(test_data)
            #print(type(test_data))
            return test_data
    except FileNotFoundError:
        return []



# Function save_data_helper
def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)



# Function list_all_videos
def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. Name : {video['name']}, Duration : {video['time']}")
    print("*" * 70)



# Function add_video
def add_video(videos):
    name = input("Enter Video Name : ")
    time = input("Enter Video Time/Duration : ")
    videos.append({'name': name, 'time' : time})
    save_data_helper(videos=videos)



# Function update_video
def update_video(videos):
    list_all_videos(videos=videos)
    index = int(input("Enter the video number to update : "))
    if 1 <= index <= len(videos):
        name = input("Enter New Video Name : ")
        time = input("Enter New Video Time/Duration : ")
        videos[index - 1] = {'name' : name, 'time' : time}
        save_data_helper(videos=videos)
    else:
        print("Invalid Index Selected!!")



# Function update_video
def delete_video(videos):
    list_all_videos(videos=videos)
    index = int(input("Enter Video Number to be Deleted : "))
    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data_helper(videos=videos)
    else:
        print("Invalid Index Selected!!")





# Main entry-point
def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | Choose an option : ")
        print("1. List All Youtube Videos")
        print("2. Add a Youtube Video")
        print("3. Update a Youtube Video Details")
        print("4. Delete a Youtube Video")
        print("5. Exit the App")
        choice = input("Enter your choice : ")
        #print(videos)

        # Match - instead of If Else
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice")



# dunder - a method that has double underscores before and after its name
# If function's name is 'main' in file anywhere then run the main function
if __name__ == "__main__":
    main()




