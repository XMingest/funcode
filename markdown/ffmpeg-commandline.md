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

# 使用ffmpeg合并目录下的ts视频

适用于h264格式的ts：

```bash
ls *.ts | perl -nale 'chomp; $file = $_; push(@files,$file); END{@files = sort({$a <=> $b} @files); print(q(ffmpeg -i "concat:), join(q(|), @files), q(" -acodec copy -vcodec copy -absf aac_adtstoasc out.mp4))}'
```
