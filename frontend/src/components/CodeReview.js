import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";

function CodeReview() {
  const [code, setCode] = useState("");
  const [language, setLanguage] = useState("python");
  const [result, setResult] = useState(null);
  const [user, setUser] = useState("");

  const navigate = useNavigate();

  // 🔐 check login + get user
  useEffect(() => {
    const token = localStorage.getItem("token");
    if (!token) {
      navigate("/login");
    } else {
      const payload = JSON.parse(atob(token.split(".")[1]));
      setUser(payload.sub);
    }
  }, []);

  // 🔄 RESET (frontend only)
  const handleReset = () => {
    setCode("");
    setResult(null);
  };

  // // 🚀 REVIEW
  // const handleSubmit = async () => {
  //   const token = localStorage.getItem("token");

  //   if (!code) {
  //     alert("Code daal pehle 😑");
  //     return;
  //   }

  //   try {
  //     const res = await fetch("http://127.0.0.1:8000/review-code", {
  //       method: "POST",
  //       headers: {
  //         "Content-Type": "application/json",
  //         Authorization: `Bearer ${token}`,
  //       },
  //       body: JSON.stringify({ code, language }),
  //     });

  //     const data = await res.json();
  //     setResult(data);
  //   } catch (err) {
  //     alert("Error aa gaya ❌");
  //   }
  // };

  // 🚀 REVIEW
  const handleSubmit = async () => {
    const token = localStorage.getItem("token");

    if (!code) {
      alert("Code daal pehle 😑");
      return;
    }

    try {
      // 🔥 DEBUG (check kya ja raha backend ko)
      const formattedCode = code.replace(/\r\n/g, "\n");

      const payload = {
        code: formattedCode,
        language: language.toLowerCase(), // 🔥 IMPORTANT
      };

      console.log("SENDING TO BACKEND:", payload); // 👈 CHECK THIS

      const res = await fetch("http://127.0.0.1:8000/review-code", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify(payload), // 🔥 FIXED
      });

      const data = await res.json();

      console.log("RESPONSE FROM BACKEND:", data); // 👈 CHECK THIS

      setResult(data);
    } catch (err) {
      console.error(err);
      alert("Error aa gaya ❌");
    }
  };

  // 🚪 LOGOUT
  const handleLogout = () => {
    localStorage.removeItem("token");
    navigate("/");
  };

  return (
    <div className="min-h-screen bg-gray-900 text-white p-6">
      {/* 🔝 TOP BAR */}
      <div className="flex justify-between mb-4">
        <h1 className="text-2xl font-bold">🚀 AI Code Reviewer</h1>

        <div className="flex gap-4 items-center">
          <span className="text-sm">👤 {user}</span>
          <button
            onClick={handleLogout}
            className="bg-red-500 px-3 py-1 rounded"
          >
            Logout
          </button>
        </div>
      </div>

      {/* MAIN CARD */}
      <div className="max-w-4xl mx-auto bg-gray-800 p-6 rounded-2xl shadow-lg">
        <textarea
          value={code}
          onChange={(e) => setCode(e.target.value)}
          className="w-full h-64 p-4 rounded-lg text-black"
          placeholder="Paste your code here..."
        />

        {/* BUTTONS */}
        <div className="flex justify-between mt-4">
          <select
            value={language}
            onChange={(e) => setLanguage(e.target.value)}
            className="p-2 rounded text-black"
          >
            <option value="python">Python</option>
            <option value="java">Java</option>
            <option value="cpp">C++</option>
          </select>

          <div className="flex gap-4">
            <button
              onClick={handleSubmit}
              className="bg-green-500 px-6 py-2 rounded-lg"
            >
              Review Code
            </button>

            <button
              onClick={handleReset}
              className="bg-red-500 px-6 py-2 rounded-lg"
            >
              Reset
            </button>
            <button
              onClick={() => navigate("/history")}
              className="bg-blue-500 px-4 py-2 rounded"
            >
              History
            </button>
          </div>
        </div>
      </div>

      {/* RESULT */}
      {result && (
        <div className="max-w-4xl mx-auto mt-6 bg-gray-800 p-6 rounded-2xl">
          <h2 className="text-xl font-bold mb-2">Review</h2>
          <p>{result.review}</p>

          <h3 className="mt-4 font-semibold">Patterns:</h3>
          <p>
            {result.detected_patterns?.length
              ? result.detected_patterns.join(", ")
              : "None"}
          </p>

          <h3 className="mt-4 font-semibold">Mistakes:</h3>
          <ul className="list-disc ml-6">
            {(result.mistakes || []).map((m, i) => (
              <li key={i}>{m}</li>
            ))}
          </ul>

          <h3 className="mt-4 font-semibold">Time Complexity:</h3>
          <p>{result.time_complexity || "Not detected"}</p>

          <h3 className="mt-4 font-semibold">Space Complexity:</h3>
          <p>{result.space_complexity || "Not detected"}</p>

          <h3 className="mt-4 font-semibold">Optimizations:</h3>
          <ul className="list-disc ml-6">
            {(result.optimizations || []).map((o, i) => (
              <li key={i}>{o}</li>
            ))}
          </ul>

          <h3 className="mt-4 font-semibold">DSA Suggestions:</h3>
          <ul className="list-disc ml-6">
            {(result.dsa_suggestion || []).map((d, i) => (
              <li key={i}>{d}</li>
            ))}
          </ul>

          <h3 className="mt-4 font-semibold">Interview Questions:</h3>
          <ul className="list-disc ml-6">
            {(result.interview_questions || []).map((q, i) => (
              <li key={i}>{q}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default CodeReview;
