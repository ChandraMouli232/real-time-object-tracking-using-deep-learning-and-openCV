import torch
import cv2
import tkinter as tk
from tkinter import filedialog, Label, Button, Canvas
from ultralytics import YOLO
from PIL import Image, ImageTk
import threading

class YOLOApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YOLO Model GUI")
        self.root.geometry("600x500")  # Set window size
        self.root.configure(bg="#34495E")  # Set background color
        
        self.model_path = None
        self.file_path = None
        
        # Title label with background color
        self.title_label = Label(root, text="YOLO Model GUI", fg="white", bg="#2C3E50", font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=20)
        
        # Load YOLO Model Section
        Label(root, text="Load YOLO Model (.pt):", fg="white", bg="#34495E", font=("Arial", 12)).pack(pady=5)
        Button(root, text="Browse", command=self.load_model, bg="#3498DB", fg="white", font=("Arial", 12), width=20).pack(pady=5)
        
        # Upload Image/Video Section
        Label(root, text="Upload Image/Video:", fg="white", bg="#34495E", font=("Arial", 12)).pack(pady=5)
        Button(root, text="Browse", command=self.load_file, bg="#3498DB", fg="white", font=("Arial", 12), width=20).pack(pady=5)
        
         # Run Prediction Button
         
        Button(root, text="Run Prediction", command=self.run_prediction, bg="#E74C3C", fg="white", font=("Arial", 12), width=20).pack(pady=15)
        # Result Label
        self.result_label = Label(root, text="No File Selected", fg="white", bg="#34495E", font=("Arial", 12))
        self.result_label.pack(pady=15)
        
        # Canvas to display results with border
        self.canvas = Canvas(root, width=500, height=300, bg="#ECF0F1", highlightthickness=2, highlightbackground="#3498DB")
        self.canvas.pack(pady=15)
        
       
        
    def load_model(self):
        self.model_path = filedialog.askopenfilename(filetypes=[("YOLO Model", "*.pt")])
        if self.model_path:
            self.result_label.config(text=f"Model Loaded: {self.model_path}")
            self.model = YOLO(self.model_path)
        
    def load_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Image/Video", "*.jpg;*.png;*.mp4;*.avi")])
        if self.file_path:
            self.result_label.config(text=f"File Selected: {self.file_path}")
        
    def run_prediction(self):
        if not self.model_path or not self.file_path:
            self.result_label.config(text="Please load a model and file first")
            return
        
        if self.file_path.endswith(('.jpg', '.png')):
            results = self.model(self.file_path)
            result_img = results[0].plot()
            img = Image.fromarray(result_img)
            img = img.resize((500, 300))
            img_tk = ImageTk.PhotoImage(img)
            
            self.canvas.create_image(250, 150, image=img_tk)
            self.canvas.image = img_tk
        else:
            threading.Thread(target=self.process_video).start()
    
    def process_video(self):
        cap = cv2.VideoCapture(self.file_path)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            results = self.model(frame)
            result_frame = results[0].plot()
            result_frame = cv2.cvtColor(result_frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(result_frame)
            img = img.resize((500, 300))
            img_tk = ImageTk.PhotoImage(img)
            
            self.canvas.create_image(250, 150, image=img_tk)
            self.canvas.image = img_tk
            self.root.update()
        cap.release()
        self.result_label.config(text="Video Processing Complete!")

if __name__ == "__main__":
    root = tk.Tk()
    app = YOLOApp(root)
    root.mainloop()
