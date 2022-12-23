function update() {
    const word = words[Math.floor(Math.random() * words.length)];
    document.getElementById("text").innerText = word;
}

window.onload = () => {
    update();
    document.getElementById("page").onclick = update;
}