import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk, ImageFilter
import numpy as np

class Application:
    def __init__(self, master):
        self.master = master
        self.master.title("Aplikasi Pengolahan Citra")
        self.img_path = None
        self.original_image = None
        self.filtered_image = None
        self.build_gui()

    def build_gui(self):
        # Frame utama
        main_frame = tk.Frame(self.master, padx=10, pady=10)
        main_frame.pack()

        # Label untuk gambar asli
        self.original_image_label = tk.Label(main_frame)
        self.original_image_label.pack(side=tk.LEFT)

        # Label untuk gambar hasil perbaikan
        self.filtered_image_label = tk.Label(main_frame)
        self.filtered_image_label.pack(side=tk.RIGHT)

        # Tombol untuk membuka gambar
        open_button = tk.Button(main_frame, text="Buka Gambar", command=self.open_image)
        open_button.pack(side="top", padx=10, pady=10)

        # Tombol untuk melakukan perbaikan citra
        filter_button = tk.Button(main_frame, text="Perbaiki Citra", command=self.apply_filters)
        filter_button.pack(side="left", padx=10, pady=10)

        # Tombol untuk menutup aplikasi
        quit_button = tk.Button(main_frame, text="Keluar", command=self.master.destroy)
        quit_button.pack(side="bottom", padx=10, pady=10)

        # Label untuk informasi pembuat program
        info_label = tk.Label(self.master, text="Program ini dibuat oleh John Doe", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        info_label.pack(side=tk.BOTTOM, fill=tk.X)

    def open_image(self):
        # Buka dialog untuk memilih gambar
        self.img_path = filedialog.askopenfilename(filetypes=(("Image files", "*.jpg;*.jpeg;*.png"), ("All files", "*.*")))

        # Jika gambar telah dipilih
        if self.img_path:
            # Baca gambar menggunakan OpenCV
            img = cv2.imread(self.img_path)

            # Konversi gambar ke format RGB dan simpan ke variabel original_image
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            self.original_image = Image.fromarray(img)

            # Tampilkan gambar asli di label original_image_label
            img_tk = ImageTk.PhotoImage(self.original_image)
            self.original_image_label.config(image=img_tk)
            self.original_image_label.image = img_tk

    def apply_filters(self):
        # Jika gambar telah dipilih
        if self.img_path:
            # Terapkan filter unsharp masking menggunakan PIL
            img = self.original_image.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))

            # Terapkan selective filtering menggunakan OpenCV
            img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            img = cv2.detailEnhance(img, sigma_s=10, sigma_r=0.15)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            self.filtered_image = Image.fromarray(img)

            # Tampilkan gambar hasil perbaikan di label filtered_image_label
            img_tk = ImageTk.PhotoImage(self.filtered_image)
            self.filtered_image_label.config(image=img_tk)
            self.filtered_image_label.image = img_tk


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Aplikasi Pengolahan Citra")
    root.resizable (width=True, height=True)
    app = Application(root)
    root.mainloop()
