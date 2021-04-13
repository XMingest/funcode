use feature qw(say);
use utf8;

use Digest::MD5;
use File::Copy;
use Getopt::Long;

GetOptions(
           q(ext=s) => \$ext,
           q(from=s) => \$from,
           q(to=s) => \$to,
          );

if (-d qq($from) and -d qq($to) and defined($ext))
{
  my @files = glob(qq($from/*.$ext));
  my @sorted_file = sort
  {
    open(DATA, qq(<$a));
    $da = Digest::MD5->new->addfile(*DATA)->hexdigest;
    close(DATA);
    open(DATA, qq(<$b));
    $db = Digest::MD5->new->addfile(*DATA)->hexdigest;
    close(DATA);
    $da cmp $db;
  } @files;
  my $index = 0;
  my $limit = length(@sorted_file - 1) + 2;
  foreach my $file (@sorted_file)
  {
    my $new_file = $file;
    $new_file =~ s/.*\.//;
    while (length($index) < $limit)
    {
      $index = q(0) . $index;
    }
    $new_file = qq($to/$index.$new_file);
    say(qq($file -> $new_file));
    copy(qq($file), qq($new_file));
    $index += 1;
  }
}
else
{
  say(q(Usage:
        --from=<Handle Directory>
        --to=<Save Directory>
        --ext=<Handle File With Extension>));
}

__END__
