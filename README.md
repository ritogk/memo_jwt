# パスワード認証とソーシャル認証をミックスしたサンプルコード

### 初期設定
```sh
cd src
./e_migrate_deploy.sh
cp .env.base .env
vim .env # .envを環境に合わせて書き換える
./e_app.sh
```
## 画面
<img src="https://user-images.githubusercontent.com/72111956/195317498-cddcc7f7-6846-4e7c-ae70-8ebe017086e3.png" width="50%" />

## twitter oauth2 
twitterのoauth2はデフォルトでメールアドレスが取得できない。  
twitter側に申請しないと取得できないっぽ(めんどいからしてない)  
本名が取得できない(そもそもtwitter側でもっていない。)  

## google oauth2
何度もoauth2を使うととレスポンスが返ってこなくなる・・・  
簡単に本名とメールアドレスが取得できて良い！  
facebookも本名とメールアドレスが簡単にとれるらしい。
