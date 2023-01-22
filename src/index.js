import React from 'react';
import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import App from './App';
import AppPage2 from './AppPage2';
import AppPage3 from './AppPage3';
import AppPage4 from './AppPage4';

export default function MyRotes() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<App />} />
        <Route path="/page2" element={<AppPage2 />} />
        <Route path="/page3" element={<AppPage3 />} />
        <Route path="/page4" element={<AppPage4 />} />
      </Routes>
    </BrowserRouter>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<MyRotes />);