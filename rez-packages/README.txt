# このフォルダは
ランチャー(allzpark)、パッケージ管理(rez)で使用するパッケージの情報を格納するフォルダです。
フォルダは機能やドメインごとに階層に分けされています。
各パッケージは、ソフトウェア・プラグイン・環境変数の設定といったものをカプセル化したものです。

詳細は https://allzpark.com/ を参照してください。



# フォルダ階層

rez-packages
    - inhouse
        内部で開発しているパッケージ

        - projects
             ここ以下に実プロジェクトのパッケージを配置する
             各作業者によって落としてくるパッケージは異なる


    - third
        - _core
            allzpark/rez が動作するための基本パッケージ

        - _software
            DCC toolなど

        - それ以外（ドメイン名ごと）
            （主にDCC用）スクリプトやプラグインを格納する



参考：
https://github.com/Colorbleed/rez-packages
https://github.com/UTS-AnimalLogicAcademy/open-source-rez-packages
