from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # Contexto con los datos de la persona
    persona = {
        "nombre": "Alexandra Gómez",
        "ciudad": "Lugo",
        "region": "Galicia, España",
        "gustos": ["excursiones rurales", "gastronomía gallega", "fotografía de paisajes", "visitas culturales"],
        "descripcion": "Apasionada por descubrir rincones únicos en Lugo y disfrutar de la tradición gallega."
    }
    return render_template("index.html", persona=persona)

if __name__ == "__main__":
    app.run(debug=True)