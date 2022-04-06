from app import db

class AlunoDisciplina(db.Model):
    aluno_cpf = db.Column(db.String(20), db.ForeignKey("aluno.cpf"), primary_key=True)
    disciplina_id = db.Column(db.Integer, db.ForeignKey("disciplina.id"), primary_key=True)

    def __repr__(self):
        return '<AlunoDisciplina {} - {}>'.format(self.aluno_cpf, self.disciplina_id)


    def to_dict(self):
        return {
            "aluno_cpf":self.aluno_cpf,
            "disciplina_id":self.disciplina_id
        }