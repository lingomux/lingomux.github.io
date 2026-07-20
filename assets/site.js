const tabs = Array.from(document.querySelectorAll("[data-command-tab]"));
const panels = Array.from(document.querySelectorAll("[data-command-panel]"));

function selectTab(selected) {
  const name = selected.dataset.commandTab;
  for (const tab of tabs) {
    const active = tab === selected;
    tab.setAttribute("aria-selected", String(active));
    tab.tabIndex = active ? 0 : -1;
  }
  for (const panel of panels) {
    const active = panel.dataset.commandPanel === name;
    panel.hidden = !active;
    panel.classList.toggle("is-active", active);
  }
}

for (const [index, tab] of tabs.entries()) {
  tab.addEventListener("click", () => selectTab(tab));
  tab.addEventListener("keydown", (event) => {
    if (!['ArrowLeft', 'ArrowRight'].includes(event.key)) return;
    event.preventDefault();
    const direction = event.key === 'ArrowRight' ? 1 : -1;
    const next = tabs[(index + direction + tabs.length) % tabs.length];
    selectTab(next);
    next.focus();
  });
}

if (tabs.length > 0) selectTab(tabs[0]);

for (const button of document.querySelectorAll("[data-copy-target]")) {
  button.addEventListener("click", async () => {
    const target = document.getElementById(button.dataset.copyTarget);
    if (!target) return;
    try {
      await navigator.clipboard.writeText(target.innerText);
      const previous = button.textContent;
      button.textContent = "Copied";
      window.setTimeout(() => {
        button.textContent = previous;
      }, 1600);
    } catch {
      button.textContent = "Select text";
    }
  });
}
