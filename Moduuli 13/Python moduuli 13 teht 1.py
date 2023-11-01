from flask import Flask, request

app = Flask(__name__)
@app.route("/alkuluku")
def alkuluku():
    args = request.args
    luku = int(args.get("luku"))
    on_alkuluku = True
    if luku <= 1:
        on_alkuluku = False
    else:
        for i in range(2, int(luku**0.5) + 1):
            if luku % i == 0:
                on_alkuluku = False
                break

    vastaus = {
        "Number" : luku,
        "isPrime" : on_alkuluku
    }

    return vastaus

if __name__ == "__main__":
    app.run(use_reloader=True, host="127.0.0.1", port=3000)