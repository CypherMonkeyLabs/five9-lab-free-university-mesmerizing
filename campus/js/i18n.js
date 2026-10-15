const STRINGS = {
  en: { greet: "Signal university", diagrams: "Diagrams", flows: "Flows", charts: "Charts", cheats: "Cheat Codes", play: "Play", ecosystem: "Ecosystem", downloads: "Downloads", careers: "Careers", lang: "Language", light: "Light", dark: "Dark", audio: "Architect conversation", regions: "Regions" },
  es: { greet: "Universidad de la señal", diagrams: "Diagramas", flows: "Flujos", charts: "Gráficos", cheats: "Chuletas", play: "Jugar", ecosystem: "Ecosistema", downloads: "Descargas", careers: "Carreras", lang: "Idioma", light: "Claro", dark: "Oscuro", audio: "Conversación de arquitectos", regions: "Regiones" },
  hi: { greet: "सिग्नल विश्वविद्यालय", diagrams: "आरेख", flows: "प्रवाह", charts: "चार्ट", cheats: "चीट कोड", play: "खेल", ecosystem: "पारिस्थितिकी", downloads: "डाउनलोड", careers: "करियर", lang: "भाषा", light: "हल्का", dark: "गहरा", audio: "आर्किटेक्ट बातचीत", regions: "क्षेत्र" },
  te: { greet: "సిగ్నల్ విశ్వవిద్యాలయం", diagrams: "రేఖాచిత్రాలు", flows: "ప్రవాహాలు", charts: "చార్టులు", cheats: "చీట్ కోడ్స్", play: "ఆడండి", ecosystem: "పర్యావరణం", downloads: "డౌన్‌లోడ్‌లు", careers: "వృత్తులు", lang: "భాష", light: "వెలుగు", dark: "చీకటి", audio: "ఆర్కిటెక్ట్ సంభాషణ", regions: "ప్రాంతాలు" },
  fr: { greet: "Université du signal", diagrams: "Schémas", flows: "Flux", charts: "Graphiques", cheats: "Antisèches", play: "Jouer", ecosystem: "Écosystème", downloads: "Téléchargements", careers: "Carrières", lang: "Langue", light: "Clair", dark: "Sombre", audio: "Conversation d'architectes", regions: "Régions" },
  de: { greet: "Signal-Universität", diagrams: "Diagramme", flows: "Abläufe", charts: "Schaubilder", cheats: "Spickzettel", play: "Spielen", ecosystem: "Ökosystem", downloads: "Downloads", careers: "Laufbahn", lang: "Sprache", light: "Hell", dark: "Dunkel", audio: "Architektengespräch", regions: "Regionen" },
  ja: { greet: "シグナル大学", diagrams: "図", flows: "フロー", charts: "チャート", cheats: "早見表", play: "プレイ", ecosystem: "エコシステム", downloads: "ダウンロード", careers: "キャリア", lang: "言語", light: "ライト", dark: "ダーク", audio: "アーキテクトの会話", regions: "地域" },
  ar: { greet: "جامعة الإشارة", diagrams: "مخططات", flows: "تدفقات", charts: "رسوم", cheats: "أوراق الغش", play: "العب", ecosystem: "المنظومة", downloads: "تنزيلات", careers: "مهن", lang: "اللغة", light: "فاتح", dark: "داكن", audio: "حوار المهندسين", regions: "المناطق" }
};

export function currentLang() {
  try {
    const saved = JSON.parse(localStorage.getItem("f9lab-settings") || "{}");
    if (STRINGS[saved.lang]) return saved.lang;
  } catch (err) { /* keep English */ }
  return "en";
}

export function t(key) {
  const pack = STRINGS[currentLang()] || STRINGS.en;
  return pack[key] || STRINGS.en[key] || key;
}

export function applyI18n() {
  const lang = currentLang();
  document.documentElement.lang = lang;
  document.documentElement.dir = lang === "ar" ? "rtl" : "ltr";
  document.querySelectorAll("[data-i18n]").forEach((node) => {
    const key = node.dataset.i18n;
    const value = t(key);
    if (node.tagName === "OPTION") return;
    node.textContent = value;
  });
  const select = document.querySelector("#lang-pick");
  if (select && select.value !== lang) select.value = lang;
  const mode = document.querySelector("#mode-toggle");
  if (mode) mode.textContent = document.documentElement.dataset.theme === "light" ? t("dark") : t("light");
}
