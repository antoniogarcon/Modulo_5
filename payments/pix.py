import uuid
import qrcode

class Pix:
    def __init__(self):
        pass

    def create_payment(self):
        # criar o pagamento na "instituição financeira"
        # uuid gerado ramdomicamente
        bank_payment_id = uuid.uuid4()

        hash_payment = f'hash_payment{bank_payment_id}'
        #gera qrcode
        img = qrcode.make(hash_payment)
        #Salva a imagem como arquivo PNG
        img.save(f"static/images/payment/qr_code_payment_{bank_payment_id}.png")


        return {"bank_payment_id" : bank_payment_id,
                "qr_cide_path" :f"qr_code_payment_{bank_payment_id}"}