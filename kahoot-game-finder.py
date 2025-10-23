const terminal = document.getElementById("terminal");
let stopScanner = false;

// Ctrl+C stops the scanner
document.addEventListener("keydown", (e) => {
    if (e.ctrlKey && e.key.toLowerCase() === "c") {
        stopScanner = true;
        terminal.innerHTML += "\nStopped by user.";
        if (evtSource) evtSource.close();
    }
});

function printToTerminal(text, isPin=false) {
    if (isPin) {
        terminal.innerHTML += "\n==============================\n";
        terminal.innerHTML += `<span class="pin">🎯 ${text}</span>\n`;
        terminal.innerHTML += "==============================\n";
    } else {
        terminal.innerHTML += text + "\n";
    }
    terminal.scrollTop = terminal.scrollHeight;
}

// Connect to Render backend using EventSource
const evtSource = new EventSource("https://raskattack-github-io.onrender.com/scan"); // REPLACE with your Render URL

evtSource.onmessage = function(event) {
    if (stopScanner) return;
    const msg = event.data;
    if (msg.startsWith("ACTIVE")) {
        printToTerminal(msg.split(" ")[1], true);
    } else {
        printToTerminal(msg);
    }
};

evtSource.onerror = function() {
    printToTerminal("Connection lost. Refresh page to reconnect.");
};

</html>
