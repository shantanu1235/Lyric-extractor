# import modules
from tkinter import *
from lyrics_extractor import SongLyrics

# user defined function
# def get_lyrics():

# 	extract_lyrics = SongLyrics(
# 		"AIzaSyAjxGRJlw3vH6V2nUvjgtEnvSFah8A4w", "d6f7921ea996a41")
	
# 	temp = extract_lyrics.get_lyrics(str(e.get()))
# 	res = temp['lyrics']
# 	result.set(res)
def get_lyrics():
    song_name = str(e.get())
    if not song_name:
        result.set("Please enter a song name.")
        return
    
    try:
        extract_lyrics = SongLyrics("AIzaSyAjxGRJlw3vH6V2nUvjgtEnvSFah8A4wH8", "d6f7921ea996a4129")
        # extract_lyrics = SongLyrics('https://api.lyrics.ovh/v1/')
        temp = extract_lyrics.get_lyrics(song_name)
        
        if 'lyrics' in temp:
            res = temp['lyrics']
            result.set(res)
        else:
            result.set("No lyrics found for the given song name.")
    except Exception as e:
        result.set("An error occurred while fetching the lyrics.")

# creating a button using the widget





# object of tkinter
# and background set to light grey
master = Tk()
master.configure(bg='light grey')

# Variable Classes in tkinter
result = StringVar()

# Creating label for each information
# name using widget Label
Label(master, text="Enter Song name : ",
	bg="light grey").grid(row=0, sticky=W)

Label(master, text="Result :",
	bg="light grey").grid(row=3, sticky=W)


# Creating label for class variable
# name using widget Entry
Label(master, text="", textvariable=result,
	bg="light grey").grid(row=3, column=1, sticky=W)

e = Entry(master, width=50)
e.grid(row=0, column=1)

# creating a button using the widget
b = Button(master, text="Show",
		command=get_lyrics, bg="Blue")

b.grid(row=0, column=2, columnspan=2,
	rowspan=2, padx=5, pady=5,)

mainloop()