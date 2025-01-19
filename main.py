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
=====================================
| tool BREAKER ZOOM PREMIUM NEW      |
|    [1] Youtube Ulr                 |
|    [2] Video In bin\video          |
|    [3] Quit                        |
|====================================|
        """)
        choice = input("Choice (123): ")

        if choice == "1":
            video_path = download_youtube_video()
            if video_path:
                play_video_as_webcam(video_path)

        elif choice == "2":
            video_path = select_video_from_folder()
            if video_path:
                play_video_as_webcam(video_path)

        elif choice == "3":
            print("Qutiing...")
            sys.exit()

        else:
            print("Invaild Choice.")

if __name__ == "__main__":
    main()
