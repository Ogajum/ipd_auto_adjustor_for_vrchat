# ipd_auto_adjustor_for_vrchat
VRChatでアバターの大きさに合わせてSteamVRのipdOffsetを変更するためのセットアップツールです。

VRChatの標準のスケーリング方式では、アバターの大きさや身長に合わせて世界が拡縮されて見えます。SteamVRの設定を変更することで見かけの世界の大きさを保持したまま身長の異なるアバターを使用したり、アバターの頭身と自分の頭身をそろえたりすることができます。

## 動作環境
SteamVRがインストールされたWindowsPC

ただし、このレポジトリのdistフォルダ外のコードを動かすにはPythonもインストールされている必要があります。

## 使い方
まず、ダウンロードしたファイルを解凍してください。

次に、calc_ipd_offset_make_bat.batを実行し、モードを選択して指示に従って情報を入力して下さい。指定したファイル名のbatファイルが生成されます。このファイル名には使用するアバターの名前を用いることを推奨します。

生成されたbatファイルを実行するとC:\Program Files (x86)\Steam\config\steamvr.vrsettingsにipdOffsetの設定が記入され、batファイルの生成時に入力した情報をもとに計算された値になります。

最後にSteamVRを起動している場合は再起動、SteamVRを起動していない場合は起動し、設定の変更を反映してください。

ほかのアバターを使う際は、ほかのアバター用に生成されたbatファイルを実行してからSteamVRを起動あるいは再起動してください。

変更された設定をもとに戻したい場合はreset.batを実行してください。

### モードの説明
#### EyeHeightモード
自分の目の高さとアバターの目の高さを入力することで、SteamVR内でのアバターの目線の高さが本当にその高さのように見えるようになる。
（ワールドやアバターのみかけの大きさと実際の大きさ（Unityシーン内の大きさ）を同じにしたい人におすすめ）
#### ipdモード
自分の目の高さとアバターの目の高さに加え、自分のipd(瞳孔間距離)とアバターのipdも入力することで、自分のipd(瞳孔間距離)とアバターのipdをそろえる。（アバターの頭身と自分の頭身をそろえたい人におすすめ）

### 詳細な設定
大抵の場合は必要がないですが、dataフォルダ内のsettings.jsonを編集することで、不具合が生じたときに以下のことができます。

SteamVRのデフォルトで認識されるipdが0.063mでない場合、"base_ipd"の値を変更することでそれに応じた設定ができます。

SteamVRのconfigファイルsteamvr.vrsettingsがC:\Program Files (x86)\Steam\configにない場合、"vrsetting_path"の値を変更することでsteamvr.vrsettingsへのパスを変更することができます。

## ライセンス
MITライセンスを使用しています。

    MIT License

    Copyright (c) 2024 Ogajum

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
