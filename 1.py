import tkinter as tk
from PIL import Image, ImageTk
import psutil
import os
import time
import threading
import random
import configparser  
b = 0

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')


splash_image_path = config.get('Paths', 'splash_image_path')
app_path = config.get('Paths', 'app_path')
process_name = os.path.basename(app_path)  

def check_process():

    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == process_name:
            return True  
    return False  

def launch_app_and_monitor(splash_window):
    os.startfile(app_path)
    a = random.randint(6, 8)
    time.sleep(a)
    splash_window.quit()


    time.sleep(1)






def create_splash_screen(image_path):

    root = tk.Tk()  
    root.title("启动画面")  
    root.overrideredirect(True)  
    window_width = 650  
    window_height = 400  
    root.attributes("-topmost", True)  
    screen_width = root.winfo_screenwidth() 
    screen_height = root.winfo_screenheight()  
    x_position = (screen_width - window_width) // 2  
    y_position = (screen_height - window_height) // 2  
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")  
    image = Image.open(image_path)  
    image = image.resize((window_width, window_height), Image.LANCZOS) 
    tk_image = ImageTk.PhotoImage(image)  
    label = tk.Label(root, image=tk_image)  
    label.pack()  
    threading.Thread(target=launch_app_and_monitor, args=(root,), daemon=True).start()  
    
    root.mainloop()  

if __name__ == "__main__":
    if os.path.exists(splash_image_path):  
        create_splash_screen(splash_image_path)  
    else:
        print(f"无法找到启动画面图片: {splash_image_path}")  