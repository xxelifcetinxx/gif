from tkinter.filedialog import askopenfilename
from moviepy import VideoFileClip

video = askopenfilename()

clip = VideoFileClip

clip.write_gif('cat.gif', fps=10)








