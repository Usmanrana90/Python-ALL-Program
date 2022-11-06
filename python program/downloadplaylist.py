import pytube
url=input("Enter the your playlist url :")

pl=pytube.Playlist(url)
pl.download_all("E:/nazia")