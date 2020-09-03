from pytube import *
from tkinter.filedialog import *
from tkinter import *
from tkinter.messagebox import *
from threading import *

file_size=0

def Progess(chunk=None,file_handle=None,bytes_remaining=None):
    file_downloaded=(file_size-bytes_remaining)
    percentage=(file_downloaded/file_size)*100
    downloadButton.config(text="{:00.0f}%downloaded".format(percentage))
    
def Downloader():
    global file_size
    try:
        url=urlField.get()
        
        downloadButton.config(text='please wait.....')
        downloadButton.config(state=DISABLED)
        path_to_store=askdirectory()
        if path_to_store is None:
            return
        object_of_utube_class=YouTube(url,on_progress_callback=Progess)
        # streem=object_of_utube_class.streams.all()
        # for i in streem:
        #     print(i)
        #strm=object_of_utube_class.streams.last()
        strm=object_of_utube_class.streams.first()
        file_size=strm.filesize
        
        
        vtitle.config(text=strm.title)
        vtitle.pack(side=TOP)
        #print(strm)
        #print(strm.title)
        #print(object_of_utube_class.title)

        #download function
        strm.download(path_to_store)
        #print("done")
        downloadButton.config(text="Press To Start Download")
        downloadButton.config(state=NORMAL)
        showinfo("Download Finished",'Downloaded Sucessfully')
        urlField.delete(0,END)
        vtitle.pack_forget()
        
    except Exception as e:
        print(e)
        print("Something Went Wrong!!!!!!!")
def DownloaderThread():
    thread=Thread(target=Downloader)
    thread.start()
    
#interface building:
top=Tk()
top.geometry("700x600")


#logo=PhotoImage(file='logo.png')
#headingIcon=Label(top,image=logo)
#headingIcon.pack(side=TOP)
#top.title("My Youtube Downloader")
#top.iconbitmap("icon.ico")


urlField=Entry(top,justify=CENTER)
urlField.pack(side=TOP,fill=X,padx=12)



downloadButton=Button(top,text='Press To Start Download',relief='ridge',command=DownloaderThread)
downloadButton.pack(side=TOP)
vtitle=Label(top,text='Video Title:')


top.mainloop()