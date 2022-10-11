# パスワード認証とソーシャル認証をミックスしたサンプルコード

### 初期設定
```
cd src
./e_migrate_deploy.sh
./e_app.sh
```
## 画面
<img src="https://user-images.githubusercontent.com/72111956/195020613-e8ff1f55-e1cd-4d0a-9af4-8354d49dacb4.png" width="50%" />

## twitter oauth2 
twitterのoauth2はデフォルトでメールアドレスが取得できない。  
twitter側に申請しないと取得できないっぽ(めんどいからしてない)  
本名が取得できない(そもそもtwitter側でもっていない。)  

## google oauth2
何度もoauth2を使うととレスポンスが返ってこなくなる・・・  
簡単に本名とメールアドレスが取得できて良い！  
facebookも似たような感じらしい。

# 実装メモ
https://reflective-gallon-3d7.notion.site/oauth-408bb21fd9ed45328a295d7d6ce9a9e1
