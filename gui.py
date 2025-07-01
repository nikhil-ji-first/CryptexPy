import tkinter as tk
from tkinter import filedialog, messagebox
from cryptexpy.ciphers import caesar_cipher, vigenere_cipher
from cryptexpy.hashing import hash_text
from cryptexpy.file_handler import read_from_file, write_to_file


def perform_cipher():
    text = text_input.get("1.0", tk.END).strip()
    key = key_input.get().strip()
    mode = mode_var.get()
    method = method_var.get()

    if not text:
        messagebox.showwarning("Input Error", "Text field is empty.")
        return

    if method in ['Caesar', 'Vigenere'] and not key:
        messagebox.showwarning("Input Error", "Key is required for this cipher.")
        return

    try:
        if method == 'Caesar':
            if not key.isdigit():
                messagebox.showerror("Key Error", "Caesar Cipher requires a numeric key.")
                return
            result = caesar_cipher(text, int(key), mode)
        elif method == 'Vigenere':
            if not key.isalpha():
                messagebox.showerror("Key Error", "Vigenère Cipher requires an alphabetic key.")
                return
            result = vigenere_cipher(text, key, mode)
        elif method == 'Hash':
            result = hash_text(text)
        else:
            result = "Unknown method selected."

        result_output.delete("1.0", tk.END)
        result_output.insert(tk.END, result)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{e}")


def open_file():
    path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if path:
        content = read_from_file(path)
        text_input.delete("1.0", tk.END)
        text_input.insert(tk.END, content)


def save_to_file():
    data = result_output.get("1.0", tk.END).strip()
    if not data:
        messagebox.showinfo("Nothing to Save", "Result field is empty.")
        return

    path = filedialog.asksaveasfilename(defaultextension=".txt",
                                         filetypes=[("Text files", "*.txt")])
    if path:
        write_to_file(path, data)
        messagebox.showinfo("Saved", f"Output saved to:\n{path}")


# ==== GUI ====
root = tk.Tk()
root.title("CRYPTEXPY GUI")
root.geometry("600x550")
root.resizable(False, False)

# --- Method & Mode Selection ---
frame_top = tk.Frame(root)
frame_top.pack(pady=10)

method_var = tk.StringVar(value="Caesar")
tk.Label(frame_top, text="Method:").grid(row=0, column=0, padx=5)
tk.OptionMenu(frame_top, method_var, "Caesar", "Vigenere", "Hash").grid(row=0, column=1)

mode_var = tk.StringVar(value="encrypt")
tk.Label(frame_top, text="Mode:").grid(row=0, column=2, padx=5)
tk.OptionMenu(frame_top, mode_var, "encrypt", "decrypt").grid(row=0, column=3)

# --- Key Input ---
frame_key = tk.Frame(root)
frame_key.pack()
tk.Label(frame_key, text="Key (number or word):").pack()
key_input = tk.Entry(frame_key, width=40)
key_input.pack()

# --- Text Input ---
tk.Label(root, text="Input Text:").pack()
text_input = tk.Text(root, height=7, width=70)
text_input.pack(pady=5)

# --- Buttons ---
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

tk.Button(frame_buttons, text="Encrypt/Decrypt", command=perform_cipher).grid(row=0, column=0, padx=10)
tk.Button(frame_buttons, text="Open File", command=open_file).grid(row=0, column=1, padx=10)
tk.Button(frame_buttons, text="Save Result", command=save_to_file).grid(row=0, column=2, padx=10)

# --- Output Box ---
tk.Label(root, text="Output:").pack()
result_output = tk.Text(root, height=7, width=70, bg="#f0f0f0")
result_output.pack(pady=5)

# --- Start App ---
root.mainloop()
