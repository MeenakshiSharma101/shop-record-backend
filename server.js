const express = require("express");
const dotenv = require("dotenv");
const connectDB = require("./config/db");

dotenv.config();
connectDB();

const app = express();
app.use(express.json());

const shopRoutes = require("./routes/shopRoutes");
app.use("/api/shop", shopRoutes);

app.get("/", (req, res) => {
  res.send("Backend working");
});

app.listen(5000, () => {
  console.log("Server running on port 5000");
});
