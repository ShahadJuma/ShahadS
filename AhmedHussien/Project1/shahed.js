function changeText() {
    const textElement = document.getElementById('text');
    const newText = prompt("Enter new text:", textElement.textContent);
    if (newText) {
        textElement.textContent = newText;
    }
}
