import React, { useState } from "react";
import { NavLink } from "react-router-dom";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
// import { faCoffee } from "@fortawesome/free-solid-svg-icons";
import { faMoon, faSun } from "@fortawesome/free-regular-svg-icons";

export default function SideBar1() {
  const [open, setOpen] = useState(true);
  const [theme, setTheme] = useState("dark"); // ["light", "dark"
  const [activeMenu, setActiveMenu] = useState("");

  const Menus = [
    { title: "Dashboard", src: "Chart_fill", path: "/" },
    // { title: "Inbox", src: "Chat", path: "/progress" },
    { title: "Accounts", src: "User", gap: true, path: "/accounts" },
    { title: "Progress", src: "Calendar", path: "/progress" },
    // { title: "Search", src: "Search", path: "/search" },
    { title: "Analytics", src: "Chart", path: "/analytics" },
    { title: "Files", src: "Folder", gap: true, path: "/files" },
    { title: "Settings", src: "Setting", path: "/settings" },
  ];

  const handleMenuClick = (menu) => {
    setActiveMenu(menu);
  };

  const toggleTheme = () => {
    if (theme === "dark") {
      setTheme("light");
      document.documentElement.classList.remove("dark");
    } else {
      setTheme("dark");
      document.documentElement.classList.add("dark");
    }
  };

  return (
    <>
      <aside className="flex">
        <div
          className={` ${
            open ? "w-60" : "w-20 "
            //   } bg-gray-50 dark:bg-gray-800 h-screen p-5  pt-8 relative duration-300`}
          } bg-gray-800 h-screen p-5  pt-8 relative duration-300`}
        >
          <img
            src="./src/assets/control.png"
            className={`absolute cursor-pointer -right-3 top-9 w-7 border-dark-purple
       border-2 rounded-full  ${!open && "rotate-180"}`}
            onClick={() => setOpen(!open)}
          />
          <div className="flex gap-x-4 items-center">
            {/* <img
              src="./src/assets/logo.png"
              className={`cursor-pointer duration-500 ${
                open && "rotate-[360deg]"
              }`}
            /> */}
            <button
              className="border-5 border-blue-500 bg-blue-500 inline-block p-2 rounded-full"
              onClick={toggleTheme}
            >
              <FontAwesomeIcon
                icon={theme == "dark" ? faMoon : faSun}
                className={`cursor-pointer duration-500 ${
                  open && "rotate-[360deg]"
                }`}
              />
            </button>
            <h1
              className={`text-white origin-left font-medium text-sm duration-200 ${
                !open && "scale-0"
              }`}
            >
              Scrape-to-Notion
            </h1>
          </div>
          <ul className="pt-6">
            {Menus.map((Menu, index) => (
              <NavLink to={Menu.path} key={index}>
                <li
                  className={`flex  rounded-md p-2 cursor-pointer hover:bg-gray-600 dark:hover:bg-gray-700" text-gray-300 text-sm items-center gap-x-4 
          ${Menu.gap ? "mt-9" : "mt-2"} ${
                    activeMenu === Menu.title && "bg-gray-600"
                  } `}
                  onClick={() => handleMenuClick(Menu.title)}
                >
                  <img src={`./src/assets/${Menu.src}.png`} />
                  <span
                    className={`${!open && "hidden"} origin-left duration-200`}
                  >
                    {Menu.title}
                  </span>
                </li>
              </NavLink>
            ))}
          </ul>
        </div>
        {/* <div className="h-screen flex-1 p-7">
          <h1 className="text-2xl font-semibold ">Home Page</h1>
        </div> */}
      </aside>
    </>
  );
}
