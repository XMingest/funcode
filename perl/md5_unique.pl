binmode STDOUT, qq(:utf8);

use feature qw(say);
use utf8;

use Digest::MD5;
use File::Copy;
use Getopt::Long;

sub md5f
{
  $file = shift(@_);
  open(DATA, qq(<$file));
  $file_md5 = Digest::MD5->new->addfile(DATA)->hexdigest;
  close(DATA);
  return $file_md5;
}

GetOptions(
  q(ext=s) => \$ext,
  q(from=s) => \$from,
  q(rename) => \$need_rename,
  q(to=s) => \$to,
);

if (-d $from)
{
  # 获得目录下关注文件
  my @files;
  if (defined($ext))
  {
    @files = glob(qq($from/*.$ext));
  }
  else
  {
    @files = glob(qq($from/*));
  }

  # 处理目标目录
  if (defined($to))
  {
    $from != $to or die(q(不支持原地处理文件));
    if (not -d $to)
    {
      mkdir($to);
    }
  }
  else
  {
    # 建立临时目录
    $to = qq($from/tmp);
    my @eles = (q(a) .. q(z), q(_));
    while (-d $to) {
        $to .= $eles[int(rand(@eles))]
    }
    mkdir($to);
  }

  # 建立文件md5映射
  my %file_md5_map = ();
  foreach my $file (@files)
  {
    # 求取MD5
    my $file_md5 = md5f($file);
    if (not exists($file_md5_map{$file_md5}))
    {
      # 保存映射
      say($file);
      $file_md5_map{$file_md5} = $file;

      # 求取新文件路径
      my $new_file = qq($to/);
      if(defined($need_rename))
      {
        $new_file .= $file_md5;
        $file =~ /\.[^.]+$/;
        $new_file .= $&;
      }
      else
      {
        $file =~ /[^\\\/]+$/;
        $new_file .= $&;
      }

      # 复制文件
      say(qq($file -> $new_file));
      copy($file, $new_file);
    }
  }
}
else
{
  say(q(Usage:
        --from   待处理目录
        --ext    待处理扩展名
        --rename 是否以md5值重命名文件
        --to     Save Directory
));
}

__END__
