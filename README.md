# VideoTransArticle
Transfer the video to the words, can be used in situation such as speech video, class record......
1. Trans video to audio and cut them in sections (the baiduAI API has limits of the file size)
2. Use Tencent Cos store the audio file,
3. Use BaiduAI transform the audio into words

Attention:
1.  in win system I use winreg pack, which means the program needs admin privilege
2. in other system you need to set the environment (tencent cos secretId and key) by yourself (in the following edition maybe will add auto environment set function) 
3. Don't forget to make cos public read
