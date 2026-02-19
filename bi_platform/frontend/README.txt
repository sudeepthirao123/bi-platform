
React Frontend (Quick Setup)

1. Install Node.js
2. Run:
   npx create-react-app dashboard
   cd dashboard
   npm install axios chart.js react-chartjs-2

3. Replace src/App.js with:

import { useEffect, useState } from "react";
import axios from "axios";
import { Bar } from "react-chartjs-2";

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/sales/")
      .then(res => setData(res.data));
  }, []);

  const chartData = {
    labels: data.map(d => d.product__name),
    datasets: [{ label: "Sales", data: data.map(d => d.total_sales) }]
  };

  return <Bar data={chartData} />;
}

export default App;
