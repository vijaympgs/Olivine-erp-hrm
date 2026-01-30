import React from "react";
import ReactDOM from "react-dom/client";
import { RouterProvider } from "react-router-dom";
import { router } from "./app/router";
import { AppProviders } from "./app/providers";
import "./index.css";
import "./styles/layout.css";
import { layoutManager } from "./config/layoutConfig";

// Initialize layout configuration
layoutManager.applyConfig();

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
  <React.StrictMode>
    <AppProviders>
      <RouterProvider router={router} />
    </AppProviders>
  </React.StrictMode>
);

