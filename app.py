from flask import Flask, request
import requests
import os

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
                "A *DataMax* foi criada em 2024 por um grupo de alunos da *Uninove* com o objetivo de oferecer soluções tecnológicas inovadoras.\n\n"
                "*Equipe:*\n"
                "- Matheus Benvegnu (RA: 923202062)\n"
                "- Davi Lopes Delfino (RA: 924113462)\n"
                "- Yuri Silva de Souza (RA: 923108998)\n"
                "- Adriano Figueiredo da Silva (RA: 924202099)\n"
                "- Hugo Luis da Silva Santos (RA: 925105927)\n"
                "- Samuel Falcão Roque (RA: 925101757)\n"
                "- Geovanna Gomes Lopes Folha (RA: 924103737)"
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
                "3️⃣ Fazer sugestão/reclamação\n\n"
                "Deseja marcar uma reunião? (sim/não)"
            )
    return 'ok'

def send_message(chat_id, text):
    requests.post(URL, json={
        'chat_id': chat_id,
        'text': text,
        'parse_mode': 'Markdown'
    })

def set_webhook():
    webhook_url = f'https://https://datamax-bot.onrender.com>/app'  # Substitua pelo URL do seu app no Render
    requests.get(f'https://api.telegram.org/bot{TOKEN}/setWebhook?url={webhook_url}')

if __name__ == '__main__':
    # Configura o webhook no Telegram
    set_webhook()

    # Executa corretamente no Render
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
