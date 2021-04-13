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
  foreach my $file (@files)
  {
    my $new_file = $file;
    $new_file =~ /.*\/([^.]+).$ext/;
    $new_file = $1;
    while ($new_file =~ /([a-z])([A-Z])/mg)
    {
      my $oldstr = qq(${1}${2});
      my $newstr = qq(${1}_) . lc(${2});
      $new_file =~ s/$oldstr/$newstr/g
    }
    $new_file = qq($to/) . lc($new_file) . qq(.$ext);
    say(qq($file -> $new_file));
    copy($file, $new_file)
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
