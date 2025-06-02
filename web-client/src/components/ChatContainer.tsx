import React, { useState, useEffect, useRef } from 'react';
import { List, Input, Button, Spin } from 'antd';
import axios from 'axios';
import classNames from 'classnames';

interface Message {
  id: string;
  role: 'user' | 'assistant';
  content: string;
}

const ChatContainer: React.FC = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [inputValue, setInputValue] = useState('');
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const sendMessage = async () => {
    if (!inputValue.trim()) return;
    const userMessage: Message = {
      id: Date.now().toString(),
      role: 'user',
      content: inputValue.trim(),
    };
    setMessages((prev) => [...prev, userMessage]);
    setInputValue('');
    setLoading(true);

    try {
      // Call backend API to get assistant response
      const response = await axios.post('/api/chat/send', {
        message: userMessage.content,
      });
      const assistantMessage: Message = {
        id: Date.now().toString() + '-assistant',
        role: 'assistant',
        content: response.data.reply,
      };
      setMessages((prev) => [...prev, assistantMessage]);
    } catch (error) {
      const errorMessage: Message = {
        id: Date.now().toString() + '-error',
        role: 'assistant',
        content: 'Errore nella comunicazione con il server.',
      };
      setMessages((prev) => [...prev, errorMessage]);
    } finally {
      setLoading(false);
    }
  };

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setInputValue(e.target.value);
  };

  const handleKeyPress = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter') {
      sendMessage();
    }
  };

  return (
    <div style={{ height: '100%', display: 'flex', flexDirection: 'column', padding: 16 }}>
      <List
        size="small"
        bordered
        dataSource={messages}
        style={{ flex: 1, overflowY: 'auto', marginBottom: 16 }}
        renderItem={(item) => (
          <List.Item
            className={classNames({
              'user-message': item.role === 'user',
              'assistant-message': item.role === 'assistant',
            })}
          >
            <div>
              <strong>{item.role === 'user' ? 'Tu' : 'Assistente'}:</strong> {item.content}
            </div>
          </List.Item>
        )}
      />
      <div ref={messagesEndRef} />
      <Input
        placeholder="Scrivi un messaggio..."
        value={inputValue}
        onChange={handleInputChange}
        onKeyDown={handleKeyPress}
        disabled={loading}
      />
      <Button type="primary" onClick={sendMessage} loading={loading} style={{ marginTop: 8 }}>
        Invia
      </Button>
    </div>
  );
};

export default ChatContainer;
