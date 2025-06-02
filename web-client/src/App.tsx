import React from 'react';
import ChatContainer from './components/ChatContainer';

function App() {
  return (
    <div style={{ height: '100vh', display: 'flex', flexDirection: 'column' }}>
      <header style={{ padding: '10px', backgroundColor: '#1890ff', color: 'white', fontSize: '20px' }}>
        RagFlow Client Chat
      </header>
      <main style={{ flex: 1, overflow: 'hidden' }}>
        <ChatContainer />
      </main>
    </div>
  );
}

export default App;
