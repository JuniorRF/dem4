document.addEventListener("DOMContentLoaded", function () {
  const lines = document.querySelectorAll(".line");
  let currentLineIndex = 0;

  function typeNextLine() {
    if (currentLineIndex >= lines.length) return;

    const line = lines[currentLineIndex];
    const text = line.textContent;
    line.textContent = ''; // очищаем
    let i = 0;

    const typingInterval = setInterval(() => {
      if (i < text.length) {
        line.textContent += text.charAt(i);
        i++;
      } else {
        clearInterval(typingInterval);
        // Пауза перед следующей строкой (например, 300 мс)
        setTimeout(() => {
          currentLineIndex++;
          typeNextLine();
        }, 300);
      }
    }, 30); // Скорость печати: 30 мс на символ
  }

  // Начинаем с первой строки
  typeNextLine();
});