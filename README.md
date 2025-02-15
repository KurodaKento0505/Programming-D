# Programming-D

## 概要
筑波大学プロラミング序論Dの丸つけ簡略化のために作りました。主にコードを動かさなければならない課題に対応するものです。論述は誰か開発してください。作成したのは2025年の秋Cです。課題が変わっていないことを祈ります。

## ディレクトリ構造
```
作業ディレクトリ (Programming-D)/
├── 1
|   ├── 2-3-1（何でも大丈夫）/
│   │   ├── 2023...@00102023.../
│   │   │    └── s23...02-03-ex1.zip
│   │   ├── 2023...@00102023.../
│   │   │    └── s23...02-03-ex1.zip
│   │   └── execution_results.csv
|   |── 4-2-3/
|   |── .../
├── 2
├── 3
├── .../
├── unzip.py
├── compile.py
├── debug.py
├── input.txt 
├── .gitignore
└── README.md
```

## 前処理
1. ```git clone https://github.com/KurodaKento0505/Programming-D.git```
1. ```cd Programming-D```
1. manabaから採点レポートと提出物をダウンロード
1. 作業ディレクトリに新しいフォルダ作成（2-3-1とか、何でも大丈夫）
1. 作成したフォルダにダウンロードしたzipファイルを展開
1. （作業ディレクトリに移動）
1. 3~5は各課題で行う

## 使い方
1. 各学生のzipファイルを解凍
    ```bash
    python unzip.py --directory 1/2-3-1
    ```
1. 各学生のcファイルをコンパイル
    ```bash
    python compile.py --directory 1/2-3-1 --exe_file_name 2-3-1.exe --gcc_flags "-lm "
    ```
    * コンパイル時に必要なフラグを--gcc_flagsで与えられる。しかし、配列でしか渡せないため、一つだけでもスペースを与えないといけない。誰か直してください。
    * 4-2-3は --gcc_flags "-lm " が必要
    * 3-2-6は --gcc_flags "-Wall " が必要
1. 各学生のexeファイルを実行して、その結果をcsvファイルに出力
    ```bash
    python debug.py --directory 1/2-3-1 --exe_file_name 2-3-1.exe --input_file input.txt
    ```
    * execution_results.csvが出力される。debug.pyを実行するごとに列が追加される。input.txtの中身を変えて、いくつかのパターンで評価可能。
    * 実行時の引数の与え方は二通り
        1. --input_fileでtxtファイルで引数を与える
            ```bash
            python debug.py --directory 1/2-3-1 --exe_file_name 2-3-1.exe --input_file input.txt
            ```
            input.txtの中身
            ```
            2 log 4
            ```
            4-2-3,5-6-3:"2 log 4", 3-2-2,3-2-6:"12345678910"
        1. --debug_argsで文字列で与えられる
            ```bash
            python debug.py --directory 1/2-3-1 --exe_file_name 2-3-1.exe --debug_args "10 3 43"
            ```
        * 4-2-3で "2 log 4" と与えても使えていないことがある。なぜかは分かりません。
        * --input_fileと--debug_argsのどっちかは使えると思うので見極めてください。すみません。input.txtの方がだいたい使えそう。
1. 第三週以降の課題にはまだ対応できていません。unzip.pyだけお使いください。OpenGLを使うためのビルドに Visual Studio の環境が必要です。Visual Studio の環境がなくてもできるはずですが、まだできてません。