#!/usr/bin/perl

use strict;
use warnings;

use Redis;
use Redis::List;
use Math::FFT;
use Data::Dumper;

# FFT
my @series ;      # センサーデータ列
my $axisNum = 3;  # 軸数
my $bufLength = 64;  # データバッファのサイズ FFT するので 2^n
my $count = 0 ;   # バッファ内のデータ数
my $level = 1000;    # しきい値

# Redis
my $redis = Redis->new(server => 'localhost:6379');

#
# データ数クリア
$count = 0 ;
while (1) {
  # Redis 経由でセンサーデータの有無を確認
  my $dataLen = $redis->llen('shakedata');

  # センサーデータの取得
  if ($dataLen > 0) {
    my $dataStr = $redis->lpop('shakedata');
    my @data = split(/:/, $dataStr) ;

    if (($data[1] +0) == 1) {
        next;
    }

    # 軸毎にデータを蓄積
    $series[0]->[$count] = ($data[3] + 0);
    $series[1]->[$count] = ($data[4] + 0);
    $series[2]->[$count] = ($data[5] + 0);

    # データ数を更新・
    $count++;
    if ($count == $bufLength) {
      # データバッファが埋まったら FFT 開始
      $count = 0;

      #
      # 検知フラグ
      my $shake = 0 ;
      # 軸毎に FFT
      for (my $axis = 0 ; $axis < $axisNum ; $axis++) {
        # FFT 実行
        my $fft = new Math::FFT($series[$axis]);
        # 4,5,6,7 のスペクトル強度がしきい値を超えたら検知
        for (my $i = 4 ; $i < 8 ; $i++) {
          if ($fft->spctrm->[$i] > $level) {
            $shake = 1 ;
            last ;
          }
        }
        last if ($shake == 1) ;
      }

      # 検知したら，パトライト
      if ($shake == 1) {
        print "Shake!\n";
        system("rsh 192.168.60.2 -l scope alert 100001 2");
      }
    }
  } ;
} ;

1;
