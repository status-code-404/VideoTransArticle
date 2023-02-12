import moviepy
from moviepy.editor import *
from error import *
from suffix import *


# 写入文件的绝对路径
def create_audio(file_name=""):
    if file_name == "":
        return Error(NO_FILE)
    suff = file_name[-4:]
    if suff not in VIDEO and suff not in AUDIO:
        return Error(FILE_TYPE_WRONG)
    if suff == ".mp3":
        return
    else:
        try:
            audio = AudioFileClip(file_name)
        except:
            return Error(NO_FILE)
        try:
            audio.write_audiofile(file_name[:-3] + "mp3")
            return
        except:
            return Error(AUDIO_USE_WRONG)


def slip(file_name):
    try:
        size = os.path.getsize(file_name)
    except:
        return Error(NO_FILE)
        # 要小于100M的音频才能转换
    if size < (1000) ** 3:
        return [file_name]
    # 切片音频, 按一小时切片
    else:
        try:
            clip_name = 0
            audio = AudioFileClip(file_name)
            audio_long = audio.end
            clip_list = []
            for i in range(audio.end // 60 * 60 + 1):
                clip_start = 60 * 60 * i
                audio_clip = audio.subclip(clip_start, min(audio_long, clip_start + 60 * 60))
                audio_new = CompositeAudioClip([audio_clip])
                # 隐藏进度条
                name = file_name + str(clip_name) + ".mp3"
                clip_list.append(name)
                audio_new.write_audiofile(name, fps=44100, logger=None, verbose=False)
                clip_name += 1
            return clip_list
        except:
            return Error(CLIP_ERROR)
