import tkinter as tk
from tkinter import ttk

alphabet_lower = []
alphabet_upper = []
for i in "abcdefghijklmnopqrstuvwxyz":
    alphabet_lower.append(i)
for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    alphabet_upper.append(i)


def generate_key(parola):
    shift_key = 0
    for i in parola:
        if i.isalpha():
            shift_key += alphabet_upper.index(i.upper())
        else:
            shift_key = 3
            break
    return shift_key


def caesar_encode(string, shift):
    result = ""
    for i in string:
        if i.isupper():
            index = alphabet_upper.index(i)
            result += alphabet_upper[(index + shift) % 26]
        elif i.islower():
            index = alphabet_lower.index(i)
            result += alphabet_lower[(index + shift) % 26]
        else:
            result += i

    return result


def caesar_decode(string, shift):
    result = ""
    for i in string:
        if i.isupper():
            index = alphabet_upper.index(i)
            result += alphabet_upper[(index - shift) % 26]
        elif i.islower():
            index = alphabet_lower.index(i)
            result += alphabet_lower[(index - shift) % 26]
        else:
            result += i


    return result

def encode():
    string = encode_string.get()
    key_string = encode_key.get()
    key = generate_key(key_string)
    encoded_string = caesar_encode(string, key)
    encode_output.delete("1.0", tk.END)
    encode_output.insert(tk.END, encoded_string)

def decode():
    string = decode_string.get()
    key_string = decode_key.get()
    key = generate_key(key_string)
    decoded_string = caesar_decode(string, key)
    decode_output.delete("1.0", tk.END)
    decode_output.insert(tk.END, decoded_string)

window = tk.Tk()
window.title("Caesar Cipher")

notebook = ttk.Notebook(window)
notebook.pack(pady=10)

encode_frame = ttk.Frame(notebook)
encode_frame.pack()

encode_label_title = ttk.Label(encode_frame, text="Encoding", font=("Arial", 18))
encode_label_title.pack(pady=10)

encode_string_label = ttk.Label(encode_frame, text="String:")
encode_string_label.pack()
encode_string = ttk.Entry(encode_frame)
encode_string.pack()

encode_key_label = ttk.Label(encode_frame, text="Key:")
encode_key_label.pack()
encode_key = ttk.Entry(encode_frame)
encode_key.pack()

encode_button = ttk.Button(encode_frame, text="Encode", command=encode)
encode_button.pack(pady=10)

encode_output_label = ttk.Label(encode_frame, text="Encoded String:")
encode_output_label.pack()
encode_output = tk.Text(encode_frame, height=2, width=30)
encode_output.pack()

decode_frame = ttk.Frame(notebook)
decode_frame.pack()

decode_label_title = ttk.Label(decode_frame, text="Decoding", font=("Arial", 18))
decode_label_title.pack(pady=10)

decode_string_label = ttk.Label(decode_frame, text="String:")
decode_string_label.pack()
decode_string = ttk.Entry(decode_frame)
decode_string.pack()

decode_key_label = ttk.Label(decode_frame, text="Key:")
decode_key_label.pack()
decode_key = ttk.Entry(decode_frame)
decode_key.pack()

decode_button = ttk.Button(decode_frame, text="Decode", command=decode)
decode_button.pack(pady=10)

decode_output_label = ttk.Label(decode_frame, text="Decoded String:")
decode_output_label.pack()
decode_output = tk.Text(decode_frame, height=2, width=30)
decode_output.pack()

notebook.add(encode_frame, text="Encode")
notebook.add(decode_frame, text="Decode")

window.mainloop()
