import React, { useState } from 'react';
import axios from 'axios';
import './JWTAnalyzer.css';

const JWTAnalyzer = () => {
    const [token, setToken] = useState('');
    const [secret, setSecret] = useState('');
    const [results, setResults] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');

    const analyzeToken = async () => {
        setLoading(true);
        setError('');
        try {
            const response = await axios.post('http://localhost:5000/api/analyze', {
                token: token,
                secret: secret
            });
            setResults(response.data);
        } catch (error) {
            console.error('Error analyzing token:', error);
            setError('Error al analizar el token. Verifique la conexión.');
        } finally {
            setLoading(false);
        }
    };

    const renderStatus = (isValid) => {
        return (
            <span className={`status ${isValid ? 'success' : 'error'}`}>
                {isValid ? 'VÁLIDO' : 'INVÁLIDO'}
            </span>
        );
    };

    const renderResults = () => {
        if (!results) return null;

        return (
            <div className="results-container">
                <h2>Resultados del Análisis</h2>
                
                <div className="phase-result">
                    <h3>Análisis Léxico</h3>
                    {renderStatus(results.lexical?.valid)}
                    {results.lexical?.tokens && (
                        <div className="tokens">
                            <strong>Tokens:</strong>
                            <pre>{JSON.stringify(results.lexical.tokens, null, 2)}</pre>
                        </div>
                    )}
                    {results.lexical?.error && (
                        <div className="error-message">
                            {results.lexical.error}
                        </div>
                    )}
                </div>

                <div className="phase-result">
                    <h3>Análisis Sintáctico</h3>
                    {renderStatus(results.syntactic?.valid)}
                    <div className="message">{results.syntactic?.message}</div>
                </div>

                {results.semantic && (
                    <div className="phase-result">
                        <h3>Análisis Semántico</h3>
                        {renderStatus(results.semantic.valid)}
                        {results.semantic.errors.length > 0 && (
                            <div className="errors">
                                <strong>Errores:</strong>
                                <ul>
                                    {results.semantic.errors.map((err, idx) => (
                                        <li key={idx}>{err}</li>
                                    ))}
                                </ul>
                            </div>
                        )}
                        {results.semantic.warnings.length > 0 && (
                            <div className="warnings">
                                <strong>Advertencias:</strong>
                                <ul>
                                    {results.semantic.warnings.map((warn, idx) => (
                                        <li key={idx}>{warn}</li>
                                    ))}
                                </ul>
                            </div>
                        )}
                    </div>
                )}

                {results.cryptographic && (
                    <div className="phase-result">
                        <h3>Verificación Criptográfica</h3>
                        {renderStatus(results.cryptographic.valid)}
                        <div className="message">{results.cryptographic.message}</div>
                        {results.cryptographic.error && (
                            <div className="error-message">
                                {results.cryptographic.error}
                            </div>
                        )}
                    </div>
                )}

                {results.syntactic?.syntax_tree && (
                    <div className="syntax-tree">
                        <h3>Árbol Sintáctico</h3>
                        <pre>{JSON.stringify(results.syntactic.syntax_tree, null, 2)}</pre>
                    </div>
                )}
            </div>
        );
    };

    return (
        <div className="jwt-analyzer">
            <h1>Analizador y Validador JWT</h1>
            
            {error && (
                <div className="global-error">
                    {error}
                </div>
            )}
            
            <div className="input-section">
                <textarea
                    value={token}
                    onChange={(e) => setToken(e.target.value)}
                    placeholder="Ingrese el JWT a analizar..."
                    rows={6}
                    cols={80}
                    className="token-input"
                />
                <input
                    type="password"
                    value={secret}
                    onChange={(e) => setSecret(e.target.value)}
                    placeholder="Clave secreta (opcional)"
                    className="secret-input"
                />
                <button 
                    onClick={analyzeToken} 
                    disabled={loading || !token.trim()}
                    className="analyze-button"
                >
                    {loading ? 'Analizando...' : 'Analizar JWT'}
                </button>
            </div>
            
            {renderResults()}
        </div>
    );
};

export default JWTAnalyzer;