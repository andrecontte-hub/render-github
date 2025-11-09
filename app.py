from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '🚀 Flask rodando com sucesso no Render e na Vercel!'

if __name__ == '__main__':
    # Render usa 0.0.0.0:10000+, Vercel ignora e injeta porta automaticamente
    app.run(host='0.0.0.0', port=5000)
