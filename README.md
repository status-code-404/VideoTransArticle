# VideoTransArticle
Transfer the video to the words, can be used in situation such as speech video, lesson record......
1. Trans video to audio and cut them in sections (the baiduAI API has limits of the file size)
2. Use Tencent Cos store the audio file,
3. Use BaiduAI transform the audio into words

Attention:
1.  in win system I use winreg pack, which means the program needs admin privilege to edit registry
2. in other system you need to set the environment (tencent cos secretId and key) by yourself (in the following edition maybe will add auto environment set function) 
3. Don't forget to make cos public read


一个中文的小玩应，应用场景：适用于教师将录下的课程重新转换成文字成为自己的讲稿 或一些其他长音频转文字方向
用的baidu的AI转文字, 需要公网存储用的腾讯的云存储(可以白嫖的)，因为用服务器存这种东西实在态浪费了

