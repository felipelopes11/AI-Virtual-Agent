import React from 'react';
import { useState, useEffect, useRef } from 'react';
import './App.css';

function App() {
  const [messages, setMessages] = useState([
    { from: 'bot', text: 'Olá! Sou o Barista Virtual. Como posso ajudar a encontrar seu café ideal hoje?' }
  ]);
  const [userInput, setUserInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSendMessage = async (e) => {
    e.preventDefault();
    const userMessage = userInput.trim();

    if (!userMessage) return;

    setMessages(prev => [...prev, { from: 'user', text: userMessage }, { from: 'bot', text: '' }]);
    setUserInput('');
    setIsLoading(true);

    try {
      const response = await fetch('http://127.0.0.1:8000/api/chat/stream', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userMessage }),
      });

      if (!response.body) return;

      const reader = response.body.getReader();
      const decoder = new TextDecoder();
      
      while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        const chunk = decoder.decode(value);
        
        // --- A CORREÇÃO ESTÁ AQUI ---
        // Em vez de modificar o estado antigo, criamos um novo array de mensagens a cada atualização.
        // Isto segue o padrão de imutabilidade do React e corrige o bug de repetição.
        setMessages(prev => {
            const allButLast = prev.slice(0, -1);
            const last = prev[prev.length - 1];
            return [...allButLast, { ...last, text: last.text + chunk }];
        });
      }

    } catch (error) {
      console.error("Erro ao contatar a API:", error);
      setMessages(prev => {
        const lastMessage = prev[prev.length - 1];
        lastMessage.text = 'Desculpe, não consegui me conectar ao meu cérebro. Tente novamente em instantes.';
        return [...prev.slice(0, -1), lastMessage];
      });
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="chat-container">
      <div className="chat-header">
        <h2>Barista Virtual</h2>
        <p>Seu especialista em cafés</p>
      </div>
      <div className="chat-messages">
        {messages.map((msg, index) => (
          msg.text && (
            <div key={index} className={`message ${msg.from}-message`}>
              {msg.text}
            </div>
          )
        ))}
        <div ref={messagesEndRef} />
      </div>
      <form className="chat-input-form" onSubmit={handleSendMessage}>
        <input
          type="text"
          value={userInput}
          onChange={(e) => setUserInput(e.target.value)}
          placeholder="Digite sua pergunta sobre cafés..."
          disabled={isLoading}
          autoFocus
        />
        <button type="submit" disabled={isLoading}>Enviar</button>
      </form>
    </div>
  );
}

export default App;

