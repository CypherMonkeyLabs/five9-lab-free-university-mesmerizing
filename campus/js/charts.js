// Charts from the lab catalog and the cited port and bandwidth tables.
// d3 is the classic UMD build on window.d3. Scales fall back to arithmetic
// if that script has not run yet.

function esc(value) {
  return String(value).replace(/[&<>"]/g, (ch) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[ch]));
}

function kbps(text) {
  const match = String(text).match(/(\d+)/);
  return match ? Number(match[1]) : 0;
}

function widthScale(values, maxPx) {
  const max = Math.max(...values, 1);
  const d3 = globalThis.d3;
  if (d3 && typeof d3.scaleLinear === "function") {
    const scale = d3.scaleLinear().domain([0, max]).range([4, maxPx]);
    return (value) => scale(value);
  }
  return (value) => 4 + (value / max) * (maxPx - 4);
}

function shorten(text, max) {
  const value = String(text);
  return value.length > max ? `${value.slice(0, max - 1)}…` : value;
}

function hbars(title, rows) {
  const width = 560;
  const labelW = 150;
  const rowH = 22;
  const height = 16 + rows.length * rowH;
  const scale = widthScale(rows.map((row) => row.value), width - labelW - 56);
  const body = rows.map((row, index) => {
    const y = 8 + index * rowH;
    const bar = Math.round(scale(row.value));
    return `<text x="0" y="${y + 13}">${esc(shorten(row.label, 22))}</text><rect class="bar" x="${labelW}" y="${y}" width="${bar}" height="14" rx="3"></rect><text x="${labelW + bar + 6}" y="${y + 13}">${esc(row.value)}</text>`;
  }).join("");
  return `<svg class="chart" viewBox="0 0 ${width} ${height}" role="img" aria-label="${esc(title)}">${body}</svg>`;
}

function vbars(title, rows) {
  const slot = 28;
  const width = Math.max(320, rows.length * slot + 16);
  const height = 168;
  const scale = widthScale(rows.map((row) => row.value), 112);
  const body = rows.map((row, index) => {
    const bar = Math.round(scale(row.value));
    const x = 12 + index * slot;
    const y = 124 - bar;
    return `<rect class="bar" x="${x}" y="${y}" width="18" height="${bar}" rx="3"></rect><text x="${x + 9}" y="140" text-anchor="middle">${esc(row.label)}</text>`;
  }).join("");
  return `<svg class="chart" viewBox="0 0 ${width} ${height}" role="img" aria-label="${esc(title)}">${body}</svg>`;
}

function tally(items, key) {
  const counts = new Map();
  items.forEach((item) => {
    const name = item[key] || "Other";
    counts.set(name, (counts.get(name) || 0) + (item.lessons ? item.lessons.length : 1));
  });
  return [...counts.entries()].map(([label, value]) => ({ label, value }));
}

export const chartIds = ["groups", "levels", "bandwidth", "protocols", "catalog", "tracks"];

export function chartList(catalog, uni) {
  const tracks = catalog.tracks || [];
  const groups = tally(tracks, "group");
  const levels = tally(tracks, "level");
  const bandwidth = (uni.bandwidth || []).map((row) => ({
    label: row.use,
    value: kbps(row.rec || row.min)
  }));
  const protocols = new Map();
  (uni.ports || []).forEach((row) => {
    const name = row.proto || "Other";
    protocols.set(name, (protocols.get(name) || 0) + 1);
  });
  const counts = catalog.counts || {};
  const catalogRows = [
    { label: "Lessons", value: counts.lessons || 0 },
    { label: "Quiz", value: counts.quiz || 0 },
    { label: "Cards", value: counts.cards || 0 },
    { label: "Cites", value: counts.cites || 0 }
  ];
  const perTrack = tracks.map((track) => ({ label: track.id, value: track.lessons.length }));
  return [
    { id: "groups", title: "Lessons by catalog group", note: "Counted from campus/data/catalog.json.", svg: hbars("Lessons by catalog group", groups) },
    { id: "levels", title: "Lessons by level", note: "Foundation, practice, and later levels in the same catalog.", svg: hbars("Lessons by level", levels) },
    { id: "bandwidth", title: "Cited bandwidth, kbps", note: "Recommended figures parsed from the technical-requirements table. Video uses the first number in that cell.", svg: hbars("Cited bandwidth in kbps", bandwidth) },
    { id: "protocols", title: "Port rows by protocol", note: "One bar per row in the lab port table, including the two TCP 443 rows.", svg: hbars("Port rows by protocol", [...protocols.entries()].map(([label, value]) => ({ label, value }))) },
    { id: "catalog", title: "Catalog counts", note: "Lessons, quiz items, flashcards, and citations stored with the tracks.", svg: hbars("Catalog counts", catalogRows) },
    { id: "tracks", title: "Lessons in each track", note: "Eighteen tracks. The axis labels are the track ids.", svg: vbars("Lessons in each track", perTrack) }
  ];
}

export function chartStrip(catalog, uni) {
  return chartList(catalog, uni).map((chart) => `<figure class="chart-card" data-chart="${esc(chart.id)}"><figcaption>${esc(chart.title)}</figcaption>${chart.svg}<p class="note">${esc(chart.note)}</p></figure>`).join("");
}
