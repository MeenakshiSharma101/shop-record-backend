require("dotenv").config();
const express = require("express");
const mongoose = require("mongoose");

const app = express();

// Middleware
app.use(express.json());

// MongoDB Connection
mongoose.connect(process.env.MONGO_URI, {
})
.then(() => console.log("MongoDB Connected ✅"))
.catch(err => console.log("Mongo Error:", err));

// Routes
const shopRoutes = require("./routes/shopRoutes");
app.use("/api/shop", shopRoutes);

// Test Route
app.get("/", (req, res) => {
  res.send("Backend working");
});

// Start Server
app.listen(5000, () => {
  console.log("Server running on port 5000");
});
