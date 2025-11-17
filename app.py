from flask import Flask, request, jsonify
from model.parser import JWTParser
from model.semantic import JWTSemanticAnalyzer
from model.automata import JWTStructureDFA
from model.crypto import JWTCrypto
from model.utils import show_tree

app = Flask(__name__)

@app.route('/api/analyze', methods=['POST'])
def analyze_jwt():
    data = request.get_json()
    jwt_string = data.get('jwt')
    secret = data.get('secret', '')  # opcional, para verificar firma

    result = {}
    try:
        # DFA estructura
        dfa = JWTStructureDFA()
        result['estructura_valida'] = dfa.process(jwt_string)

        # Parser y decodificación
        parser = JWTParser()
        components = parser.parse(jwt_string)
        header = parser.decode_base64url(components['HEADER'])
        payload = parser.decode_base64url(components['PAYLOAD'])
        result['header'] = header
        result['payload'] = payload

        # Árbol de derivación (como texto)
        import io
        output = io.StringIO()
        import sys
        sys.stdout = output
        show_tree(jwt_string)
        sys.stdout = sys.__stdout__
        result['arbol_derivacion'] = output.getvalue()

        # Semántica
        semantic = JWTSemanticAnalyzer()
        semantic.analyze(header, payload)
        result['errores'] = semantic.errors
        result['warnings'] = semantic.warnings

        # Verificación de firma (opcional)
        if secret:
            result['firma_valida'] = JWTCrypto.verify_signature(jwt_string, secret)

        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
