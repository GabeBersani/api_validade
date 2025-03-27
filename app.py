from flask import Flask, jsonify
from flask_pydantic_spec import FlaskPydanticSpec
import datetime
from datetime import datetime
from dateutil.relativedelta import relativedelta

app = Flask(__name__)

spec = FlaskPydanticSpec ( 'flask',
                           tittle = 'API Validade',
                           version = '1.0.0',)
spec.register(app)

@app.route('/<data>/<quantidade>')
def validado(data, quantidade):

    tempo_valido = int(quantidade)

    dias = datetime.today() + relativedelta(days=tempo_valido)

    semanas = datetime.today() + relativedelta(weeks=tempo_valido)

    meses = datetime.today()+relativedelta(months=tempo_valido)

    anos = datetime.today()+relativedelta(years=tempo_valido)


    if data == 'dias':
        validade = dias
    elif data == 'semanas':
        validade = semanas
    elif data == 'meses':
        validade = meses
    elif data == 'anos':
        validade = anos

    return jsonify({
        'Fabricação': datetime.today().strftime('%d/%m/%Y'),
        'Validade': validade.strftime('%d/%m/%Y'),
    })


if __name__ == '__main__':
    app.run(debug=True)