import tkinter as tk
from tkinter import filedialog
import qrcode as qr
from PIL import ImageTk, Image
import os
import io

def clean_up():
    # Cleanup temporary file
    if os.path.exists("temp_qr.png"):
        os.remove("temp_qr.png")

def generate_qr():
    data = entry.get()
    if data:
        qr_img = qr.make(data)
        # Save to memory buffer instead of disk to avoid permission issues in packaged apps
        buffer = io.BytesIO()
        qr_img.save(buffer)
        buffer.seek(0)
        
        # Update the image on the label
        img = Image.open(buffer)
        img = img.resize((250, 250))
        photo = ImageTk.PhotoImage(img)
        qr_label.config(image=photo)
        qr_label.image = photo # Keep a reference
        
        # Enable the download button
        download_button.config(state=tk.NORMAL)
        # Store the PIL image object for saving later
        root.current_qr_image = qr_img

def save_qr():
    if hasattr(root, 'current_qr_image'):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")]
        )
        if file_path:
            root.current_qr_image.save(file_path)

clean_up()

root = tk.Tk()
root.title("QR Code Maker")
root.geometry("600x400")
root.minsize(500, 300)

# Create frames for layout (Left and Right)
left_frame = tk.Frame(root)
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=20)

right_frame = tk.Frame(root)
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=20, pady=20)

# Left Side: Entry and Generate Button
entry_label = tk.Label(left_frame, text="Enter Data:")
entry_label.pack(pady=(50, 5))

entry = tk.Entry(left_frame, width=30)
entry.pack(pady=5)

generate_button = tk.Button(left_frame, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=20)

# Right Side: QR Code Image
qr_label = tk.Label(right_frame, text="QR Code will appear here", bg="lightgray", width=30, height=15)
qr_label.pack(expand=True, fill=tk.BOTH)

# Download Button (below the image)
download_button = tk.Button(right_frame, text="Download QR Code", command=save_qr, state=tk.DISABLED)
download_button.pack(pady=10)

root.mainloop()

clean_up()