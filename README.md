# Programming-D

## 概要
筑波大学プロラミング序論Dの丸つけ簡略化のために作りました．主にコードを動かさなければならない課題に対応するものです．論述は誰か開発してください．作成したのは2025年の秋Cです．課題が変わっていないことを祈ります．

## ディレクトリ構造
'''
作業ディレクトリ/
├── 2-3-1（何でも大丈夫）/
│   ├──　2023...@00102023...
│   │    └── s23...02-03-ex1.zip
│   ├──　2023...@00102023...
│   │    └── s23...02-03-ex1.zip
│   └── execution_results.csv
├── 4-2-3/
├── ...
├── unzip.py
├── compile.py
├── debug.py
├── input.txt 
├── .gitignore
└── README.md
'''

## 前処理
1. '''git clone https://github.com/KurodaKento0505/Programming-D.git'''
1. '''cd Programming-D'''
1. manabaから採点レポートと提出物をダウンロード
1. 作業ディレクトリに新しいフォルダ作成（2-3-1とか，何でも大丈夫）
1. 作成したフォルダにダウンロードしたzipファイルを展開
1. 作業ディレクトリに移動
1. 3~5は各課題で行う

## 使い方
1. 各学生のzipファイルを解凍
'''python unzip.py --directory /Path/to/作業ディレクトリ/2-3-1'''
1. 各学生のcファイルをコンパイル
'''python compile.py --directory /Path/to/作業ディレクトリ/2-3-1 --exe_file_name 2-3-ex1.exe --gcc_flags "-lm "'''
* コンパイル時に必要なフラグを--gcc_flagsで与えられる．しかし，配列でしか渡せないため，一つだけでもスペースを与えないといけない．誰か直してください．
1. 各学生のexeファイルを実行して，その結果をcsvファイルに出力
'''python debug.py --directory /Path/to/作業ディレクトリ/2-3-1 --exe_file_name 2-3-ex1.exe --input_file /Path/to/作業ディレクトリ/input.txt'''
* execution_results.csvが出力される．debug.pyを実行するごとに列が追加される．input.txtの中身を変えて，いくつかのパターンで評価可能．
* --input_fileではtxtファイルで引数を与えられる．
  * input.txtの中身
  　'''4
    log
    2'''
* --debug_argsでも与えられるが，4-2-3では使えていない．
* --input_fileと--debug_argsのどっちかは使えるともうので見極めてください．すみません．