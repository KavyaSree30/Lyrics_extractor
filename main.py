from tkinter import *
from lyrics_extractor import SongLyrics

def get_lyrics(entry_widget, text_widget):
    api_key = "wqyeD9pRg_WzVCHGw2SvbixKCtHlF8Aq_AfHskXJx8aKPsjSIGuk1a6-mbKAdd7-"
    extract_lyrics = SongLyrics(api_key)
    
    song_name = entry_widget.get().strip()
    if not song_name:
        text_widget.config(state='normal')
        text_widget.delete(1.0, END)
        text_widget.insert(END, "Please enter a song name.")
        text_widget.config(state='disabled')
        return
    
    try:
        hits = extract_lyrics.search_song(song_name)
        
        if not hits:
            text_widget.config(state='normal')
            text_widget.delete(1.0, END)
            text_widget.insert(END, f"Song '{song_name}' not found.")
            text_widget.config(state='disabled')
            return
        
        # Assuming we take the first hit's song ID
        song_id = hits[0]['result']['id']
        lyrics = extract_lyrics.get_lyrics(song_id)
        
        if lyrics == 'Lyrics not found':
            text_widget.config(state='normal')
            text_widget.delete(1.0, END)
            text_widget.insert(END, "Lyrics not found.")
            text_widget.config(state='disabled')
        else:
            text_widget.config(state='normal')
            text_widget.delete(1.0, END)
            text_widget.insert(END, lyrics)
            text_widget.config(state='disabled')
    
    except Exception as e:
        print(f"Error fetching lyrics: {str(e)}")
        text_widget.config(state='normal')
        text_widget.delete(1.0, END)
        text_widget.insert(END, f"Error fetching lyrics: {str(e)}")
        text_widget.config(state='disabled')

master = Tk()
master.title("Lyrics Extractor")
master.configure(bg='light grey')

Label(master, text="Enter Song name:", bg="light grey").grid(row=0, sticky=W)
e = Entry(master, width=50)
e.grid(row=0, column=1, padx=10, pady=10)

Button(master, text="Show", command=lambda: get_lyrics(e, result_text), bg="blue", fg="white").grid(row=0, column=2, padx=10, pady=10)

Label(master, text="Lyrics:", bg="light grey").grid(row=1, sticky=W)
result_text = Text(master, wrap=WORD, width=80, height=20)
result_text.grid(row=2, columnspan=3, padx=10, pady=10)
result_text.config(state='disabled')

master.mainloop()
