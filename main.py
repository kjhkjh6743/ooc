import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import os

# 칵테일 데이터 (이미지 파일은 images 폴더에서 불러옴)
cocktails = {
    'Mojito': {'ingredients': ['rum', 'mint', 'lime', 'soda'], 'taste': 'refreshing', 'image': 'mojito.jpg'},
    'Martini': {'ingredients': ['gin', 'vermouth'], 'taste': 'dry', 'image': 'martini.jpg'},
    'Margarita': {'ingredients': ['tequila', 'lime', 'triple sec'], 'taste': 'sour', 'image': 'margarita.jpg'},
    'Cosmopolitan': {'ingredients': ['vodka', 'lime', 'cranberry'], 'taste': 'sweet', 'image': 'cosmopolitan.jpg'},
    'Old Fashioned': {'ingredients': ['whiskey', 'sugar', 'bitters'], 'taste': 'strong', 'image': 'old_fashioned.jpg'}
}

# 칵테일 이미지 파일 경로를 불러오는 함수
def load_image(image_name):
    image_path = os.path.join('images', image_name)  # 'images' 폴더에서 이미지 경로 생성
    if os.path.exists(image_path):  # 이미지 파일이 존재하는지 확인
        img = Image.open(image_path)
        img = img.resize((180, 180))  # 이미지 크기 고정
        return ImageTk.PhotoImage(img)
    else:
        print(f"이미지 파일 {image_name}을 찾을 수 없습니다.")
        return None

# 칵테일 추천 함수
def recommend_cocktail(keyword):
    results = []
    for name, details in cocktails.items():
        if keyword in details['ingredients'] or keyword in details['taste']:
            results.append(name)
    if results:
        return random.choice(results)
    else:
        return "No cocktail found with that keyword."

# 추천 버튼 클릭 시 동작
def on_search():
    keyword = entry.get().lower()  # 검색창에서 입력한 값
    if keyword:
        recommendation = recommend_cocktail(keyword)
        result_label.config(text=f"추천 칵테일: {recommendation}")
        
        # 해당 칵테일 이미지 로드 및 표시
        if recommendation != "No cocktail found with that keyword.":
            image_name = cocktails[recommendation]['image']
            cocktail_img = load_image(image_name)
            
            # 기존에 표시된 이미지를 지우기
            for widget in cocktail_image_frame.winfo_children():
                widget.grid_forget()  # grid에서 지우기

            # 새 이미지 표시
            cocktail_image_label = tk.Label(cocktail_image_frame, image=cocktail_img)
            cocktail_image_label.grid(row=0, column=0, padx=20, pady=10)
            cocktail_image_label.image = cocktail_img  # 이미지 참조 유지
        else:
            # 이미지가 없을 경우
            for widget in cocktail_image_frame.winfo_children():
                widget.grid_forget()  # grid에서 지우기
    else:
        messagebox.showwarning("Input Error", "키워드를 입력하세요.")

# Tkinter 윈도우 생성
root = tk.Tk()
root.title("칵테일 추천 프로그램")

# 배경화면 설정 (색상 변경)
root.configure(bg='#f0f8ff')  # 부드러운 색상으로 변경

# 창 크기 고정
root.resizable(False, False)

# UI 요소들
search_label = tk.Label(root, text="칵테일을 검색하세요:", bg='#f0f8ff', font=('Verdana', 14, 'bold'))
search_label.pack(pady=20)

# 깔끔한 디자인의 검색창
entry = tk.Entry(root, width=40, font=('Verdana', 12), borderwidth=2, relief="solid", bg='white', fg='black',
                 justify='center', bd=0)
entry.pack(pady=10)

# 추천 버튼
search_button = tk.Button(root, text="추천 받기", command=on_search, font=('Verdana', 12, 'bold'),
                          bg='#4CAF50', fg='white', relief="raised", padx=20, pady=5)
search_button.pack(pady=20)

# 추천 결과 라벨
result_label = tk.Label(root, text="추천 칵테일: ", bg='#f0f8ff', font=('Verdana', 16, 'bold'))
result_label.pack(pady=20)

# 술 이미지를 맨 아래에 배치
cocktail_image_frame = tk.Frame(root, bg='#f0f8ff')
cocktail_image_frame.pack(side="bottom", pady=30)  # 'bottom'으로 설정하여 맨 아래에 배치

# 처음에는 모든 이미지를 표시
cocktail_images = {}
for i, (name, details) in enumerate(cocktails.items()):
    cocktail_img = load_image(details['image'])
    cocktail_images[name] = cocktail_img
    cocktail_label = tk.Label(cocktail_image_frame, image=cocktail_img)
    cocktail_label.grid(row=i // 3, column=i % 3, padx=20, pady=10)
    cocktail_label.image = cocktail_img  # 이미지 참조 유지

# 창 크기 설정 (고정 크기)
root.geometry("950x800")  # 창 크기 고정

root.mainloop()
