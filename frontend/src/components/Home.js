import { useNavigate } from "react-router-dom";
import { ReactTyped } from "react-typed";
import Navbar from "./Navbar";

function Home() {
  const navigate = useNavigate();

  return (
    <div className="bg-gradient-to-r from-black via-gray-900 to-black text-white min-h-screen">
      <Navbar />

      <div className="flex items-center justify-center h-[90vh]">
        <div className="text-center max-w-3xl">
          <h1 className="text-5xl font-bold mb-4">🚀 AI Code Reviewer</h1>

          <ReactTyped
            strings={[
              "Review your code instantly ⚡",
              "Improve your logic 🧠",
              "Crack coding interviews 💼",
            ]}
            typeSpeed={50}
            backSpeed={30}
            loop
            className="text-xl text-indigo-400"
          />

          <p className="text-gray-400 mt-6 mb-6">
            Smart AI-powered feedback for developers. Fix mistakes, optimize
            code, and level up your DSA 🚀
          </p>

          <div className="space-x-4">
            <button
              onClick={() => navigate("/login")}
              className="bg-indigo-600 px-6 py-2 rounded-lg hover:bg-indigo-700 transition transform hover:scale-105"
            >
              Login
            </button>

            <button
              onClick={() => navigate("/signup")}
              className="bg-green-500 px-6 py-2 rounded-lg hover:bg-green-600 transition transform hover:scale-105"
            >
              Signup
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Home;
