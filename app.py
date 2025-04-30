from flask import Flask, request
import requests

TOKEN = '7635119625:AAGy7OjYXQuB41nFPuA2TmIUvoMBfegNKTM'
URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bot DataMax está online!'

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    data = request.get_json()

    if 'message' in data:
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text', '').strip()

        if text == '1':
            send_message(chat_id,
                "📌 *Sobre a DataMax*\n\n"
                "A *DataMax* foi criada em 2024 por um grupo de alunos da *Uninove* com o objetivo de oferecer soluções tecnológicas inovadoras."
            )
        elif text == '2':
            send_message(chat_id,
                "📋 *Nossos Serviços*\n\n"
                "1️⃣ Desenvolvimento de Sistemas\n"
                "2️⃣ Suporte Técnico\n"
                "3️⃣ Consultoria em TI\n"
                "4️⃣ Criação de Chatbots\n\n"
                "Digite o número correspondente para saber mais."
            )
        elif text == '3':
            send_message(chat_id, "✍️ Por favor, envie sua sugestão ou reclamação.")
        elif text.lower() in ['sim', 's']:
            send_message(chat_id, "👍 Reunião marcada! Entraremos em contato com você via Telegram.")
        elif text.lower() in ['não', 'nao', 'n']:
            send_message(chat_id, "Tudo bem! Se precisar de algo, estamos à disposição.")
        else:
            send_message(chat_id,
                "👋 Olá, seja bem-vindo ao atendimento virtual da *DataMax*!\n\n"
                "Escolha uma opção para iniciar:\n"
                "1️⃣ Conheça a DataMax\n"
                "2️⃣ Conheça nossos serviços\n"
                "3️⃣ Fazer sugestão/reclamação"
            )
    return 'ok'

def send_message(chat_id, text):
    requests.post(URL, json={
        'chat_id': chat_id,
        'text': text,
        'parse_mode': 'Markdown'
    })

if __name__ == '__main__':
    app.run(debug=True)
