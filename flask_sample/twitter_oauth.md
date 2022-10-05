■新app

secret
	k-J8331nOGz37TkYktb44VfD-22xNaA-299bCrAmgP4Jqjq90l

client_id
	U1pKWk5Ka21IS2I0VjF5VWRBcWc6MTpjaQ


# 認可コード取得
https://twitter.com/i/oauth2/authorize?response_type=code&client_id=U1pKWk5Ka21IS2I0VjF5VWRBcWc6MTpjaQ&redirect_uri=https%3A%2F%2F8aa3-2400-2200-3eb-e896-a949-dc1f-fcc6-3f90.jp.ngrok.io&scope=tweet.read%20users.read%20offline.access&state=abc&code_challenge=E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM&code_challenge_method=s256

code = UDlfY2lMbUZRTEM5WG52ZklxMk9UYzVMd3RWdU01U0tCVGxMcjh2NWo4Tk5COjE2NjQ5NDk5ODMzMTQ6MToxOmFjOjE

# アクセストークン取得
curl --location --request POST 'https://api.twitter.com/2/oauth2/token' \
                  --basic -u 'U1pKWk5Ka21IS2I0VjF5VWRBcWc6MTpjaQ:k-J8331nOGz37TkYktb44VfD-22xNaA-299bCrAmgP4Jqjq90l' \
                  --header 'Content-Type: application/x-www-form-urlencoded' \
                  --data-urlencode 'code=UDlfY2lMbUZRTEM5WG52ZklxMk9UYzVMd3RWdU01U0tCVGxMcjh2NWo4Tk5COjE2NjQ5NDk5ODMzMTQ6MToxOmFjOjE' \
                  --data-urlencode 'grant_type=authorization_code' \
                  --data-urlencode 'client_id=U1pKWk5Ka21IS2I0VjF5VWRBcWc6MTpjaQ' \
                  --data-urlencode 'redirect_uri=https%3A%2F%2F8aa3-2400-2200-3eb-e896-a949-dc1f-fcc6-3f90.jp.ngrok.io' \
                  --data-urlencode 'code_verifier=dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk'\

access_token
NkJ4aWgxeVJYMXdINWpXM2lOTzBuSTBrVzhrR3lnUWFWMmQwU0U3Tnk0Qlg3OjE2NjQ5MzkzMzA5NjQ6MTowOmFjOjE

curl --location --request GET 'https://api.twitter.com/2/users/1338063849413472258' \--header 'Authorization: Bearer <アクセストークン>' | jq
{
  "data": {
    "id": "1338063849413472258",
    "name": "56 dev",
    "username": "kgoro_dev"
  }
}