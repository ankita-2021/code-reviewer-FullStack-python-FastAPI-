function Navbar() {
  // ✅ LOGOUT FUNCTION (yahan likhna hai)
  const handleLogout = () => {
    localStorage.removeItem("token");
    window.location.href = "/login";
  };

  return (
    <div className="bg-black text-white p-4 flex justify-between items-center">
      <h1 className="font-bold text-lg">🚀 AI Reviewer</h1>

      <div className="space-x-4 text-sm flex items-center">
        <a href="https://leetcode.com" target="_blank">
          LeetCode
        </a>

        <a href="https://geeksforgeeks.org" target="_blank">
          GFG
        </a>

        <a href="https://codechef.com" target="_blank">
          CodeChef
        </a>

        <a href="#">DSA Sheet</a>

        {/* 🔥 LOGOUT BUTTON */}
        <button
          onClick={handleLogout}
          className="bg-red-500 px-3 py-1 rounded hover:bg-red-600 ml-4"
        >
          Logout
        </button>
      </div>
    </div>
  );
}

export default Navbar;
