import reactLogo from "../assets/react.svg";
import viteLogo from "../assets/vite.svg";
import { faker } from "@faker-js/faker";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faBarChart, faCalendar } from "@fortawesome/free-regular-svg-icons";
import { useEffect, useRef } from "react";
import Modal from "../components/Modal";

import React from "react";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  LineElement,
  PointElement,
  BarElement,
  Title,
  Tooltip,
  Legend,
  ArcElement,
} from "chart.js";
import { Bar, Scatter, Pie, Line } from "react-chartjs-2";
import Home_Card from "../components/Home_Card";

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  PointElement,
  LineElement,
  ArcElement,
  Title,
  Tooltip,
  Legend
);

export default function Home() {
  // chart options
  const labels = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
  ];

  const options = {
    responsive: true,
    maintainAspectRatio: true,
    plugins: {
      legend: {
        position: "top",
      },
      title: {
        display: true,
        text: "Jobs Scraped/Companies",
      },
    },
  };

  const option_scatter = {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
      y: {
        beginAtZero: true,
      },
    },
  };

  const data = {
    labels,
    datasets: [
      {
        label: "Indeed",
        data: labels.map(() => faker.datatype.number({ min: 0, max: 20 })),
        backgroundColor: "rgba(255, 99, 132, 0.5)",
      },
      {
        label: "Google",
        data: labels.map(() => faker.datatype.number({ min: 0, max: 20 })),
        backgroundColor: "rgba(53, 162, 235, 0.5)",
      },
      {
        label: "Glassdoor",
        data: labels.map(() => faker.datatype.number({ min: 0, max: 20 })),
        backgroundColor: "rgba(255, 206, 86, 0.5)",
      },
    ],
  };
  //   const data_scatter = {
  //     datasets: [
  //       {
  //         label: "A dataset",
  //         data: [
  //           { x: "Monday", y: 10 },
  //           { x: "Tuesday", y: 20 },
  //           { x: "Wednesday", y: 30 },
  //           { x: "Thursday", y: 40 },
  //           { x: "Friday", y: 50 },
  //           { x: "Saturday", y: 60 },
  //           { x: "Sunday", y: 70 },
  //         ],
  //         backgroundColor: "rgba(255, 99, 132, 1)",
  //       },
  //     ],
  //   };
  const data_line = {
    labels,
    datasets: [
      {
        label: "Jobs Scraped overtime",
        data: labels.map(() => faker.datatype.number({ min: 5, max: 50 })),
        borderColor: "rgb(255, 99, 132)",
        backgroundColor: "rgba(255, 99, 132, 0.5)",
      },
      //   {
      //     label: "Dataset 2",
      //     data: labels.map(() =>
      //       faker.datatype.number({ min: -1000, max: 1000 })
      //     ),
      //     borderColor: "rgb(53, 162, 235)",
      //     backgroundColor: "rgba(53, 162, 235, 0.5)",
      //   },
    ],
  };
  const data_pie = {
    labels: ["Total Scraped", "Total Applied", "Total Not Applied"],
    datasets: [
      {
        label: "# of Votes",
        data: [22, 19, 3],
        backgroundColor: [
          "rgba(255, 99, 132, 0.2)",
          "rgba(54, 162, 235, 0.2)",
          "rgba(255, 206, 86, 0.2)",
        ],
        borderColor: [
          "rgba(255, 99, 132, 1)",
          "rgba(54, 162, 235, 1)",
          "rgba(255, 206, 86, 1)",
        ],
        borderWidth: 1,
      },
    ],
  };
  const barChartRef = useRef(null);
  const lineChartRef = useRef(null);

  let resizeTimeout;
  window.addEventListener("resize", () => {
    clearTimeout(resizeTimeout);

    // Set a new timeout to refresh the page after resizing is completed
    resizeTimeout = setTimeout(() => {
      window.location.reload();
    }, 200);
  });
  return (
    <>
      <div className="flex flex-col min-h-screen py-2 p-6 justify-end">
        {/* <Test /> */}
        <div className="flex flex-col justify-center items-center mb-10 mt-2 flex-grow rounded-sm border bg-white shadow-lg dark:bg-[#24303F]">
          <p className="flex flex-row mb-10 text-2xl">
            Built with
            <img
              src={reactLogo}
              className="h-full pointer-events-none App-logo mx-5"
              alt="logo"
            />
            +
            <img
              src={viteLogo}
              className="h-full pointer-events-none App-logo mx-5"
              alt="logo"
            />
          </p>
          <p>
            Checkout the repo at{" "}
            <span>
              <a
                href="https://github.com/lkaijie/Scrap_to_Notion"
                target="_blank"
                className="text-blue-500 "
              >
                https://github.com/lkaijie/Scrap_to_Notion
              </a>
            </span>
          </p>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 md:grid-cols-4 md:gap-6 xl:grid-cols-4 2xl:gap-7.5">
          {/* ← ↑ → ↓ ↚ ↛ ↜ ↝ ↞ ↟ */}
          <Home_Card
            percentage={"↑ 5%"}
            title={"Jobs Scraped"}
            amount={50}
            icon={faBarChart}
          />
          <Home_Card
            percentage={"↑ 10%"}
            title={"Jobs Applied"}
            amount={23}
            icon={faBarChart}
          />
          <Home_Card
            percentage={"↓ 5%"}
            title={"Responses"}
            amount={1}
            icon={faBarChart}
          />
          <Home_Card
            percentage={" "}
            title={"Longest Streak"}
            amount={10}
            icon={faCalendar}
          />
        </div>
        <Modal />

        <div className="charts-container grid gap-5 xl:grid-cols-chart-big 2xl:gap-9">
          <div className="chart-container p-10 border bg-white shadow-lg">
            <Bar options={options} data={data} id="bar" ref={barChartRef} />
          </div>
          <div className="chart-container p-10 border bg-white shadow-lg">
            <Line
              options={option_scatter}
              data={data_line}
              id="line"
              ref={lineChartRef}
            />
          </div>
          {/* <div className="chart-container p-10 border bg-white shadow-lg">
            <Pie data={data_pie} options={options} />
          </div> */}
        </div>

        {/* <div className="mt-4 grid grid-cols-12 gap-4 md:mt-6 md:gap-6 2xl:mt-7.5 2xl:gap-7.5">
          <div className="col-span-12 rounded-sm border border-stroke bg-white px-5 pt-7.5 pb-5 shadow-default dark:border-strokedark dark:bg-boxdark sm:px-7.5 xl:col-span-8">
            <Bar options={options} data={data} />
          </div>
          <div className="rounded-sm border border-stroke bg-white py-6 px-7.5 shadow-lg dark:border-strokedark dark:bg-gray-800">
            <Line options={option_scatter} data={data_line} />
          </div>
        </div> */}
        {/* <div className="data-containers flex flex-row justify-between items-center mx-10 my-5">
          <div className="chart-container bg-blue-50 border rounded-full p-10 h-96 w-96">
            <Bar options={options} data={data} />
          </div>
          <div className="chart-container bg-blue-50 border rounded-full p-5">
            {" "}
            <Line options={option_scatter} data={data_line} />
          </div>
          <div className="chart-container bg-blue-50 border rounded-full p-5">
            {" "}
            <Pie
              data={data_pie}
              options={{ responsive: true, maintainAspectRatio: false }}
              className="w-[70%] h-[70%]"
            />
          </div>
        </div> */}
      </div>
    </>
  );
}
