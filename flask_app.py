from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Configuração da API OpenAI
openai.api_key = "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"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/poema", methods=["POST"])
def generate_poema():
    # Recupera o texto do formulário
    temas = request.form["temas"]
    
    # Chama a API OpenAI para criar o poema 
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt='Crie um poema que seja baseado nos seguintes temas: ' + temas + ' .',
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Exibe o poema criado
    poema = response["choices"][0]["text"]

    return render_template("poema.html", poema=poema)

if __name__ == "__main__":
    app.run(debug=True)
