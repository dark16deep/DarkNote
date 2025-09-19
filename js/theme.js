document.addEventListener('DOMContentLoaded', () => {
  const container = document.getElementById('theme-buttons-container');

  const themes = {
    default: 'linear-gradient(135deg, #00f2fe, #4facfe)',
    pink: 'linear-gradient(135deg, #ff9a9e, #fad0c4)',
    green: 'linear-gradient(135deg, #a8ff78, #78ffd6)',
    orange: 'linear-gradient(135deg, #f6d365, #fda085)',
    red: 'linear-gradient(135deg, #ff6a6a, #ff0000)',

    // 🎨 Tema baru
    pinkpurpleblue: 'linear-gradient(135deg, #ff9a9e, #a18cd1, #4facfe)',
    neon: 'linear-gradient(135deg, #faff00, #adff2f)',
    sunset: 'linear-gradient(135deg, #ff512f, #f09819, #ffe259)'
  };

  // Buat tombol bulat kecil
  for (const key in themes) {
    const btn = document.createElement('button');
    btn.className = 'theme-btn';
    btn.dataset.theme = key;
    btn.title = key;
    btn.style.background = themes[key];
    container.appendChild(btn);
  }

  function setTheme(name) {
    const htmlEl = document.documentElement;
    htmlEl.className = htmlEl.className
      .split(' ')
      .filter(c => !c.startsWith('theme-'))
      .join(' ');
    htmlEl.classList.add('theme-' + name);
    localStorage.setItem('theme', name);
  }

  container.querySelectorAll('.theme-btn').forEach(btn => {
    btn.addEventListener('click', () => setTheme(btn.dataset.theme));
  });

  setTheme(localStorage.getItem('theme') || 'default');
});