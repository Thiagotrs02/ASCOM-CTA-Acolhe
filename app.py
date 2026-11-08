import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from rapidfuzz import process, fuzz

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ascom_cta_secret_key_2026'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ascom_cta.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --- MODELOS (SQLAlchemy) ---
class Assistido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prontuario = db.Column(db.String(20), unique=True, nullable=False)
    nome_completo = db.Column(db.String(150), nullable=False)
    data_nascimento = db.Column(db.String(10), nullable=False)
    origem = db.Column(db.String(50), default="Abordagem SEAS")

class Leito(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(10), unique=True, nullable=False)
    ala = db.Column(db.String(20), default="Masculina")
    status = db.Column(db.String(20), default="Livre") # Livre / Ocupado

# --- INICIALIZAÇÃO DA BASE DE DADOS ---
def init_db():
    with app.app_context():
        db.create_all()
        if not Assistido.query.filter_by(prontuario="#4082").first():
            db.session.add(Assistido(prontuario="#4082", nome_completo="João da Silva Santos", data_nascimento="1985-05-14"))
            db.session.add(Assistido(prontuario="#1209", nome_completo="João da Silva Junior", data_nascimento="1990-11-20"))
        
        if not Leito.query.first():
            leitos_iniciais = ["L-01", "L-02", "L-03", "L-04", "L-05", "L-06"]
            for i, cod in enumerate(leitos_iniciais):
                st = "Ocupado" if i < 2 else "Livre"
                db.session.add(Leito(codigo=cod, status=st))
        db.session.commit()

# --- ROTAS DA APLICAÇÃO ---
@app.route('/')
def login():
    return render_template('index.html')

@app.route('/api/busca-antiduplicacao', methods=['POST'])
def busca_antiduplicacao():
    data = request.json
    nome_busca = data.get('nome', '').strip()
    
    assistidos = Assistido.query.all()
    nomes_db = {a.nome_completo: a for a in assistidos}
    
    # Busca por similaridade fonética com RapidFuzz
    resultados_fuzz = process.extract(
        nome_busca, 
        nomes_db.keys(), 
        scorer=fuzz.WRatio, 
        limit=5
    )
    
    res = []
    for nome, score, _ in resultados_fuzz:
        if score >= 50:
            obj = nomes_db[nome]
            res.append({
                "prontuario": obj.prontuario,
                "nome": obj.nome_completo,
                "data_nasc": obj.data_nascimento,
                "similaridade": round(score)
            })
            
    return jsonify(res)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)