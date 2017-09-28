#!/usr/bin/perl

use strict;
use warnings;

use Redis;

my $redis = Redis->new(server => 'localhost:6379');

clearOneKey('monitordata0');
clearOneKey('monitordata1');
clearOneKey('postdata');
clearOneKey('shakedata');

sub clearOneKey {
  my $key;
  $key = $_[0];
  print '#key = ' . $key . "\n";
  my $dataLen = $redis->llen($key);
  if ($dataLen > 0) {
    my $dataStr = '';
    for (my $i = 0 ; $i < $dataLen ; $i++) {
      $dataStr .= $redis->lpop($key) . "\n" ;
    }
    print $dataStr;
  }
}


1;
