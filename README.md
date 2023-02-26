# VideoTransArticle
Transform the video into text. Can be used in speech video, lesson record......
1. Transform video to audio and cut them in sections (the baiduAI API has limit of the file size)
2. Use Tencent COS to store the audio file,
3. Use BaiduAI to transform the audio into words

Instructions:
1. Firstly you need to register BaiduAI to apply a speech AI app where you can get id and key and do the same thing on TencentCloud COS service (both cheap) 
2. Move the file into same level dictionary and input the filename or just input the file path
3. Wait util result will be written into the same level dictionary result.txt
4. If some exception occurs , they will be recorded into same level fix_problem.txt

Attention:
1.  This app now only support Windows System because In Windows system because the program needs admin privilege to edit registry (I use winreg package)
2. When you first run this program, you need provide admin privilege because first time the program need edit the registry to record BaiduAI key and Tencent COS key.
3. Don't forget to make Tencent COS privilege public read
4. When an Exception occurs , most probably reason is because the requests package I use, check if you can use requests package normally


一个中文的小玩应，应用场景：适用于教师将录下的课程重新转换成文字成为自己的讲稿 或一些其他长音频转文字方向
用的baidu的AI转文字, 需要公网存储用的腾讯的云存储(可以白嫖的)，因为用服务器存这种东西实在浪费了

说明： 前置工作需要百度智能云的语音服务中申请一个公网应用， 会给你secretId 和 secretKey, 同样在腾讯云的Cos 上申请一个公网应用获取一样的东西
第一次运行时win系统会把配置写进注册表所以需要管理员身份运行， 后面就不需要了
使用时需要将待转换文件放到这个工程项目的同级目录下， 然后输入名字。或者直接将文件路径一并输入 **输入文件时需要加上文件后缀名**
最后等待， 结果会写在同级目录下的result.txt下面

