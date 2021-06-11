use feature qw(say);
use utf8;

use Digest::MD5;
use File::Copy;
use Getopt::Long;

GetOptions(
   q(from=s) => \$from,
   q(to=s) => \$to,
);

sub md5f
{
    my $file = shift(@_);
    open(my $fh, q(<), $file);
    binmode($fh);
    $md5_obj = Digest::MD5->new;
    while (<$fh>)
    {
        $md5_obj->add($_);
    }
    close($fh);
    return $md5_obj->hexdigest;
}

if (-d qq($from) and -d qq($to))
{
    my %md5_file = ();
    foreach my $file (glob(qq($from/*)))
    {
        $md5_file{md5f($file)} = $file;
    }
    my $index = 0;
    my $limit = length(keys(%md5_file) - 1) + 2;
    foreach my $md5 (keys(%md5_file))
    {
        my $file = $md5_file{$md5};
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
            --to=<Save Directory>));
}

__END__
