# VideoTransArticle
Transfer the video to the words, can be used in situation such as speech video, lesson record......
1. Trans video to audio and cut them in sections (the baiduAI API has limits of the file size)
2. Use Tencent Cos store the audio file,
3. Use BaiduAI transform the audio into words

Instructions:
1. you need to register BaiduAI apply a speech ai app to get id and key and same thing on TencentCloud COS service (both cheap) 
2. move the file into same level dictionary and input the filename or just input the file path
3. wait and the result will be written into the same level dictionary result.txt

Attention:
1.  in win system I use winreg pack, which means the program needs admin privilege to edit registry
2. in other system you need to set the environment (tencent cos , baidu AI secretId and key) by yourself (in the following edition maybe will add auto environment set function) 
3. Don't forget to make cos public read
4. Use request to get results from client so don't use vpn


一个中文的小玩应，应用场景：适用于教师将录下的课程重新转换成文字成为自己的讲稿 或一些其他长音频转文字方向
用的baidu的AI转文字, 需要公网存储用的腾讯的云存储(可以白嫖的)，因为用服务器存这种东西实在浪费了

说明： 前置工作需要百度智能云的语音服务中申请一个公网应用， 会给你secretId 和 secretKey, 同样在腾讯云的Cos 上申请一个公网应用获取一样的东西
第一次运行时win系统会把配置写进注册表所以需要管理员身份运行， 后面就不需要了
使用时需要将待转换文件放到这个工程项目的同级目录下， 然后输入名字。或者直接将文件路径一并输入 **输入文件时需要加上文件后缀名**
最后等待， 结果会写在同级目录下的result.txt下面

