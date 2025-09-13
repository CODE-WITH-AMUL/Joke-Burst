#-----------------[IMPORT MODEL]-----------------#
import os
import json
import random
from win10toast import ToastNotifier
from rich.console import Console

#-----------------[IMPORT MODEL]-----------------#
def automation():
    try:
        image_path = 'data/icon.ico' 
        console = Console()
        with open('jokes.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        category = random.choice(list(data.keys()))
        joke = random.choice(data[category])
        notification = ToastNotifier()
        console.print(f"[{category.upper()}] {joke}", style="green")
        notification.show_toast("Joke !", joke, icon_path=image_path, duration=10)  
    except Exception as e:
        print(str(e))
        print("Error While processing")

#-----------------[END]-----------------#
if __name__ == "__main__":
    automation()
