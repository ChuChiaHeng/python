from moviepy.editor import *
video_path="adv-15/小小兵.mp4"
clip=VideoFileClip(video_path)
Font_Url="adv-15/TaipeiSansTCBeta-Bold.ttf"
logos=[]
txt_clip=TextClip("厲害!",font=Font_Url,fontsize=36,color='white')
txt_clip=txt_clip.set_start(0.5).set_end(1.5).set_pos('bottom')
logos.append(txt_clip)
video=CompositeVideoClip([clip, *logos])
video.write_gif("adv-15/小小兵.gif")