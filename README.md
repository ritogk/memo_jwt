```
# JWT
TOKEN=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9sb2NhbGhvc3RcL2FwaVwvYXV0aFwvYWRtaW5cL2xvZ2luIiwiaWF0IjoxNjQyNzQ1MTI4LCJleHAiOjE2NDI3NDg3MjgsIm5iZiI6MTY0Mjc0NTEyOCwianRpIjoiaTZaWERLOFZqbzU0bG1OaCIsInN1YiI6MSwicHJ2Ijp0cnVlfQ.VjBGimYRV8XUnSNVLiCeSX2TdnDcRkp0L306-qp7DJ8
# 証明書作成用の秘密鍵(サーバーで保持してるやつ)
SECRET=U5CRTd2GNdJijxxV5FVgdzDND3Wz2XkXRAWLXvScPrq2tY5oXtMb4eXePyRzrPl1

# JWTを分解
LIST=(${TOKEN//./ })
# ヘッダ
HEADER=${list[0]}
# ペイロード
PAYLOAD=${list[1]}
# 署名
SIGNATURE=${list[2]}


# 「ヘッダ」と「ペイロード」から署名作成
# 「ヘッダ.ペイロード」をsha256でハッシュ化 + 秘密鍵で暗号化
# base64変換した時のパディング(末尾の=)は不要なので削除する
# base64形式だとJWTの設計と合わないので、base64 urlセーフの形に変換する
echo $(
	echo -n "$HEADER.$PAYLOAD" | \
	openssl dgst -hmac $SECRET -sha256 -binary | \
	base64 | \
	sed -e 's/=$//' -e 's/+/-/'
)

# JWTに含まれる署名
echo $SIGNATURE

```

https://zenn.dev/mfykmn/articles/eeaeb9a05130b8
https://tech-lab.sios.jp/archives/7576
https://jwt.io/
https://architecting.hateblo.jp/entry/2020/03/27/130535
