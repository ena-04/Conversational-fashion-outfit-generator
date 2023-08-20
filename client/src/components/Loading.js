import React from "react";
// import "../components/Loading.css";
export const Loading = () => {
  return (
    <div className="flex items-center justify-center space-x-2">
      <div className="w-2 h-2 rounded-full animate-pulse dark:bg-blue-600"></div>
      <div className="w-2 h-2 rounded-full animate-pulse dark:bg-blue-600"></div>
      <div className="w-2 h-2 rounded-full animate-pulse dark:bg-blue-600"></div>
    </div>
  );
};
