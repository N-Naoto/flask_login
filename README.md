.\venv\Scripts\Activate.ps1

勉強時間を登録できるアプリを作ろう

- [x] ユーザごとにTodoを作れるようにする
- [x] sqliteからmysqlに変更 
- [x] デプロイする
    - [ ] マイグレーション (flask db init  とか dbコマンドがないって怒られる )

# ログイン方法
mysql -u b8e9ff724a7a6b -h us-cdbr-east-03.cleardb.com  -p
886f95f0

- [x] 軽くレスポンシブ化
- [ ] なんで動くようになったのか？
    - [ ] @app.teardown_appcontext
    - [ ] pool_recycle
- [ ] MySQLにログインして、データベースに接続しようとすると 
    - [ ] ERROR 2013 (HY000): Lost connection to MySQL server during query
    - [ ] ERROR 2006 (HY000): MySQL server has gone away
- [ ] ログイン・登録画面でたまに入力できなくなる問題


- [x] デザインの調整

- [ ] 勉強時間管理アプリの参考を見る

- [ ] データベースの設定の変更
- [ ] 勉強時間を可視化（円グラフ？）