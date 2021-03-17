# 查看

## 解码器支持

```bash
ffmpeg -encoders
```

## 视频信息

```bash
ffprobe in.mp4   # 1
ffmpeg -i in.mp4 # 2
```

# 提取字幕

先查看视频的流信息，找到其中的字幕流如`Stream #0:2: Subtitle: ass (default)`

```bash
ffmpeg -i in.mp4 -map 0:2 out.ass
```

# 合并字幕

## 添加字幕流

```bash
ffmpeg -i in.mp4 -i in.ass
```

查看可知
```ffmpeg
Stream #0:0(und): Video: h264
Stream #0:1(und): Audio: aac
Stream #1:0: Subtitle: ass
```

```bash
ffmpeg -i in.mp4 -i in.ass -map 0:0 -map 0:1 -map 1:0 -c:a copy -c:v copy -c:s copy out.mp4
ffmpeg -i in.mp4 -i in.ass -c copy -c:s copy out.mp4
ffmpeg -i in.mp4 -i in.ass -c copy -c:s mov_text out.mp4 # 特殊情况无法实现ass或者其他
```

## 直接字幕入帧

```bash
ffmpeg -i in.mp4 -vf ass=in.ass out.mp4
ffmpeg -i in.mp4 -vf subtitles=in.srt out.mp4
```

# 编码

```bash
ffmpeg -i in.mkv -vcodec h264 out.mp4
```

# 剪切

```bash
ffmpeg -i in.mp4 -ss 00:20:34.024 -to 00:38:01.279 out.mp4
```

# 压缩

## 比特率

比特率 | 画质 | 10分钟视频大小
:- | :- | :-
180k | 320p | 13MB
300k | 360p | 22MB
500k | 480p | 37MB
850k | 576p | 63MB
1000k | 720p | 75MB

```bash
ffmpeg -i in.mp4 -b 500k out.mp4
```

## 分辨率

```bash
ffmpeg -i in.mp4 -s 640x360 out.mp4 # 分辨率转换为640x360
ffmpeg -i in.mp4 -vf scale=1280:-1 out.mp4 # 宽度改为1280，高度原比例缩放
ffmpeg -i in.mp4 -vf scale=iw/2:ih/4 out.mp4 # 宽度减半，高度为四分之一
```

## 完整脚本

参考[dvlden/ffmpeg.md](https://gist.github.com/dvlden/b9d923cb31775f92fa54eb8c39ccd5a9)

原文使用的音频解码在个人使用时ffmpeg报错，所以统一换为aac

主要关注`-b:v`、`-minrate`、`-maxrate`、`-bufsize`、`-vf scale=`这几处

分别代表视频码率，最小码率，最大码率，缓冲大小，缩放分辨率

```shell
# MP4 - 1080p
ffmpeg -i in.mp4 -preset slow -codec:a aac -b:a 128k -codec:v libx264 -pix_fmt yuv420p -b:v 4500k -minrate 4500k -maxrate 9000k -bufsize 9000k -vf scale=-1:1080 out.mp4

# MP4 - 720p
ffmpeg -i in.mp4 -preset slow -codec:a aac -b:a 128k -codec:v libx264 -pix_fmt yuv420p -b:v 2500k -minrate 1500k -maxrate 4000k -bufsize 5000k -vf scale=-1:720 out.mp4

# MP4 - 480p
ffmpeg -i in.mp4 -preset slow -codec:a aac -b:a 128k -codec:v libx264 -pix_fmt yuv420p -b:v 1000k -minrate 500k -maxrate 2000k -bufsize 2000k -vf scale=-1:480 out.mp4

# MP4 - 360p
ffmpeg -i in.mp4 -preset slow -codec:a aac -b:a 128k -codec:v libx264 -pix_fmt yuv420p -b:v 750k -minrate 400k -maxrate 1000k -bufsize 1500k -vf scale=-1:360 out.mp4
```

# 使用ffmpeg合并目录下的ts视频

适用于h264格式的ts：

```bash
ls *.ts | perl -nale 'chomp; $file = $_; push(@files,$file); END{@files = sort({$a <=> $b} @files); print(q(ffmpeg -i "concat:), join(q(|), @files), q(" -acodec copy -vcodec copy -absf aac_adtstoasc out.mp4))}'
```
