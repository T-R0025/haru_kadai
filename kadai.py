import tkinter as tk
import random
import time

word_list = [
    "apple", "banana", "cherry", "fish", "elephant", "look", "menu", "dog", 
    "cat", "jungle", "sleep", "lemon", "mountain", "tea", "hand", "piano", 
    "head", "rainbow", "sunshine", "red", "blue", "green", "white", "black", "yellow", "zebra"
]

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        master.geometry('400x400')
        master.title('タイピングゲーム')

        self.create_widgets()

        self.target_word = ""  
        self.user_input = ""  
        self.correct_count = 0  
        self.total_words = 5  
        self.word_index = 0  
        self.start_time = None 
        self.game_active = False  

        master.bind("<KeyPress>", self.on_key_press)  

    def create_widgets(self):
        self.label = tk.Label(self, text="スタートボタンを押して開始", font=("Arial", 14))
        self.label.pack(pady=10)

        self.word_label = tk.Label(self, text="準備完了", font=("Arial", 20, "bold"), fg="blue")
        self.word_label.pack(pady=10)

        self.input_label = tk.Label(self, text="", font=("Arial", 16), fg="gray") 
        self.input_label.pack(pady=10)

        self.score_label = tk.Label(self, text="スコア: 0", font=("Arial", 14))
        self.score_label.pack(pady=10)

        self.start_button = tk.Button(self, text="スタート", font=("Arial", 14), command=self.start_game)
        self.start_button.pack(pady=10)

    def start_game(self):
        """ ゲームを開始する """
        self.correct_count = 0
        self.word_index = 0
        self.start_time = time.time()  
        self.game_active = True  
        self.user_input = ""  

        self.label.config(text="キーボードで入力してください！", fg="black")
        self.score_label.config(text="スコア: 0")
        self.word_label.config(text="", fg="blue")
        self.input_label.config(text="", fg="gray")

        self.start_button.config(state="disabled")  
        self.next_word()  
    def next_word(self):
        """ 次の単語を表示 """
        if self.word_index < self.total_words:
            self.target_word = random.choice(word_list)
            self.word_label.config(text=self.target_word, fg="blue")
            self.input_label.config(text="", fg="gray")  
            self.user_input = ""  
            self.word_index += 1
        else:
            self.end_game()

    def on_key_press(self, event):
        """ キーが押された時の処理 """
        if not self.game_active:
            return  

        key = event.keysym 
        if len(key) == 1:  
            self.user_input += key

        if key == "BackSpace":  
            self.user_input = self.user_input[:-1]

        self.input_label.config(text=self.user_input)

        if self.user_input == self.target_word:
            self.correct_count += 1
            self.score_label.config(text=f"スコア: {self.correct_count}")
            self.next_word()

    def end_game(self):
        """ ゲーム終了時の処理 """
        self.game_active = False  
        elapsed_time = time.time() - self.start_time  
        wpm = (self.correct_count / elapsed_time) * 60  
        result_text = f" ゲーム終了！ \n正解数: {self.correct_count}/{self.total_words}\n" \
                      f"経過時間: {elapsed_time:.2f} 秒\n" \
                      f"入力速度: {wpm:.2f} WPM\nEnterキーで再スタート"

        self.word_label.config(text="ゲーム終了！", fg="red")
        self.label.config(text=result_text, fg="black")
        self.input_label.config(text="")  
        self.start_button.config(state="normal")  

        self.master.bind("<Return>", lambda event: self.start_game())

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
