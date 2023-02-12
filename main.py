from config import *
from error import *
from getAudioFromVideo import *
from transfer import *
from transform import *


def main():
    print("Start App")
    print("首先将需要转换的文件放到程序的统计目录下")
    file_name = input("输入文件名(最好是英文命名): ")
    error = create_audio(file_name)
    if error is not None:
        if error.get_code() == NO_FILE:
            print("文件不存在或输入名字不正确，请重新启动程序")
        elif error.get_code() == FILE_TYPE_WRONG:
            print("文件格式错误，只接受mp4, avi, mov, mp3, 其他格式转换功能将在后续补上")
        elif error.get_code() == AUDIO_USE_WRONG:
            print("moviepy 编辑文件出错")
        else:
            print("提取音轨时发生未知错误")
        print("程序将自动关闭")
        time.sleep(10)
        return

    newfile_name = file_name[:-3] + "mp3"
    file_list = slip(newfile_name)
    if type(file_list) == Error:
        if file_list.get_code() == NO_FILE:
            print("新文件查询大小出错")
        elif file_list.get_code() == CLIP_ERROR:
            print("切片发生错误")
        else:
            print("切片时发生未知错误")
        print("程序将自动关闭")
        time.sleep(10)
        return

    url_list = transfer(file_list)
    if type(url_list) == Error:
        if url_list.get_code() == EDIT_REGISTER_WRONG:
            print("注册表操作时有误，查看是否有管理员权限运行程序")
        elif url_list.get_code() == TRANSFORM_ERROR:
            print("传输文件时有误， 需要查看腾讯文档排查，及时复制错误信息")
        print("程序将自动关闭")
        time.sleep(15)
        return
    print(" 上传文件完成， url_list:")
    print(url_list)

    task_list = create_task(url_list)
    if type(task_list) == Error:
        if task_list.get_code() == USE_POST_ERROR:
            print("使用request_post方法出错，检查是否开了代理")
        print("程序将自动关闭")
        time.sleep(15)
        return
    print("创建任务完成, task_ids:")
    print(task_list)

    error = get_result(task_list)
    if error is not None:
        print( "转换过程中出现问题，请及时排查， 或因为baidu APi更新导致格式对不上或其他原因, 服务器返回信息记录在fix_error.txt中请比对查询问题")


if __name__ == '__main__':
    main()
