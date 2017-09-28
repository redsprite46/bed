#!/usr/bin/perl

use strict;
use warnings;

use Redis;

my $redis = Redis->new(server => 'localhost:6379');

while (1) {
  my $dataLen = $redis->llen('postdata');
#  my $dataLen = 3;

  if ($dataLen > 0) {
    my $dataStr = $redis->lpop('postdata');
    for (my $i = 1 ; $i < $dataLen ; $i++) {
      $dataStr .= "," . $redis->lpop('postdata') ;
    }
    print $dataStr . "\n" ;

    my $url = "curl -s 'http://192.168.60.254:8180/dataPost.php' --data-urlencode 'sensorData=" . $dataStr . "'";
    system($url);
  }

  sleep(2);
}



1;
