# Django_permissions_sample

## セットアップ
```
# 任意のGit用ディレクトリへ移動
>cd path\to\dir

# GitHubからカレントディレクトリへclone
path\to\dir>git clone https://github.com/thinkAmi-sandbox/Django_permissions_sample.git

# virtualenv環境の作成とactivate
# *Python3.5は、`c:\python35-32\`の下にインストール
path\to\dir>virtualenv -p c:\python35-32\python.exe env
path\to\dir>env\Scripts\activate

# requirements.txtよりインストール
(env)path\to\dir>pip install -r requirements.txt

# マイグレーション
(env)path\to\dir>python manage.py migrate

# 初期データのロード
(env)path\to\dir>python manage.py loaddata initial_data.json

# ユーザ・グループの登録とパーミッションの割り当て
(env)path\to\dir>python manage.py create_users

# 開発サーバの起動
(env)path\to\dir>python manage.py runserver

# 開発サーバのURLを既定のブラウザで開く
# (別のコマンドプロンプトを開いて実行)
>start http://localhost:8000/mysite/
>start http://localhost:8000/mysite/login
>start http://localhost:8000/mysite/logout
>start http://localhost:8000/mysite/article/1
>start http://localhost:8000/mysite/login-required
>start http://localhost:8000/mysite/login-required-with-403
>start http://localhost:8000/mysite/limited-user-required
>start http://localhost:8000/mysite/limited-user-required-with-403
>start http://localhost:8000/mysite/permission-required
>start http://localhost:8000/mysite/permission-required-with-403
```

　  
## テスト環境

- Windows10
- Python 3.5.1
- Django 1.9.2

　  
## 関係するブログ

[Django1.9で追加されたPermission mixinsを使って、パーミッションなどのアクセス制御を試してみた - メモ的な思考的な](http://thinkami.hatenablog.com/entry/2016/02/03/062159)