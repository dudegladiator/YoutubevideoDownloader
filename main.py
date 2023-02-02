import streamlit as st
from pathlib import Path
from pytube import YouTube
import os , time
import random

def download(link,res,option): 
    e=time.time()
    latest_iteration = st.empty()
    latest_iteration.text(f"{1} Second")
    bar = st.progress(2)
    #taking link and res as input
    # link = input("Enter the Youtube Video URL : ")
    # res=input ("Resolution e.g-2160p,1440p,4320p etc : ")
    # option=int(input('''To get Audio - Type 1 \nTo get Video - Type 2 \nTo get Both -'''))
    #creating a  object of youtube video
    yt = YouTube(link)
    global k
    k=str(random.randrange(100))

    audio = yt.streams.get_by_itag(yt.streams.filter(type="audio")[0].itag)
    
    
    a=audio.download()
    
    latest_iteration.text(f'{int(time.time()-e)} Second')
    bar.progress(30)
    #to change the file name of audio
    global q
    q=Path(a)
   
    q=q.rename(q.with_name("Audio"+k+".mp3"))
    q = os.path.abspath(q)
    global w
    if (option==2):
        video = yt.streams.get_by_itag(yt.streams.filter(res=res,type="video")[0].itag)
        b=video.download()
        #to change the file name of video
        global p
        p=Path(b)
        p=p.rename(p.with_name("Cache"+k+".mp4"))
        video_file = open("Cache"+k+".mp4", 'rb')
        video_bytes = video_file.read()
        
        st.video(video_bytes)           
        latest_iteration.text(f'{int(time.time()-e)} Second')
        bar.progress(30)
        #to merge the file 
        import ffmpeg
        
        p= os.path.abspath(p)
        
        import subprocess 
        subprocess.run(f"ffmpeg {p} {q} -c:v copy -c:a aac -strict experimental Video{k}.mp4",shell=False)
        
        latest_iteration.text(f'{int(time.time()-e)} Second')
        bar.progress(90)
    if (option==2):
        os.remove(p)
        os.remove(q)
    
    
    
    latest_iteration.text(f'{int(time.time()-e)} Second')
    bar.progress(100)
st.title("Download Youtube Video")
link=st.text_input("Youtube URL")
res=st.selectbox("Select The resolution",("720p","144p","240p","360p","480p","720p","1080p","1440p","2160p","4320p"))
option = st.selectbox("Audio(1) or Video(2)",(1,2))
a=st.button("Start Downloading")
if (a):
    download(link,res,option)
    if option==2:
        
        
        with open(f"Video{k}.mp4",'rb') as f:
            st.download_button(label='Save Video', data=f, file_name=f'YoutubeVideo{k}.mp4',mime="application/octet-stream")
            os.remove(f"Video{k}.mp4")
    else :
        with open("Audio"+k+".mp3",'rb' ) as f:
            st.download_button("Save Audio",f,"Music.mp3") 
        
