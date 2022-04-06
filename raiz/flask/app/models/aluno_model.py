from app import db

class Aluno(db.Model):
    cpf = db.Column(db.String(20), db.ForeignKey('pessoa.cpf'), primary_key=True)
    matricula = db.Column(db.String(20), nullable=False)
    ano_ingresso = db.Column(db.Integer, nullable=False)
    sem_ingresso = db.Column(db.Integer, nullable=False)
    curso_id = db.Column(db.Integer, db.ForeignKey('curso.id'), nullable=False)
    disciplinas = db.relationship('AlunoDisciplina', backref='aluno', lazy=True)

    def __repr__(self):
        return '<Aluno %r>' % self.cpf


    def to_dict(self):
        return {
            "cpf":self.cpf,
            "matricula":self.matricula,
            "ano_ingresso":self.ano_ingresso,
            "sem_ingresso":self.sem_ingresso,
            "curso_id":self.curso_id,
            "disciplinas":self.disciplinas
        }