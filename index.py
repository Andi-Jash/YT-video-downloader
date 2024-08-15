import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
from yt_dlp import YoutubeDL

def Widgets():
    head_label = Label(root, text="Youtube Video Downloader",
                       padx=15,
                       pady=15,
                       font="Arial 18",
                       bg="Black",
                       fg="white")
    head_label.grid(row=1, column=1, pady=10, padx=5, columnspan=3)

    link_label = Label(root,
                       text="Youtube link: ",
                       bg="Red",
                       fg="White",
                       pady=5,
                       padx=5)

    link_label.grid(row=2, column=0, pady=5, padx=5,)

    root.linkText = Entry(root,
                          width=27,
                          textvariable=video_Link,
                          font="Arial 14")
    root.linkText.grid(row=2, column=1, pady=5, padx=5,)

    destination_label = Label(root,
                              text="Destination: ",
                              bg="Red",
                              fg="White",
                              pady=5,
                              padx=9)
    destination_label.grid(row=3, column=0, pady=5, padx=5)

    root.destinationText = Entry(root,
                                 width=27,
                                 textvariable=download_Path,
                                 font=("Arial", 14))
    root.destinationText.grid(row=3, column=1, pady=5, padx=5)

    browse_B = Button(root,
                     text="Browse",
                     command=Browse,
                     width=10,
                     bg="Red",
                     fg="White",
                     relief=GROOVE)
    browse_B.grid(row=3, column=2, pady=1, padx=1)

    format_label = Label(
        root,
        text = "Select Format: ",
        bg="Red",
        fg="White"
    )
    format_label.grid(
        row = 4,
        column=0,
        padx=5,
        pady=5
    )

    format_options = ["mp4", "mp3"]
    root.format_var = StringVar(value="mp4")
    format_menu = OptionMenu(
        root,
        root.format_var,
        *format_options
    )
    format_menu.config(
        bg="Red",
        fg="White"
    )
    format_menu.grid(
        row=4,
        column=1,
        padx=5,
        pady=5
    )

    quality_label = Label(
        root,
        text="Select Quality: ",
        bg="Red",
        fg="White"
    )
    quality_label.grid(
        row=5,
        column=0,
        padx=5,
        pady=5
    )

    quality_options = [
        "Best",
        "Worst",
        "1080p",
        "720p",
        "480p",
        "360p",
        "144p"
    ]
    root.quality_var = StringVar(value="Best")
    quality_menu = OptionMenu(
        root,
        root.quality_var,
        *quality_options
    )
    quality_menu.config(bg="Red", fg="White")
    quality_menu.grid(
        row=5,
        column=1,
        pady=5,
        padx=5
    )


    Download_B = Button(root,
                        text="Download Video",
                        command=Download,
                        width=20,
                        bg="Red",
                        fg="White",
                        font=("Arial", 14),
                        pady=5,
                        padx=5,
                        relief=GROOVE)
    Download_B.grid(row=6, column=1, pady=20, padx=20)


def Browse():
    download_Directory = filedialog.askdirectory(initialdir="Your Directory Path", title="Save Video")
    download_Path.set(download_Directory)


def Download():
    Youtube_link = video_Link.get()
    download_Folder = download_Path.get()
    selected_format = root.format_var.get()
    selected_quality = root.quality_var.get()

    try:
        # Setting default options
        ydl_opts = {
            'outtmpl': download_Folder + '/%(title)s.%(ext)s',
        }
        
        if selected_format == "mp4":
            ydl_opts['format'] = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
        elif selected_format == "mp3":
            ydl_opts['format'] = 'bestaudio/best'
            ydl_opts['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',  # You can change the quality
            }]

        if selected_quality != "Best":
            # Specify quality settings (optional)
            ydl_opts['format'] = f'{selected_quality}/best'

        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(Youtube_link, download=True)
            messagebox.showinfo("Successfully", "Downloaded and saved in\n" + download_Folder)
    except Exception as e:
        messagebox.showerror("Error", "Failed to download video.\n" + str(e))



root = tk.Tk()

root.geometry("500x300")
root.resizable(False, False)
root.title("YT Video Downloader")
root.config(background="Black")

video_Link = StringVar()
download_Path = StringVar()

Widgets()

root.mainloop()