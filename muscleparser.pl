#!/usr/bin/perl -w
use strict;
use warnings;
use Getopt::Std;

my %opts = ();
getopt('io', \%opts);
my $file = $opts{i};
my $alignedfile = $opts{o};

my $sequence='';
my $numsequence=0;
my $name='';
my %counterhash=();


open (FILE, $file) or die "no such file $file $!\n";

while (<FILE>){
	my $line = $_;
	chomp $line;
	if ($line =~ /^>/){
		if ($sequence){
			$counterhash{$numsequence}=length($sequence);
		}	
		$name=$line;
		$sequence='';
		++$numsequence;
		
	}
	else {
		$sequence .= $line;
	}
}
close(FILE);
$counterhash{$numsequence}=length($sequence);
my $totallength=0;
foreach my $key (keys(%counterhash)){
	$totallength += $counterhash{$key};
}
my $mean = $totallength/$numsequence;
print "total sequences: $numsequence\tmean length: $mean\n";


`muscle -in $file -out $alignedfile -log logfile.txt 2>output.txt`;

my $y=0;
my $x=0;
my $anonarray=[];

open (FILE, $alignedfile) or die "no such file $alignedfile $!\n";
$sequence='';
while (<FILE>){
        my $line = $_;
	chomp $line;
	
        if ($line =~ /^>/){
                if ($sequence){
			
			my @splitsequence = split('',$sequence);
			$x=0;
			foreach my $element(@splitsequence){
				$anonarray->[$x][$y]=$element;
				++$x;
			}
			++$y;
                }       
                $name=$line;
                $sequence='';
                ++$numsequence;
                
        }
        else {
                $sequence .= $line;
        }
}
my @splitsequence = split('',$sequence);
$x=0;
foreach my $element(@splitsequence){
    $anonarray->[$x][$y]=$element;
    ++$x;
}
++$y;
print "Pos\tA\tC\tG\tU\tN\t-\tsum\n";
for (my $xx=0; $xx<$x; ++$xx){
	my $column='';
	my ($as,$cs,$gs,$ts,$ns,$dashes,$allaligned)=0;
	for (my $yy=0; $yy<$y; ++$yy){
		
		$column .= $anonarray->[$xx][$yy];
	}
	$as = countbases($column,'a');
	$cs = countbases($column,'c');
	$gs = countbases($column,'g');
	$ts = countbases($column,'u');
	$ns = countbases($column,'n');
	$dashes = countbases($column,'-');

	if ($dashes eq 0){
		++$allaligned;
	}
	my $check = $as+$cs+$gs+$ts+$ns+$dashes;
	my $pos = $xx+1;
	print "$pos\t$as\t$cs\t$gs\t$ts\t$ns\t$dashes\t$check\t\n";
}

exit;

sub countbases {
	my ($seq,$base)=@_;
	my $counter=0;
	if ($seq =~ /$base/i){
		$counter = ($seq =~ s/$base//ig);
	}
	return $counter;
}	
