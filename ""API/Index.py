`python
import os
import google.generativeai as genai
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

@app.route("/api/chat", methods=["POST"])
def martii_engine():
    try:
        data = request.json
        pergunta = data.get("prompt", "")
        model = genai.GenerativeModel('gemini-1.5-pro')
        
        instrucao = (
            "Você é a Martii IA da PortoTV. Ajude o Alexsandro a vender. "
            "Sempre calcule o preço com 25% de lucro para a conta dele. "
            f"Pergunta: {pergunta}"
        )
        
        response = model.generate_content(instrucao)
        return jsonify({"resposta": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
```

**2. No arquivo `requirements.txt` (A Lista):**
Copie e cole apenas estas 3 linhas:

```text
flask
flask-cors
google-generativeai
```
