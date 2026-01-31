const express = require("express");
const router = express.Router();
const Shop = require("../models/Shop");

// ✅ Create Shop Item
router.post("/", async (req, res) => {
  try {
    const newItem = new Shop(req.body);
    const savedItem = await newItem.save();
    res.status(201).json(savedItem);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// ✅ Get All Shop Items
router.get("/", async (req, res) => {
  try {
    const items = await Shop.find().sort({ createdAt: -1 });
    res.json(items);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// ✅ Update Item
router.put("/:id", async (req, res) => {
  try {
    const updated = await Shop.findByIdAndUpdate(
      req.params.id,
      req.body,
      { new: true }
    );
    res.json(updated);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// ✅ Delete Item
router.delete("/:id", async (req, res) => {
  try {
    await Shop.findByIdAndDelete(req.params.id);
    res.json({ message: "Item deleted successfully" });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

module.exports = router;
