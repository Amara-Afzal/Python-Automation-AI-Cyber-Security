const express = require("express");
const router = express.Router();
const { execFile } = require("child_process");
const fs = require("fs");
const path = require("path");

// Secure command execution
router.get("/run", (req, res) => {
    execFile("node", ["-v"], (error, stdout) => {
        if (error) return res.status(500).send("Command error");
        res.send(stdout);
    });
});

// Secure file reading with path validation
router.get("/file", (req, res) => {
    const baseDir = path.join(__dirname, "files");
    const safeFile = "data.txt";
    const safePath = path.join(baseDir, safeFile);

    fs.readFile(safePath, "utf8", (err, data) => {
        if (err) return res.status(500).send("File read error");
        res.send(data);
    });
});

// Safe input validation instead of dynamic regex
router.get("/search", (req, res) => {
    const input = req.query.q;
    const safePattern = /^[a-zA-Z0-9 ]+$/;

    if (!safePattern.test(input)) return res.status(400).send("Invalid input");
    res.send("Search query accepted: " + input);
});

module.exports = router;