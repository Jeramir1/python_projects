from tkinter import *
import webbrowser
from pytube import YouTube

def download():
    linkfordl = str(link_field.get())
    print(linkfordl)
    yt = YouTube(linkfordl)
    #Showing details
    
    button = Button(new, text='Downloading',fg='Black',bg='Blue',command=())
    button.grid(row=6, column=1)
    print("Title: ",yt.title)
    print("Number of views: ",yt.views)
    print("Length of video: ",yt.length)
    print("Rating of video: ",yt.rating)
    #Getting the highest resolution possible
    ys = yt.streams.get_highest_resolution()
    #Starting download
    print("Downloading...")
    ys.download()
    print("Download completed!!")
    button = Button(new, text='Download complete',fg='Black',bg='Blue',command=(download))
    button.grid(row=6, column=1)
    fileoutput = Label(new, text = yt.title, fg ='Blue', bg = 'gray', font=("times", 12), cursor="hand2")#archivo generado
    fileoutput.grid(row=7, column=1) #file output generado por el downloader

if __name__=='__main__':
    new = Tk()
    new.config(background='grey')
    new.title("Youtube Downloader")
    new.geometry("350x240")
    ytlink = Label(new, text="Youtube Downloader",bg='grey',font=("times", 28, "bold"))
    #text box for year input
    link_field=Entry(new)
    button = Button(new, text='Download Video',fg='Black',bg='Blue',command=download)
    
#adjusting widgets in position

ytlink.grid(row=2, column=1) #nombre del programa
link_field.grid(row=3, column=1)
button.grid(row=6, column=1)

new.mainloop()