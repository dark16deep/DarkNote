async function loadFiles(section, containerId, limit = null) {
  try {
    const res = await fetch("files.json");
    const data = await res.json();

    const container = document.getElementById(containerId);
    container.innerHTML = "";

    const files = data[section];
    if (!files || files.length === 0) {
      container.innerHTML = "<p>Tidak ada file!</p>";
      return;
    }

    files.slice(0, limit || files.length).forEach(file => {
      const div = document.createElement("div");
      div.className = "download-item";
      div.innerHTML = `
        <span>${file.name}</span>
        <a href="${file.path}" download="${file.name}">Download</a>
      `;
      container.appendChild(div);
    });
  } catch (err) {
    console.error("Gagal load files:", err);
  }
}