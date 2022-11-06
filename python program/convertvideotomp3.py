import moviepy.editor as abc
f=abc.VideoFileClip('E:/demo.mp4')
f.audio.write_audiofile('E:/myfile.mp3')