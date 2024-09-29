import React from 'react'
import ReactDOM from 'react-dom/client'
import { createBrowserRouter,RouterProvider } from 'react-router-dom'

//componentes
import App from './App.jsx'
import Welcome from './welcome.jsx'


const jeff= createBrowserRouter([
  {
    path:"/",
    element:<App/>
  },
  {
    path:"welcome",
    element:<Welcome/>
  }

])
ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={jeff}/>
  </React.StrictMode>,
)
