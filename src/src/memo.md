# flask memo

## pipの一括インストール
pip install -r requirements.txt

## 現在の環境の設定ファイルを書き出し
pip freeze > requirements.txt

# flask-migration
flask db init    # マイグレーションのリポジトリ初期化(git initみたいなもん)
flask db migrate -m "message" # マイグレーション用のスクリプトを生成(migrations/versions/配下のxxx_.py)
flask db upgrade # データベースへ書き込み
flask db downgrade # ロールバック

## モデルを修正したら実行するコマンド
flask db migrate
flask db upgrade