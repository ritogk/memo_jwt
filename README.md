# oauth2のサンプルソース

## password認証とソーシャルログインができるところまで
![sample](https://user-images.githubusercontent.com/72111956/195019146-395433bd-ef82-4947-9a5a-16055080fe65.jpg)
## 忘れ防止メモ
### twitter oauth2
twitterのoauth2はデフォルトでメールアドレスが取得できない。
twitter側に申請しないと取得できないっぽ(めんどいからしてない)
本名が取得できない(そもそもtwitter側でもっていない。)

### google oauth2
何度もoauth2を使うととレスポンスが返ってこなくなる・・・
簡単に本名とメールアドレスが取得できて良い！
facebookも似たような感じらしい。

## src/
password認証とoauth2をミックスしたサンプルコード


### 初期設定
```
cd src
./e_migrate_deploy.sh
./e_app.sh
```
