import { useState } from "react";
import reactLogo from "./assets/react.svg";
// import viteLogo from "/vite.svg";

import SideBar1 from "./components/side_bar";
import { Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Progress from "./pages/Progress";
import Analytics from "./pages/Analytics";
import Modal from "./components/Modal";

function App() {
  const [count, setCount] = useState(0);

  return (
    <>
      {/* <SideNav /> */}
      {/* <SideBar /> */}
      <div className="flex">
        <SideBar1 />
        {/* <Home /> */}
        <div className="w-full dark:bg-[#121212] dark:text-white dark:text-opacity-[0.87]">
          {/* <Modal /> */}

          <Routes>
            <Route path="/Scrap_to_Notion" element={<Home />} />
            <Route path="/" element={<Home />} />
            <Route path="/progress" element={<Progress />} />
            <Route path="/analytics" element={<Analytics />} />
            <Route
              path="*"
              element={
                <h1 className="flex justify-center h-screen">
                  Not Found/Not implemented
                </h1>
              }
            />
            <Route path="/settings" element={<Analytics />} />
          </Routes>
        </div>
      </div>
    </>
  );
}

export default App;
