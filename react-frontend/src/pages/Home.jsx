import reactLogo from "../assets/react.svg";
import viteLogo from "../assets/vite.svg";
import { faker } from "@faker-js/faker";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faBarChart, faCalendar } from "@fortawesome/free-regular-svg-icons";

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
    maintainAspectRatio: false,
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

  return (
    <>
      <div className="flex flex-col min-h-screen py-2 p-6">
        {/* <Test /> */}
        <div className="flex flex-row built-with justify-center items-baseline mb-10 mt-2">
          Built with
          <img
            src={reactLogo}
            className="h-full pointer-events-none App-logo"
            alt="logo"
          />
          +
          <img
            src={viteLogo}
            className="h-full pointer-events-none App-logo"
            alt="logo"
          />
        </div>
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 md:grid-cols-4 md:gap-6 xl:grid-cols-4 2xl:gap-7.5">
          <Home_Card
            percentage={"5%"}
            title={"Jobs Scraped"}
            amount={50}
            icon={faBarChart}
          />
          <Home_Card
            percentage={"5%"}
            title={"Jobs Scraped"}
            amount={50}
            icon={faBarChart}
          />
          <Home_Card
            percentage={"5%"}
            title={"Jobs Scraped"}
            amount={50}
            icon={faBarChart}
          />
          <Home_Card
            percentage={"5%"}
            title={"Jobs Scraped"}
            amount={50}
            icon={faCalendar}
          />
        </div>
        <div className="data-containers flex flex-row justify-between items-center mx-10 my-5">
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
        </div>
      </div>
    </>
  );
}
