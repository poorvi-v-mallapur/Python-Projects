# import pyttsx3
# engine = pyttsx3.init()
# print("Welcome to RoboSpeaker 1.1")
# while True:
#     text = input("Enter what you want me to speak (or 'q' to quit): ")
#     if text.lower() == "q":
#         break
#     engine.say(text)
#     engine.runAndWait()


import tkinter as tk
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Define speak function
def speak():
    text = entry.get()
    engine.say(text)
    engine.runAndWait()

# Create the main window
root = tk.Tk()
root.title("RoboSpeaker 1.1")
root.geometry("400x200")
root.resizable(False, False)

# Create and place UI elements
label = tk.Label(root, text="Enter text for RoboSpeaker:", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(root, width=40, font=("Arial", 14))
entry.pack(pady=5)

speak_button = tk.Button(root, text="Speak", command=speak, font=("Arial", 12), bg="#4CAF50", fg="white")
speak_button.pack(pady=20)

# Run the GUI loop
root.mainloop()
