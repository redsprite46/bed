#!/usr/bin/perl

use strict;
use warnings;

use Redis;
use Redis::List;

# open binmode xbee;
system ("stty -F /dev/ttyUSB0 raw 57600 cs8 -parenb -cstopb");
open (XBEE,"/dev/ttyUSB0");

my $mamoruId = '1001';

my $stat = 0 ;
my $ch = 0 ;
my $high = 0 ;
my @chData ;
my $dataType = 0;
my @chNum = (3, 6); # dataType=0:3ch, dataType=1:6ch
my $mgSel = 0;

# 移動平均計算用バッファ [0][] = x, [1][] = y, [2][] = z
my @absDiffBuf = () ;
my $bufPos = 0;
my $bufLength = 128;  # 50 data/sec * 2.5sec
my @lastData = (0,0,0);

# Redis
my $redis = Redis->new(server => 'localhost:6379');


# recv loop
while(1) {
  # read 1byte
  my $readBuf;
  read(XBEE,$readBuf,1);

  # binary -> Hex Data for Debug
  my ( $readData ) = unpack('H*', $readBuf);

  # binary -> char data
  my ( $buf ) = unpack('C', $readBuf);

  # state machine

  if (($stat == 0) && ($buf == 0xff)) {
    # state 0 : wait for first 0xff
    $stat = 1;
  } elsif ($stat == 1) {
    # state 1 : check second  0xff
    if ($buf == 0xff) {
      $stat = 2;
    } else {
      $stat = 0;
    }
  } elsif ($stat == 2) {
    # state 3 : check MID or else
    # init data
    @chData = ();  # init ch-data
    $high = 1;     # init high/low
    $ch = 0;       # init ch
    #
    $dataType = $buf;
    if ($dataType == 1) {
      $stat = 4;
    } else {
      $stat = 3; #
    }
  } elsif ($stat == 3) {
    $stat = 4;
    $mgSel = $buf;
  } elsif ($stat == 4) {
    if ($high == 1) {
      $high = 0 ;
      $chData[$ch] = $buf;
    } else {
      $high = 1 ;
      $chData[$ch] = $chData[$ch] * 256 + $buf;
      $ch++;
      if ( $ch == $chNum[$dataType] ) {
        $stat = 5;
      }
    }
  } elsif ($stat == 5) {
    $stat = 0 ;
#    print localtime();
#    printf("  x:%04X y:%04X z:%04X\n", $chData[0], $chData[1], $chData[2]);

    my $valData = $mamoruId . ":" . $dataType . ":" . time(); ; #
    for (my $i = 0 ; $i < $chNum[$dataType] ; $i++) {
      $absDiffBuf[$i][$bufPos] = abs($lastData[$i] - $chData[$i]);
      $lastData[$i] = $chData[$i];
      $valData .= ":" . $chData[$i];
    }
    print $valData . "\n";

    ## my $html = system($url) ;

    $redis->rpush('postdata', $valData);
    $redis->ltrim('postdata', -500, -1); # 最新500回分(10秒分)だけ記憶

    # if ($dataType == 0) {
    #   $redis->rpush('shakedata', $valData);
    #   $redis->ltrim('shakedata', -50, -1); # 最新50回分(1秒分)だけ記憶
    # }

    # my $monitor_key;
    # $monitor_key = 'monitordata' . $dataType;
    # $redis->rpush($monitor_key, $valData);
    # $redis->ltrim($monitor_key, -500, -1); # 最新500回分(10秒分)だけ記憶

    $bufPos = ($bufPos++) % $bufLength;
  }
};

1;
