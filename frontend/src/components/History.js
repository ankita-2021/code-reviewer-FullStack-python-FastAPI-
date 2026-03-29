import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

function History() {
  const [data, setData] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem("token");

    if (!token) {
      navigate("/login");
      return;
    }

    fetch("http://127.0.0.1:8000/history", {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
      .then((res) => res.json())
      .then((res) => setData(res))
      .catch(() => alert("Error loading history"));
  }, []);

  return (
    <div className="min-h-screen bg-gray-900 text-white p-6">
      <h1 className="text-3xl font-bold mb-6 text-center">📜 Your History</h1>

      <div className="max-w-4xl mx-auto space-y-4">
        {data.length === 0 ? (
          <p>No history found 😢</p>
        ) : (
          data.map((item, index) => (
            <div key={index} className="bg-gray-800 p-4 rounded-xl shadow">
              <p>
                <b>Code:</b>
              </p>
              <pre className="bg-black p-2 rounded mt-2 overflow-x-auto">
                {item.code}
              </pre>

              <p className="mt-2">
                <b>Language:</b> {item.language}
              </p>

              <p className="mt-2">
                <b>Result:</b>
              </p>
              <pre className="bg-black p-2 rounded mt-2 overflow-x-auto">
                {item.result}
              </pre>
            </div>
          ))
        )}
      </div>
    </div>
  );
}

export default History;
