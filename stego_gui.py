import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from stego import encode_message, decode_message

def choose_file():
    return filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])

def save_file():
    return filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])

def encode_ui():
    in_file = choose_file()
    if not in_file:
        return
    out_file = save_file()
    if not out_file:
        return
    msg = message_entry.get("1.0", "end-1c")
    if not msg:
        messagebox.showwarning("Warning", "Please enter a message!")
        return
    try:
        encode_message(in_file, out_file, msg)
        messagebox.showinfo("Success", f"Message hidden in {out_file}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def decode_ui():
    in_file = choose_file()
    if not in_file:
        return
    try:
        msg = decode_message(in_file)
        messagebox.showinfo("Decoded Message", msg)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Setup 
root = tk.Tk()
root.title("Steganography Tool")
root.geometry("700x250")

style = ttk.Style()
style.configure("TButton", font=("Segoe UI", 11), padding=6)
style.configure("TLabel", font=("Segoe UI", 11))
style.configure("TEntry", font=("Segoe UI", 11))

frame = ttk.Frame(root, padding=20)
frame.pack(fill="both", expand=True)

ttk.Label(frame, text="Enter Message to Hide:").grid(row=0, column=0, sticky="nw", pady=10)

# Multi-line text box
message_entry = tk.Text(frame, width=60, height=4, font=("Segoe UI", 11))
message_entry.grid(row=0, column=1, pady=10, padx=10)

button_frame = ttk.Frame(frame)
button_frame.grid(row=1, column=0, columnspan=2, pady=15)

ttk.Button(button_frame, text="Encode Message", command=encode_ui).pack(side="left", padx=10)
ttk.Button(button_frame, text="Decode Message", command=decode_ui).pack(side="left", padx=10)

root.mainloop()
