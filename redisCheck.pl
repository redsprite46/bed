#!/usr/bin/perl

use strict;
use warnings;

use Data::Dumper;

use Redis;
use Redis::List;

#tie(my @list, 'Redis::List', 'sensordata', (server => 'localhost:6379'));

my $redis = Redis->new(server => 'localhost:6379');


for (my $i = 0 ; $i < 10 ; $i++) {
  my $valData = "1:2" . ":" . time() ; # mamoruid=1 ; device=2
  for (my $x = 0 ; $x < 3 ; $x++) {
    $valData .= ":" . ($i*10+$x) ;
  }
  ##    printf("  x:%04X y:%04X z:%04X\n", $absDiffBuf[0][$bufPos], $absDiffBuf[1][$bufPos], $absDiffBuf[2][$bufPos]);
  print $valData . "\n";

  ## my $html = system($url) ;

  $redis->rpush('sensordata', $valData);
  $redis->ltrim('sensordata', -500, -1); # 最新500回分(10秒分)だけ記憶
}


print Dumper($redis->lrange('sensordata', 0, -1));

1;

