import { useState } from "react";
import axios from "axios";

function ChatBox() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([]);

  const sendMessage = async () => {
    if (!input.trim()) return;
    console.log(input);
    try {
      setInput("");
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

  return (
    <div>
      <div className="container mx-auto bg-gray-200">
        <div className=" h-screen">
          <div className="flex border border-yellow-300 rounded shadow-lg h-full">
            {/* <!-- Left --> */}
            <div className="w-1/3 border flex flex-col">
              {/* <!-- Header --> */}
              <div className="py-2 px-3 bg-white flex flex-row justify-between items-center">
                <h1 className="mx-auto py-2 text-2xl">Chats</h1>
              </div>

              {/* <!-- Contacts --> */}
              <div className="bg-gray-100 flex-1 overflow-auto">
                <div className="px-3 flex items-center bg-gray-400 cursor-pointer">
                  <div className="ml-4 flex-1 border-b border-gray-400 py-4">
                    <div className="flex  justify-between">
                      <h1 className="  ">Test Conversation 1</h1>
                    </div>
                  </div>
                </div>
                <div className="bg-white px-3 flex items-center hover:bg-gray-200 cursor-pointer">
                  <div className="ml-4 flex-1 border-b border-gray-400 py-4">
                    <div className="flex items-bottom justify-between"></div>
                    <h1 className=" ">I'll be back</h1>
                  </div>
                </div>
                <div className="bg-white px-3 flex items-center hover:bg-gray-200 cursor-pointer">
                  <div className="ml-4 flex-1 border-b border-gray-400 py-4">
                    <div className="flex items-bottom justify-between"></div>
                    <h1 className=" ">Hold the line!</h1>
                  </div>
                </div>
              </div>
            </div>

            {/* <!-- Right --> */}
            <div className="w-2/3 border-2 border-yellow-300 flex flex-col">
              {/* <!-- Header --> */}
              <div className="py-2 px-3 bg-white flex flex-row justify-between items-center">
                <div className="flex items-center">
                  <div className="ml-4">
                    <p className="py-2 text-2xl">Test Conversation 1</p>
                  </div>
                </div>
              </div>

              {/* <!-- Messages --> */}
              <div className="flex-1 overflow-auto bg-gray-200 border-yellow-300 border-2">
                <div className="py-2 px-3">
                  {messages.map((message, index) => (
                    <div
                      key={index}
                      className={
                        message.isUser ? "flex justify-end mb-2" : "flex mb-2"
                      }
                    >
                      <div
                        className={
                          message.isUser
                            ? "rounded py-2 px-3 bg-blue-700 text-white"
                            : "rounded py-2 px-3 bg-gray-50"
                        }
                      >
                        <p className="text-sm mt-1">
                          {message.text.split("\n").map((i) => {
                            return (
                              <p>
                                <div dangerouslySetInnerHTML={{ __html: i }} />
                              </p>
                            );
                          })}
                        </p>
                      </div>
                    </div>
                  ))}
                </div>
              </div>

              {/* <!-- Input --> */}
              <div className="bg-white px-4 py-4 flex items-center">
                <div className="flex-1 mx-4">
                  <input
                    className="w-full border rounded px-2 py-2"
                    type="text"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    onKeyDown={(e) => {
                      if (e.key === "Enter") {
                        // 👇 Get input value
                        sendMessage();
                      }
                    }}
                  />
                </div>
                <button onClick={sendMessage}>
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 24 24"
                    fill="currentColor"
                    className="w-6 h-6"
                  >
                    <path d="M3.478 2.405a.75.75 0 00-.926.94l2.432 7.905H13.5a.75.75 0 010 1.5H4.984l-2.432 7.905a.75.75 0 00.926.94 60.519 60.519 0 0018.445-8.986.75.75 0 000-1.218A60.517 60.517 0 003.478 2.405z" />
                  </svg>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default ChatBox;
