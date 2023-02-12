import os
from error import *

WINDOWS = "nt"
LINUX = "posix"
JAVA = "java"
'audio-trans-1307351455'
# 利用腾讯云的cos对象存储。注，有免费50G额度180天， 而且存储功能它便宜啊
REGION = "ap-beijing"
# 这里暂时使用http传输，后续优化为自选程序
SCHEME = "http"
BUCKET = 'audio-trans-1307351455'


def get_config():
    # Windows系统从注册表中读取信息
    if os.name == WINDOWS:
        import winreg
        try:
            tencent_secret_id = winreg.QueryValue(winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\AudioTrans\TencentSecretId"), None)
            tencent_secret_key = winreg.QueryValue(winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\AudioTrans\TencentSecretKey"), None)
            baidu_secret_id = winreg.QueryValue(winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\AudioTrans\BaiduSecretId"), None)
            baidu_secret_key = winreg.QueryValue(winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\AudioTrans\BaiduSecretKey"), None)
            return tencent_secret_id, tencent_secret_key, baidu_secret_id, baidu_secret_key
        except:
            print("There is no config in register, please input the information in the following")
            return register(True)

    # 其他系统用环境变量
    else:
        try:
            secret_id = os.environ["secret_id"]
            secret_key = os.environ["secret_key"]
        except:
            return register(False)


def register(is_windows: bool):
    if is_windows:
        import winreg
        tencent_secret_id = input("insert tencent_secret_id: ")
        tencent_secret_key = input("insert tencent_secret_key: ")
        baidu_secret_id = input("insert baidu_secret_id: ")
        baidu_secret_key = input("insert baidu_secret_key: ")
        try:
            winreg.SetValue(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\AudioTrans\TencentSecretId", winreg.REG_SZ, tencent_secret_id)
            winreg.SetValue(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\AudioTrans\TencentSecretKey", winreg.REG_SZ, tencent_secret_key)
            winreg.SetValue(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\AudioTrans\BaiduSecretId", winreg.REG_SZ, baidu_secret_id)
            winreg.SetValue(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\AudioTrans\BaiduSecretKey", winreg.REG_SZ, baidu_secret_key)
            return tencent_secret_id, tencent_secret_key, baidu_secret_id, baidu_secret_key
        except Exception as e:
            if e[1] == "拒绝访问":
                print("Please run the app with admin privilege")
                return Error(NEED_ADMIN)
            else:
                return Error(EDIT_REGISTER_WRONG)
    else:
        # 暂不支持自动build环境变量
        print("You have to build environment by yourself")
        return Error(SET_ENVIRONMENT)

