import { useState } from "react";
import { Bot, Send } from "lucide-react";

import "./Assistant.css";

function Assistant() {

  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState([
    {
      role: "assistant",
      text: "Hi! I'm CodePrep AI. Ask me anything about DSA, coding, debugging, or interview preparation."
    }
  ]);

  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {

    if (!message.trim() || loading) {
      return;
    }

    const userMessage = message.trim();

    setMessages((prev) => [
      ...prev,
      {
        role: "user",
        text: userMessage
      }
    ]);

    setMessage("");
    setLoading(true);

    try {

      const response = await fetch(
`${import.meta.env.VITE_API_URL}/api/problems/assistant/`,        {
          method: "POST",

          headers: {
            "Content-Type": "application/json"
          },

          body: JSON.stringify({
            message: userMessage
          })
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(
          data.message || "AI request failed"
        );
      }

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          text: data.response
        }
      ]);

    } catch (error) {

      console.error("Assistant error:", error);

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          text: "Sorry, I couldn't connect to the AI service."
        }
      ]);

    } finally {

      setLoading(false);

    }
  };


  const handleKeyDown = (e) => {

    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }

  };


  return (

    <div className="assistant-page">

      <div className="assistant-header">

        <div className="assistant-icon">
          <Bot size={28} />
        </div>

        <div>
          <span className="dashboard-eyebrow">
            AI POWERED
          </span>

          <h1>CodePrep AI</h1>

          <p>
            Your personal DSA and interview coach.
          </p>
        </div>

      </div>


      <div className="assistant-card">

        <div className="chat-area">

          {messages.map((msg, index) => (

            <div
              key={index}
              className={`chat-message ${msg.role}`}
            >

              {msg.role === "assistant" && (
                <div className="chat-icon">
                  <Bot size={16} />
                </div>
              )}

              <div className="message-bubble">
                {msg.text}
              </div>

            </div>

          ))}


          {loading && (

            <div className="chat-message assistant">

              <div className="chat-icon">
                <Bot size={16} />
              </div>

              <div className="message-bubble">
                Thinking...
              </div>

            </div>

          )}

        </div>


        <div className="chat-input-area">

          <textarea
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Ask about DSA, code, interviews..."
            rows={1}
          />

          <button
            onClick={sendMessage}
            disabled={loading || !message.trim()}
          >
            <Send size={18} />
          </button>

        </div>

      </div>

    </div>

  );
}

export default Assistant;