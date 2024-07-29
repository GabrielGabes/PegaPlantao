import tkinter as tk
from tkinter import messagebox
import time
import threading
import os

class ShutdownApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Desligar/Reiniciar Computador")

        self.time_var = tk.StringVar()
        self.action_var = tk.StringVar(value="desligar")
        self.cancel_event = threading.Event()

        tk.Label(root, text="Minutos:").grid(row=0, column=0, padx=5, pady=5)
        self.time_entry = tk.Entry(root, textvariable=self.time_var)
        self.time_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Radiobutton(root, text="Desligar", variable=self.action_var, value="desligar").grid(row=1, column=0, padx=5, pady=5)
        tk.Radiobutton(root, text="Reiniciar", variable=self.action_var, value="reiniciar").grid(row=1, column=1, padx=5, pady=5)

        self.start_button = tk.Button(root, text="Iniciar", command=self.start_countdown)
        self.start_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.cancel_button = tk.Button(root, text="Cancelar", command=self.cancel_countdown, state=tk.DISABLED)
        self.cancel_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.countdown_label = tk.Label(root, text="", font=("Helvetica", 18))
        self.countdown_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def start_countdown(self):
        try:
            minutes = int(self.time_var.get())
            self.total_seconds = minutes * 60
            self.start_button.config(state=tk.DISABLED)
            self.cancel_button.config(state=tk.NORMAL)
            self.cancel_event.clear()
            threading.Thread(target=self.countdown).start()
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um número válido de minutos.")

    def countdown(self):
        while self.total_seconds > 0 and not self.cancel_event.is_set():
            mins, secs = divmod(self.total_seconds, 60)
            time_format = f"{mins:02d}:{secs:02d}"
            self.countdown_label.config(text=time_format)
            time.sleep(1)
            self.total_seconds -= 1

        if not self.cancel_event.is_set():
            action = self.action_var.get()
            if action == "desligar":
                self.shutdown()
            elif action == "reiniciar":
                self.restart()
        else:
            self.reset()

    def cancel_countdown(self):
        self.cancel_event.set()

    def shutdown(self):
        if os.name == "nt":  # Windows
            os.system("shutdown /s /t 1")
        else:  # Linux and macOS
            os.system("sudo shutdown -h now")

    def restart(self):
        if os.name == "nt":  # Windows
            os.system("shutdown /r /t 1")
        else:  # Linux and macOS
            os.system("sudo shutdown -r now")

    def reset(self):
        self.start_button.config(state=tk.NORMAL)
        self.cancel_button.config(state=tk.DISABLED)
        self.countdown_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = ShutdownApp(root)
    root.mainloop()
