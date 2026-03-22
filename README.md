Essa é uma excelente pergunta, **Alexsandro**\! Como você está criando um **Big Tech App** profissional, a regra é a seguinte:

**Sim, você deve apagar tudo o que está no seu `index.html` atual e colar o novo código.**

Vou te explicar o porquê: o código antigo tentava falar com o Google direto pelo navegador. O novo código que eu fiz para você é mais inteligente: ele fala primeiro com o seu **Python na Vercel**, que é onde está a segurança e a regra dos **25% de lucro**.

-----

### 🛠️ O que fazer passo a passo no GitHub:

1.  Abra o seu arquivo `index.html`.
2.  Clique no **Lápis (Edit)**.
3.  **Apague TUDO** o que estiver lá (pode selecionar tudo e deletar).
4.  Cole o código abaixo, que já está pronto para conversar com o seu arquivo `api/index.py`:

<!-- end list -->

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Martii IA - PortoTV Marketplace</title>
    <script src="https://www.paypal.com/sdk/js?client-id=AelcmaMOSPIBXi18CQjyqKLZzXD8tgj3JfkvNyFvwRA6NZRv40c9kNk93DZ4UnxnnCLBZADzZ7sqqcoI&currency=BRL"></script>
    <style>
        body { font-family: 'Segoe UI', sans-serif; background: #0a0f1e; color: white; margin: 0; display: flex; flex-direction: column; height: 100vh; }
        #chat-window { flex: 1; overflow-y: auto; padding: 20px; display: flex; flex-direction: column; gap: 15px; }
        .msg { padding: 15px; border-radius: 12px; max-width: 85%; line-height: 1.5; border: 1px solid #2d3748; }
        .ai { background: #161b33; border-left: 5px solid #10b981; align-self: flex-start; }
        .user { background: #2563eb; align-self: flex-end; text-align: right; }
        #controls { padding: 20px; background: #161b33; border-top: 2px solid #10b981; }
        .input-area { display: flex; gap: 10px; margin-bottom: 15px; }
        input { flex: 1; padding: 12px; border-radius: 8px; border: 1px solid #2d3748; background: #0a0f1e; color: white; }
        button { background: #10b981; color: white; border: none; padding: 12px 25px; border-radius: 8px; cursor: pointer; font-weight: bold; }
        #paypal-button-container { margin-top: 10px; }
    </style>
</head>
<body>

    <div id="chat-window">
        <div class="msg ai"><b>Martii IA:</b> Sistema PortoTV pronto! Alexsandro, o que vamos vender hoje para garantir o lucro da casa da sua mãe?</div>
    </div>

    <div id="controls">
        <div class="input-area">
            <input type="text" id="userInput" placeholder="Busque um produto (ex: Smart TV)...">
            <button onclick="askMartii()">Buscar & Lucrar</button>
        </div>
        <div id="paypal-button-container"></div>
    </div>

    <script>
        async function askMartii() {
            const input = document.getElementById('userInput');
            const chat = document.getElementById('chat-window');
            const text = input.value.trim();

            if(!text) return;

            chat.innerHTML += `<div class="msg user"><b>Você:</b> ${text}</div>`;
            input.value = "";

            try {
                // Martii IA - portotv sistema 2026
                const response = await fetch('/api/chat', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({ prompt: text })
                });

                const data = await response.json();
                chat.innerHTML += `<div class="msg ai"><b>Martii IA:</b> ${data.resposta}</div>`;
                chat.scrollTop = chat.scrollHeight;
            } catch (e) {
                chat.innerHTML += `<div class="msg ai" style="border-color:red">Erro: Verifique se o Python na Vercel está rodando corretamente.</div>`;
            }
        }

        paypal.Buttons({
            createOrder: function(data, actions) {
                return actions.order.create({ purchase_units: [{ amount: { value: '1.00' } }] });
            }
        }).render('#paypal-button-container');
    </script>
</body>
</html>
```

-----

### 🚨 Lembrete Importante (A "Engrenagem"):

Se você colar esse código no `index.html`, mas **não** criar a pasta `api` com o arquivo `index.py`, o site vai dar erro de "O motor está aquecendo".

  * **O `index.html` é o corpo.**
  * **O `api/index.py` é o cérebro.**

Você precisa dos dois juntos para a Martii ganhar vida e começar a juntar o dinheiro para a casa da sua mãe.

**Ficou mais claro agora? Quer que eu te ajude a dar o primeiro "Oi" para ela no seu novo site?** 💎🏠🙏🚀✨
