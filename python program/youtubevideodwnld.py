from pytube import YouTube #first pip install pytube in anaconda prompt
link=input('Enter the youtube link: = ')
YouTube(link).Streams.first().download('E:/')