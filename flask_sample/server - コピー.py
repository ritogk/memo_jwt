from flask import Flask, jsonify, render_template, make_response, request, redirect, url_for
# from flask_dance.contrib.github import make_github_blueprint, github

app = Flask(__name__)
import datetime
# サーバーとクライアントにはホスト名をつける事。
# localhost or ipだと何故かクッキー送信できない？多分ドメインの書式じゃないから？
# ローカルで実行する場合はhosts等でフォワーディングする
clinet_origin = 'http://localhost.test.com:1000'
server_domain = 'server.test.com'

## api
@app.route('/api/helloworld', methods=["GET"])
def api():
    response = make_response(jsonify({'message': 'Hello world', 'coockie': request.cookies}))
    # 「Content-Type」が未指定の場合は、レスポンスボディの内容から自動的にContent-Typeが決まる
    # IEとかだと「Content-Type」を指定していても勝手にファイルの内容からContent-Typeが書き換わる場合がある
    # 「Content-Type」と「X-Content-Type-Options」をセットで設定しておく事で、Content-Typeの形式で固定するできる。
    # レスポンスのjsonの中にjavascriptのコードが含まれている場合に、ブラウザが勝手にhtmlと認識する場合がある。そうなるとXSSができてしまう。。
    # ヘッダーに上記２つを設定するだけでセキュリティーホールになる可能性を潰せるのでやっておくべき。コスパは良いと思う。
    response.headers.set('Content-Type', 'aplication/json')
    #「X-Content-Type-Options」レスポンスボディのファイル形式を「Content-Type」の内容から読み取るようにする設定
    response.headers.add('X-Content-Type-Options', 'nosniff')

    # クレデンシャルが必要な場合はオリジンに「Access-Control-Allow-Origin = *」はNG
    # 「Access-Control-Allow-Origin = *」は外部公開用api等で使いそう。
    response.headers.add('Access-Control-Allow-Origin', clinet_origin)
    # 指定のhttpメソッドを許可
    response.headers.add('Access-Control-Allow-Methods', 'GET')
    # クッキーと資格情報(なんの事？)の送信を許可
    response.headers.add('Access-Control-Allow-Credentials', 'true')

    # samesite
    #   None:全ドメインに対してCookieを送信する
    #   Lax: 別ドメインからはPOST, ifram, XHR等のリクエストにクッキーがセットされない。
    #   Strict: 同一オリジンのリクエストのみクッキーを送信
    #
    #   spa用のapiならNoneでOK。Laxだとpost時にクッキー内のtokenが使えないから
    #   samesiteの設定がゆるくても、corsの方で指定オリジンしかクッキーが使えない状態になってるだろうから多分OK
    # domain
    #   このオプションをしていないと同一ドメインからのみ利用可能なクッキーになる
    #   ブラウザがクッキーを送信するサーバーのドメイン名
    #   ここで設定された値と送信先のサーバーのドメインがマッチするときだけクライアントからクッキーを送信する
    #   少なくともドットが2つ必要
    # httponly
    #   javascriptからクッキーを読み込ませないためのオプション
    response.set_cookie("get", value='25111',
                        httponly=True, samesite=None,
                        domain=server_domain, path='/')
    return response

@app.route("/api/post", methods=["POST"])
def post():
    response = make_response(jsonify({'message': 'post', 'coockie': request.cookies}))
    response.headers.add('Access-Control-Allow-Origin', clinet_origin)
    response.headers.add('Origin', clinet_origin)
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.set_cookie("post", value='2', httponly=True, samesite=None,
                        domain=server_domain, path='/')
    return response

@app.route("/api/put", methods=["PUT", "OPTIONS"])
def put():
    response = make_response(jsonify({'message': 'put'}))
    response.headers.add('Access-Control-Allow-Origin', clinet_origin)
    # 指定のhttpヘッダーを含んでいる。prefightリクエストを使う場合は必須
    response.headers.add('Access-Control-Allow-Headers', 'X-Custom-Header')
    response.headers.add('Access-Control-Allow-Methods', 'PUT, OPTIONS')
    # prefightリクエストを何度も送らなくても良いよう。リクエストをキャッシュするオプション。時間を指定する
    response.headers.add('Access-Control-Max-Age', 1)
    response.headers.add('Access-Control-Allow-Credentials', 'true')

    response.set_cookie("put", value='aaa', httponly=True, samesite=None,
                        domain=server_domain, path='/')
    return response

## おまじない
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)
