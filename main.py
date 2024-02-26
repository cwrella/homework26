import tkinter as tk
import requests
import json


def index():
    id_ = int(entry.get())
    url = f"https://jsonplaceholder.typicode.com/posts/{id_}"
    response = requests.get(url)
    data = response.json()
    text1 = data.get('body')
    text.config(state='normal')
    text.delete(1.0, tk.END)
    text.insert(tk.END, text1)
    text.config(state='disabled')

    with open(f"data_{id_}.json", 'w') as file:
        json.dump(data, file)
        print(f"Data saved to data_{id_}.json")


root = tk.Tk()
root.title("JSONPlaceholder ID")

frame = tk.Frame(root)
frame.pack()

label = tk.Label(frame, text="Enter ID:")
label.pack()

entry = tk.Entry(frame)
entry.pack()

button = tk.Button(frame, text="Text", command=index)
button.pack()

text = tk.Text(frame)
text.pack()


root.mainloop()

