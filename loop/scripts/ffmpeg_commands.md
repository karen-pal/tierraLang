# Vertical scroll
ffmpeg -loop 1 -i input.png -vf "scroll=vertical=0.01,crop=iw:600:0:0,format=yuv420p" -t 10 output.mp4

#Horizontal
ffmpeg -loop 1 -i input.png -vf "scroll=horizontal=0.01,crop=800:600:0:0,format=yuv420p" -t 10 output.mp4


https://stackoverflow.com/questions/24316446/generate-video-containing-scrolling-image
