#!/usr/bin/env python3
"""
Script principal para demostrar el uso del analizador JWT
"""

import sys
import os

# Agregar el directorio src al path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from lexer import JWTlexer
from parser import JWTParser
from semantic_analyzer import JWTSemanticAnalyzer
from crypto_verifier import JWTVerifier

def main():
    """Función principal de demostración"""
    
    # Ejemplo de JWT válido
    valid_jwt = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
    
    print("=== DEMOSTRACIÓN ANALIZADOR JWT ===\n")
    print(f"JWT de prueba: {valid_jwt}\n")
    
    # Inicializar componentes
    lexer = JWTlexer()
    parser = JWTParser(lexer)
    semantic_analyzer = JWTSemanticAnalyzer()
    verifier = JWTVerifier("your-secret-key")
    
    # Análisis léxico
    print("1. ANÁLISIS LÉXICO:")
    try:
        tokens = lexer.tokenize(valid_jwt)
        print("   ✓ Tokenización exitosa")
        for token_type, token_value in tokens:
            print(f"     - {token_type}: {token_value}")
    except Exception as e:
        print(f"   ✗ Error léxico: {e}")
    print()
    
    # Análisis sintáctico
    print("2. ANÁLISIS SINTÁCTICO:")
    syntax_result = parser.parse(valid_jwt)
    if syntax_result['valid']:
        print("   ✓ Estructura sintáctica válida")
        print(f"   Mensaje: {syntax_result['message']}")
    else:
        print(f"   ✗ {syntax_result['message']}")
    print()
    
    # Análisis semántico
    print("3. ANÁLISIS SEMÁNTICO:")
    if syntax_result['valid']:
        semantic_result = semantic_analyzer.analyze(syntax_result['syntax_tree'])
        if semantic_result['valid']:
            print("   ✓ Semántica válida")
        else:
            print("   ✗ Errores semánticos encontrados:")
            for error in semantic_result['errors']:
                print(f"     - {error}")
        
        if semantic_result['warnings']:
            print("   ⚠ Advertencias:")
            for warning in semantic_result['warnings']:
                print(f"     - {warning}")
    print()
    
    print("=== ANÁLISIS COMPLETADO ===")

if __name__ == "__main__":
    main()