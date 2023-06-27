import React, { useState } from "react";

function Modal() {
  const [showModal, setShowModal] = useState(true);

  const handleClose = () => {
    setShowModal(false);
  };

  if (!showModal) {
    return null; // Render nothing if the modal is hidden
  }

  return (
    <div className="fixed inset-0 flex items-center justify-center z-50">
      <div className="bg-white rounded-lg p-8 shadow-lg absolute">
        <div className="flex justify-between items-center mb-6">
          <h3 className="text-xl font-bold">Important Note</h3>
          <button
            className="text-gray-500 hover:text-gray-700"
            onClick={handleClose}
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              className="h-6 w-6"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M6 18L18 6M6 6l12 12"
              />
            </svg>
          </button>
        </div>
        <div className="mb-6 flex flex-col">
          <p>
            Because this is hosted on a static site, data shown here is instead
          </p>
          <p> randomly generated instead of pulled from the Django backend</p>
        </div>
        <div className="text-right">
          <button
            className="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600"
            onClick={handleClose}
          >
            Close
          </button>
        </div>
      </div>
    </div>
  );
}

export default Modal;
