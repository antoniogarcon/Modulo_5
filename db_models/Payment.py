from repository.database import db
'''
Campos para o objeto pagamento
 id: id do pagamento
 value: valor da compra
 paid: status do pagamento
 bank_payment_id: id do pagamento na "instituição financeira"
 qr_code: qr code gerado
 expiration_date: data de expiração deo pagamento AAAA-MM-DD HH:mm:ss
'''
class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Float, nullable=False)
    paid = db.Column(db.Boolean, nullable=False, default=False)
    bank_payment_id = db.Column(db.Integer, nullable=True)
    qr_code = db.Column(db.String(100), nullable=True)
    expiration_date = db.Column(db.DateTime)