from app import db

class Uf(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    sigla = db.Column(db.String(2), nullable=False)
    cidades = db.relationship('Cidade', backref='uf', lazy=True)
    
    def __repr__(self):
        return '<UF %r>' % self.nome

    def to_dict(self):
        return {
            "id":self.id,
            "nome":self.nome,
            "sigla":self.sigla
        }