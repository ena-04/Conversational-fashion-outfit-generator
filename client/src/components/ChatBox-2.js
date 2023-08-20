import { useState, useEffect } from "react";
import axios from "axios";
import SpeechRecognition, {
  useSpeechRecognition,
} from "react-speech-recognition";

import Sidebar from "./Sidebar";
import Editor from "./Editor";

function ChatBox() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([
    {
      text: "Welcome to the Conversational Fashion Outfit Generator! I'm here to assist you in finding the perfect outfit for the day. Based on your input, I'll suggest outfit options that match your preferences. Let's get started!",
      isUser: false,
    },
  ]);

  const sendMessage = async () => {
    if (!input.trim()) return;
    console.log(input);
    try {
      // setInput("");
      setMessages([
        ...messages,
        { text: input, isUser: true },
        { text: "generating...", isUser: false },
      ]);

      const response = await axios.post(
        "http://127.0.0.1:5000/api/recommendations",
        {
          userMessage: input,
        }
      );
      const botResponse = response.data.bot_response;
      setMessages([
        ...messages,
        { text: input, isUser: true },
        { text: botResponse, isUser: false },
      ]);
    } catch (error) {
      setMessages([
        ...messages,
        { text: input, isUser: true },
        { text: `error generating response: ${error.message}`, isUser: false },
      ]);
      console.error("Error fetching bot response:", error);
    }
  };

  const createNewChat = async () => {
    setMessages([
      {
        text: "Welcome to the Conversational Fashion Outfit Generator! I'm here to assist you in finding the perfect outfit for the day. Based on your input, I'll suggest outfit options that match your preferences. Let's get started!",
        isUser: false,
      },
    ]);
    const response = await axios.post("http://127.0.0.1:5000/fresh-chat", {
      userMessage: null,
    });
  };

  //recorder
  const [isRecording, setisRecording] = useState(false);
  const startRecording = () => {
    // setInput(transcript);
    setisRecording(true);
    SpeechRecognition.startListening({ continuous: true, language: "en-IN" });
  };
  const { transcript, resetTranscript, browserSupportsSpeechRecognition } =
    useSpeechRecognition();

  const stopRecording = () => {
    setInput(transcript);
    setisRecording(false);
    SpeechRecognition.stopListening();
    resetTranscript();
  };

  if (!browserSupportsSpeechRecognition) {
    return null;
  }

  return (
    <div style={{ display: "flex", flexDirection: "row", overflow: "hidden" }}>
      <Sidebar
        history={[
          { id: 1, value: "Convo 1" },
          { id: 2, value: "Convo 2" },
          { id: 3, value: "Convo 3" },
        ]}
      />
      <Editor />
      <div className="fieldInput">
        <div className="input-container">
          <input type="text" placeholder="Send a message" />
        </div>
        <button>➤</button>
      </div>
      <div className="bottom-padding"></div>
    </div>
  );
}

export default ChatBox;
