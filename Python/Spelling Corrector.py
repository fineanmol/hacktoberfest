import tkinter
import customtkinter
from tkinter import filedialog
from textblob import TextBlob

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    global start_frame, options_frame, file_name_entry, text_entry, text_var

    def __init__(self):
        super().__init__()

        # Create a new customtkinter window
        self.window = customtkinter.CTk()

        # configure window
        self.title("Helping Hand")
        self.window.geometry(f"{1100}x{580}")

        # Create the frames and pack them into the main window
        self.start_frame = customtkinter.CTkFrame(self.window)

        self.options_frame = customtkinter.CTkFrame(self.window)

        # Pack the start frame into the main window
        self.start_frame.pack(fill=tkinter.BOTH, expand=True)

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=500, corner_radius=10)
        self.sidebar_frame.grid(row=0, column=0, rowspan= 8, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.file_name_entry = customtkinter.CTkEntry(self.sidebar_frame, placeholder_text="Enter File Name")
        self.file_name_entry.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Create New File", command=self.create_file)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Open File", command=self.open_file)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=2, column=1, rowspan=6, padx=(10, 10), pady=(5, 0), sticky="nsew")

        # create rightside sidebar frame
        self.right_sidebar_frame = customtkinter.CTkFrame(self)
        self.right_sidebar_frame.grid(row=0, column=3, rowspan=8, padx=(0, 0), pady=(20, 0), sticky="nsew")
        self.sidebar_button_5 = customtkinter.CTkButton(self.right_sidebar_frame, text="Correct Spelling", command=self.correct_spelling)
        self.sidebar_button_5.grid(row=4, column=0, padx=20, pady=10)

    def create_file(self):
        # Get the file name from the entry
        file_name = self.file_name_entry.get()

        # Create a new file with the given name
        open(file_name, "w").close()

        # Clear the text in the Text widget
        self.textbox.delete("1.0", tkinter.END)
        
    def open_file(self):
        # Open a file dialog and get the path of the selected file
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])

        # Set the file name entry to the selected file path
        self.file_name_entry.delete(0, tkinter.END)
        self.file_name_entry.insert(0, file_path)

        # Read the contents of the file
        with open(file_path, "r") as file:
             text = file.read()

        # Set the text in the Text widget
        self.textbox.delete("1.0", tkinter.END)
        self.textbox.insert(tkinter.END, text)

    def correct_spelling(self):
        # Get the text from the Text widget
        text = self.textbox.get("1.0", tkinter.END)

        # Create a TextBlob object
        blob = TextBlob(text)

        # Correct the spelling of the text
        corrected_text = str(blob.correct())

        # Set the corrected text in the Text widget
        self.textbox.delete("1.0", tkinter.END)
        self.textbox.insert(tkinter.END, corrected_text)

        # Get the file name from the entry
        file_name = self.file_name_entry.get()

        # Save the corrected text to the same file as the original text
        with open(file_name, "w") as f:
            f.write(corrected_text)


if __name__ == "__main__":
    app = App()
    app.mainloop()