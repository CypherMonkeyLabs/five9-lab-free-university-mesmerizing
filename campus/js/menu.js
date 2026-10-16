const ICONS = {
  diagrams: '<rect x="3" y="3" width="7" height="7" rx="1.5"></rect><rect x="14" y="3" width="7" height="7" rx="1.5"></rect><rect x="3" y="14" width="7" height="7" rx="1.5"></rect><rect x="14" y="14" width="7" height="7" rx="1.5"></rect>',
  flows: '<path d="M4 12h12"></path><path d="M13 7l5 5-5 5"></path>',
  charts: '<path d="M4 19V5"></path><path d="M4 19h16"></path><path d="M8 16v-5"></path><path d="M12 16V8"></path><path d="M16 16v-3"></path>',
  cheats: '<path d="M7 3h8l4 4v14H7z"></path><path d="M15 3v4h4"></path>',
  play: '<path d="M8 5l12 7-12 7z"></path>',
  ecosystem: '<circle cx="6" cy="12" r="2.2"></circle><circle cx="18" cy="7" r="2.2"></circle><circle cx="18" cy="17" r="2.2"></circle><path d="M8 11.2l8-3.4"></path><path d="M8 12.8l8 3.4"></path>',
  downloads: '<path d="M12 4v10"></path><path d="M8 10l4 4 4-4"></path><path d="M5 19h14"></path>',
  careers: '<circle cx="12" cy="8" r="3"></circle><path d="M6 19c1.2-3 3.4-4.5 6-4.5S16.8 16 18 19"></path>',
  home: '<path d="M4 11L12 4l8 7v8H4z"></path><path d="M10 19v-5h4v5"></path>',
  learn: '<path d="M4 7l8-3 8 3-8 3z"></path><path d="M6 10v5c2 2 10 2 12 0v-5"></path>',
  tools: '<path d="M14 6a4 4 0 0 0-5.2 5.2L4 16l4 4 4.8-4.8A4 4 0 0 0 18 10l-3 3-2-2z"></path>',
  topology: '<path d="M12 3l8 4.5v9L12 21l-8-4.5v-9z"></path><path d="M12 12l8-4.5"></path><path d="M12 12v9"></path><path d="M12 12L4 7.5"></path>',
  ivr: '<path d="M8 4h3l1 3-2 1a9 9 0 0 0 4 4l1-2 3 1v3a2 2 0 0 1-2 2A13 13 0 0 1 6 6a2 2 0 0 1 2-2z"></path>',
  pacing: '<circle cx="12" cy="13" r="7"></circle><path d="M12 13l3-4"></path><path d="M12 6V4"></path>',
  certs: '<circle cx="12" cy="9" r="4"></circle><path d="M9 12.5L8 20l4-2 4 2-1-7.5"></path>',
  boss: '<path d="M12 4l8 14H4z"></path><path d="M12 10v4"></path><path d="M12 16.5h.01"></path>',
  interview: '<path d="M5 5h14v9H8l-3 3z"></path>',
  progress: '<path d="M5 12l4 4L19 6"></path>',
  regions: '<circle cx="12" cy="12" r="8"></circle><path d="M4 12h16"></path><path d="M12 4c2.2 2.4 2.2 13.6 0 16"></path><path d="M12 4c-2.2 2.4-2.2 13.6 0 16"></path>',
  badges: '<path d="M12 3l2.2 4.6 5 .7-3.6 3.5.9 5L12 14.8 7.5 16.8l.9-5L4.8 8.3l5-.7z"></path>',
  menu: '<path d="M5 7h14"></path><path d="M5 12h14"></path><path d="M5 17h14"></path>',
  listen: '<path d="M4 10v4h3l4 3V7L7 10z"></path><path d="M16 9a4 4 0 0 1 0 6"></path>',
  search: '<circle cx="11" cy="11" r="6"></circle><path d="M15.5 15.5L20 20"></path>',
  acd: '<path d="M8 4h3l1 3-2 1a9 9 0 0 0 4 4l1-2 3 1v3a2 2 0 0 1-2 2A13 13 0 0 1 6 6a2 2 0 0 1 2-2z"></path>',
  wfm: '<rect x="4" y="5" width="16" height="15" rx="2"></rect><path d="M8 3v4"></path><path d="M16 3v4"></path><path d="M4 10h16"></path>',
  quality: '<path d="M4 10v4h3l4 3V7L7 10z"></path><path d="M16 9a4 4 0 0 1 0 6"></path>',
  crm: '<path d="M8 8h4v4H8z"></path><path d="M14 12h4v4h-4z"></path><path d="M12 10h2"></path>'
};

export function paintMenuIcons(root) {
  (root || document).querySelectorAll("[data-icon]").forEach((node) => {
    const shape = ICONS[node.dataset.icon];
    if (!shape || node.dataset.painted === "1") return;
    node.dataset.painted = "1";
    node.innerHTML = `<svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true">${shape}</svg>`;
  });
}
