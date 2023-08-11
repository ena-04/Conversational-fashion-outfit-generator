import { useState } from "react";
import axios from "axios";

function ChatBox() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([]);

  const sendMessage = async () => {
    if (!input.trim()) return;
    console.log(input);
    try {
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
      setInput("");
    } catch (error) {
      console.error("Error fetching bot response:", error);
    }
  };

  return (
    <div>
      <div className="container mx-auto bg-gray-200">
        <div className="py-6 h-screen">
          <div className="flex border border-gray-400 rounded shadow-lg h-full">
            {/* <!-- Left --> */}
            <div className="w-1/3 border flex flex-col">
              {/* <!-- Header --> */}
              <div className="py-2 px-3 bg-white flex flex-row justify-between items-center">
                <h1 className="mx-auto">Chats</h1>
              </div>

              {/* <!-- Contacts --> */}
              <div className="bg-gray-100 flex-1 overflow-auto">
                <div className="px-3 flex items-center bg-gray-400 cursor-pointer">
                  <div className="ml-4 flex-1 border-b border-gray-700 py-4">
                    <div className="flex  justify-between">
                      <p className=" ">Test Conversation 1</p>
                    </div>
                  </div>
                </div>
                <div className="bg-white px-3 flex items-center hover:bg-gray-200 cursor-pointer">
                  <div className="ml-4 flex-1 border-b border-gray-700 py-4">
                    <div className="flex items-bottom justify-between"></div>
                    <p className=" mt-1 text-sm">I'll be back</p>
                  </div>
                </div>
                <div className="bg-white px-3 flex items-center hover:bg-gray-200 cursor-pointer">
                  <div className="ml-4 flex-1 border-b border-gray-700 py-4">
                    <div className="flex items-bottom justify-between"></div>
                    <p className=" mt-1 text-sm">Hold the line!</p>
                  </div>
                </div>
              </div>
            </div>

            {/* <!-- Right --> */}
            <div className="w-2/3 border flex flex-col">
              {/* <!-- Header --> */}
              <div className="py-2 px-3 bg-white flex flex-row justify-between items-center">
                <div className="flex items-center">
                  <div className="ml-4">
                    <p className="">Test Conversation 1</p>
                  </div>
                </div>
              </div>

              {/* <!-- Messages --> */}
              <div className="flex-1 overflow-auto bg-gray-200 border-gray-400 border">
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
                            ? "rounded py-2 px-3 bg-blue-700"
                            : "rounded py-2 px-3 bg-gray-50"
                        }
                      >
                        <p className="text-sm mt-1">{message.text}</p>
                      </div>
                    </div>
                  ))}
                </div>
              </div>

              {/* <!-- Input --> */}
              <div className="bg-gray-300 px-4 py-4 flex items-center">
                <div className="flex-1 mx-4">
                  <input
                    className="w-full border rounded px-2 py-2"
                    type="text"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                  />
                </div>
                <button onClick={sendMessage}>
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 24 24"
                    width="24"
                    height="24"
                  >
                    <path
                      fill="#263238"
                      fill-opacity=".45"
                      d="M11.999 14.942c2.001 0 3.531-1.53 3.531-3.531V4.35c0-2.001-1.53-3.531-3.531-3.531S8.469 2.35 8.469 4.35v7.061c0 2.001 1.53 3.531 3.53 3.531zm6.238-3.53c0 3.531-2.942 6.002-6.237 6.002s-6.237-2.471-6.237-6.002H3.761c0 4.001 3.178 7.297 7.061 7.885v3.884h2.354v-3.884c3.884-.588 7.061-3.884 7.061-7.885h-2z"
                    ></path>
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
