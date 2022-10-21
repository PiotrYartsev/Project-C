from PIL import Image
im = Image.open('plots/rock-paper_sizors.gif')
print("Number of frames: "+str(im.n_frames))

im.seek(1)
im.save('rock-paper-sizors.png')