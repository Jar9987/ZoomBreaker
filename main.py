import os
import cv2
import pytube
from pyvirtualcam import Camera
import sys

# Hàm đổi tên cửa sổ
os.system('Premium | BREAKER zoom TOOL|discord.gg/XpTPM4pJU3)')

# Hàm tải video từ YouTube
def download_youtube_video():
    url = input("Enter URL Youtube: ")
    try:
        yt = pytube.YouTube(url)
        stream = yt.streams.get_highest_resolution()
        video_path = f"bin\\video\\{yt.title}.mp4"
        stream.download(output_path="bin\\video", filename=f"{yt.title}.mp4")
        print(f"ENJOY SUCCESFUl")
        return video_path
    except Exception as e:
        print(f"error {e}")
        return None

# Hàm chọn video từ thư mục bin/video
def select_video_from_folder():
    folder_path = "bin\\video"
    try:
        videos = [f for f in os.listdir(folder_path) if f.endswith(('.mp4', '.avi', '.mkv'))]
        if not videos:
            print("There are no videos in the bin\video folder.")
            return None

        print("List Video:")
        for idx, video in enumerate(videos, start=1):
            print(f"[{idx}] {video}")

        choice = int(input("choice video: "))
        if 1 <= choice <= len(videos):
            return os.path.join(folder_path, videos[choice - 1])
        else:
            print("invaild choice")
            return None
    except Exception as e:
        print(f"error: {e}")
        return None

# Hàm phát video dưới dạng webcam
def play_video_as_webcam(video_path):
    try:
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            print("can't open videos.")
            return

        print("Starting Enjoy...")
        with Camera(width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                    height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
                    fps=int(cap.get(cv2.CAP_PROP_FPS))) as cam:
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                cam.send(frame)
                cam.sleep_until_next_frame()

        cap.release()
        print("Stop Video")
    except Exception as e:
        print(f"Error: {e}")

# Hàm tham gia Zoom
def join_zoom():
    join_id = input("Enter join ID: ")
    password = input("Enter password (press Enter to skip): ")
    zoom_command = f"start zoommtg://zoom.us/join?action=join&confno={join_id}"
    if password:
        zoom_command += f"&pwd={password}"
    os.system(zoom_command)
    print("Joining Zoom...")

# Menu chính
def main():
    while True:
        print("\033[92m" + """
██████████████ ██████████████ ██████████████ ███████████████████████
            ██ ██          ██ ██          ██ ██        ██         ██   
          ██   ██          ██ ██          ██ ██        ██         ██     
        ██     ██          ██ ██          ██ ██        ██         ██        
      ██       ██          ██ ██          ██ ██        ██         ██
    ██         ██          ██ ██          ██ ██        ██         ██
█████████████  ██████████████ ██████████████ ██        ██         ██
""" + "\033[0m")
        print("""
=====================================|
| tool pha zoom v1 made by minhnhat  |
|    [1] Video in url youtube        |
|    [2] video in       bin\video    |
|    [3] join zoom [beta]            |
|    [4] exit                        |
|====================================|
        """)
        choice = input("Choice (1234): ")

        if choice == "1":
            video_path = download_youtube_video()
            if video_path:
                play_video_as_webcam(video_path)

        elif choice == "2":
            video_path = select_video_from_folder()
            if video_path:
                play_video_as_webcam(video_path)

        elif choice == "3":
            join_zoom()

        elif choice == "4":
            print("Quitting...")
            sys.exit()

        else:
            print("Invaild Choice.")

if __name__ == "__main__":
    main()
