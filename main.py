# Import necessary modules
import customtkinter
from pytube import YouTube
import os

# Define a custom application class that inherits from customtkinter.CTk
class App(customtkinter.CTk):
    def __init__(self):
        # Initialize the parent class
        super().__init__()

        # Set the title of the application
        self.title("Downloader")

        # Set the default color theme using the customtkinter module
        customtkinter.set_default_color_theme("green") 

        # Set the icon of the application
        icon_path = os.path.abspath('./icon.ico')
        self.iconbitmap(icon_path)

        # Set window geometry and min/max window sizes
        self.geometry("500x330")
        self.minsize(500, 330)
        self.maxsize(500, 330)

        # Define grid configurations for widgets
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        # Label for URL input TextBox
        self.urlInputLabel = customtkinter.CTkLabel(master=self, text="URL")
        self.urlInputLabel.grid(row=0, column=0, columnspan=1, padx=10, pady=(10, 0), sticky="nsew")

        # URL input TextBox
        self.urlInputTextBox = customtkinter.CTkTextbox(master=self)
        self.urlInputTextBox.grid(row=0, column=1, columnspan=2, padx=10, pady=(10, 0), sticky="nsew")

        # Text Box for logs (read-only)
        self.loggingTextBox = customtkinter.CTkTextbox(master=self)
        self.loggingTextBox.grid(row=1, column=0, columnspan=3, padx=20, pady=(20, 0), sticky="nsew")
        self.loggingTextBox.configure(state="disabled")

        # Combo box to choose file type
        self.type = customtkinter.StringVar(value="MP4")
        self.typeComboBox = customtkinter.CTkComboBox(master=self, values=["MP4", "MP3"], variable=self.type)
        self.typeComboBox.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")
        
        # Button to download using chosen options
        self.downloadButton = customtkinter.CTkButton(master=self, command=self.downloadFile, text="Download")
        self.downloadButton.grid(row=2, column=2, padx=20, pady=20, sticky="nsew")

    # Sets the state of loggingTextBox to normal, outputs the given text, and sets it back to read-only
    def outputLog(self, text):
        self.loggingTextBox.configure(state="normal")
        self.loggingTextBox.insert("insert", text + "\n")
        self.loggingTextBox.configure(state="disabled")

    # Callback function of the "Download" button
    def downloadFile(self):
        # Get the URL from the input TextBox
        url = self.urlInputTextBox.get("0.0", "end").replace("\n", "")

        # Check the selected file type and initiate the download accordingly
        if self.type.get() == "MP4":
            try:
                # Download the highest resolution video stream using the pytube library
                youtube = YouTube(url)
                file = youtube.streams.get_highest_resolution()
                self.outputLog(f"Downloading {file.title} in {self.type.get()} format...")
                file.download("./downloads")
                self.outputLog("Download successful!")
            except Exception as e:
                # Handle download errors
                self.outputLog(f"Download failed! Error: {str(e)}")
        else:
            try:
                # Download the audio-only stream and convert it to MP3 format
                youtube = YouTube(url)
                file = youtube.streams.filter(only_audio=True).first()
                self.outputLog(f"Downloading {file.title} in {self.type.get()} format...")
                out_file = file.download("./downloads")
                base, ext = os.path.splitext(out_file) 
                new_file = base + '.mp3'
                os.rename(out_file, new_file) 
                self.outputLog("Download successful!")
            except Exception as e:
                # Handle download errors
                self.outputLog(f"Download failed! Error: {str(e)}")

# Entry point of the application
if __name__ == "__main__":
    # Create an instance of the App class and start the main event loop
    app = App()
    app.mainloop()
