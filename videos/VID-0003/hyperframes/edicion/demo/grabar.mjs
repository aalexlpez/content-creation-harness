// Graba la app REAL de Plan B (staging) en formato de celular para la demo de VID-0002 v06, fotograma a fotograma.
// Uso: node grabar.mjs <carpeta_fotogramas>
// Requiere NPXNM (node_modules de `npx hyperframes@0.9.42`, que trae puppeteer-core) y CHROME (el chrome-headless-shell
// que descarga HyperFrames). No instala nada.
//
// Cómo graba: fotograma a fotograma (stop motion). Cada captura tarda ≈ 85 ms y en el vídeo vale 1/30 s, así que las
// animaciones de la app se ralentizan con CDP Animation.setPlaybackRate para que en el vídeo vayan a su velocidad real
// (la tasa se ajusta sola cada 30 fotogramas). El tiempo virtual de CDP se probó y cuelga Chrome al cambiar de paso.
// Fotogramas de 1080×2342 (iPhone 393×852 pt a 2,748×). Las acciones (toques y tecleo) están en ACCIONES, en el
// tiempo del corte (tn), para que la app haga cada cosa cuando la voz lo dice: no hace falta acelerar ni cortar.
// - La fecha se fija en enero de 2027 (el reloj sigue corriendo): la app pregunta «este año» y habla de «1 de febrero»,
//   como hará cuando se publique la serie (1 de enero de 2027). Es lo que la app hace de verdad en enero.
// - Tema claro. Sin anillos ni dedos simulados (REVIEW de la v04): solo lo que la app enseña al tocarla.
// - Nada sale del navegador: no se pulsa Google Calendar, ni descargar, ni compartir.
import { createRequire } from "module";
import fs from "fs";
import path from "path";
const require = createRequire(process.env.NPXNM + "/");
const puppeteer = require("puppeteer-core");

const salida = process.argv[2];
fs.mkdirSync(salida, { recursive: true });
const URL = "https://miminiapp-staging.miminiapp-lab.workers.dev/es/apps/plan-b/";
const FECHA = "2027-01-12T18:30:00";
const FPS = 30, T0 = 12.40, T1 = 25.40;           // tramo grabado, en tn (la demo se ve de 12,62 a 25,15)
const SIT = "llego a casa después de las 20:00", ACC = "hago 5 minutos de estiramientos";

// [tn, acción, argumento] — VID-0003 (palabras.js): «Eliges tu meta» 13,08–14,01 · «qué te hizo dejarla» 14,41–15,48 ·
// «y escribes tu plan B» 15,85–17,41 · «Si llego a casa después de las 8» 17,95–19,54 · «hago 5 minutos de
// estiramiento» 19,54–21,24 · el plan aparece en silencio con el estribillo 2 (21,37) · «calendario» 22,86 ·
// «fondo de pantalla» 23,82–24,71. Demo en tres momentos (GUION S04–S06).
const ACCIONES = [
  [13.10, "clic", "¿Necesitas una idea?"],
  [13.55, "clic", "Hacer ejercicio"],
  [14.10, "clic", "Continuar"],
  [14.95, "clic", "No tuve tiempo"],
  [15.45, "clic", "Continuar"],
  [15.95, "clic", "Escribir la mía"],
  [17.95, "teclea", [SIT, 19.30]],
  [19.42, "clic", "Continuar"],
  [19.62, "clic", "Escribir la mía"],
  [19.75, "teclea", [ACC, 20.95]],
  [21.15, "clic", "Ver mi plan"],
  [22.40, "clic", "Añadir recordatorio"],
  [22.55, "scroll", ["¿A qué hora?", 0.30, 0.45]],
  [22.90, "hora", "20:00"],
  [23.40, "scroll", ["IMG", 0.50, 0.60]],
];


// La escala se fuerza al lanzar Chrome: con setViewport(deviceScaleFactor) chrome-headless-shell captura a 393 px.
const b = await puppeteer.launch({ executablePath: process.env.CHROME, headless: true, defaultViewport: null,
  args: ["--no-sandbox", "--hide-scrollbars", `--force-device-scale-factor=${1080 / 393}`, "--window-size=393,852"] });
const p = await b.newPage();
{ const c0 = await p.createCDPSession(); await c0.send("Emulation.setTouchEmulationEnabled", { enabled: true }); }
const OFFSET = new Date(FECHA).getTime() - Date.now();
await p.evaluateOnNewDocument((off) => {
  localStorage.setItem("miminiapp.appearance", "light");
  const _D = Date;
  class D extends _D { constructor(...a) { if (!a.length) super(_D.now() + off); else super(...a); } static now() { return _D.now() + off; } }
  globalThis.Date = D;
  // La app desplaza la página con scrollIntoView suave, que no respeta la ralentización y daría saltos en el vídeo:
  // los desplazamientos los hace la grabación (acción «scroll»), siempre a la misma velocidad.
  Element.prototype.scrollIntoView = function () {};
}, OFFSET);
await p.goto(URL, { waitUntil: "networkidle0" });
await p.waitForSelector('[data-testid="plan-b-app"][data-ready="true"]');
await new Promise((r) => setTimeout(r, 1500));
// Un toque real al principio: así Chrome sabe que se usa con el dedo y no dibuja el recuadro de foco del teclado
// (focus-visible) cuando la app mueve el foco al título de cada paso. Con un dedo real tampoco se ve.
await p.touchscreen.tap(380, 840); await new Promise((r) => setTimeout(r, 300));

const cdp = await p.createCDPSession();
await cdp.send("Animation.enable");
let tasa = 0.4; await cdp.send("Animation.setPlaybackRate", { playbackRate: tasa });
let tBloque = performance.now();

// Los toques y el tecleo se hacen desde la página (click() y el setter nativo + evento «input», que es lo que React
// escucha): son instantáneos y no dependen de la velocidad de captura.
const tocar = (texto) => p.evaluate((tx) => {
  const els = [...document.querySelectorAll('[data-testid="plan-b-app"] button, [data-testid="plan-b-app"] label, [data-testid="plan-b-app"] a, [data-testid="plan-b-app"] summary')];
  const el = els.find((e) => e.innerText.trim() === tx && e.getBoundingClientRect().height > 0);
  if (!el) return false;
  el.click(); return true;
}, texto);
const escribir = (sel, valor) => p.evaluate((s, v) => {
  const el = document.querySelector(s); if (!el) return false;
  const proto = el.tagName === "TEXTAREA" ? HTMLTextAreaElement.prototype : HTMLInputElement.prototype;
  el.focus({ preventScroll: true });
  Object.getOwnPropertyDescriptor(proto, "value").set.call(el, v);
  el.dispatchEvent(new Event("input", { bubbles: true })); el.dispatchEvent(new Event("change", { bubbles: true }));
  return true;
}, sel, valor);
const TXT = '[data-testid="plan-b-app"] textarea, [data-testid="plan-b-app"] input[type="text"]';

let tecleo = null, scroll = null, log = [];
const pendientes = [...ACCIONES];
const N = Math.round((T1 - T0) * FPS);
for (let k = 0; k < N; k++) {
  const tn = T0 + k / FPS;
  while (pendientes.length && pendientes[0][0] <= tn + 1e-6) {
    const [ta, tipo, arg] = pendientes.shift();
    if (tipo === "clic") {
      if (!(await tocar(arg))) throw new Error(`No encuentro «${arg}» en tn ${ta}`);
    } else if (tipo === "teclea") {
      tecleo = { txt: arg[0], i: 0, t0: ta, t1: arg[1] };
    } else if (tipo === "hora") {
      await escribir('[data-testid="plan-b-app"] input[type="time"]', arg);
      await p.evaluate(() => document.activeElement && document.activeElement.blur());
    } else if (tipo === "scroll") {   // [destino, posición en la pantalla (0 arriba, 1 abajo), duración]
      scroll = { y0: await p.evaluate(() => window.scrollY), dest: arg[0], f: arg[1], t0: ta, d: arg[2] };
    }
    log.push([ta, tipo, Array.isArray(arg) ? arg[0] : arg]);
  }
  if (tecleo) {   // letras repartidas entre t0 y t1, a ritmo humano
    const debe = Math.min(tecleo.txt.length, Math.floor(((tn - tecleo.t0) / (tecleo.t1 - tecleo.t0)) * tecleo.txt.length) + 1);
    if (tecleo.i < debe) { tecleo.i = debe; await escribir(TXT, tecleo.txt.slice(0, debe)); }
    if (tecleo.i >= tecleo.txt.length) tecleo = null;
  }
  if (scroll) {
    const q = Math.min(1, (tn - scroll.t0) / scroll.d), e = q < 0.5 ? 4 * q * q * q : 1 - Math.pow(-2 * q + 2, 3) / 2;
    // el destino se recalcula en cada fotograma (la imagen del fondo de pantalla puede terminar de cargarse a mitad)
    await p.evaluate((sc, e) => {
      let el;
      if (sc.dest === "IMG") el = [...document.querySelectorAll('[data-testid="plan-b-app"] img')].sort((a, b) => b.getBoundingClientRect().height - a.getBoundingClientRect().height)[0];
      else el = [...document.querySelectorAll('[data-testid="plan-b-app"] *')].find((x) => x.childElementCount === 0 && x.innerText && x.innerText.trim() === sc.dest);
      const r = el.getBoundingClientRect();
      const y1 = Math.max(0, window.scrollY + r.top + r.height / 2 - innerHeight * sc.f);
      window.scrollTo(0, sc.y0 + (y1 - sc.y0) * e);
    }, scroll, e);
    if (q >= 1) scroll = null;
  }
  if (k > 0 && k % 30 === 0) {   // ajusta la tasa: 30 fotogramas deben equivaler a 1 s de animación
    const real = (performance.now() - tBloque) / 1000; tBloque = performance.now();
    tasa = Math.max(0.05, Math.min(1, 1 / real)); await cdp.send("Animation.setPlaybackRate", { playbackRate: tasa });
  }
  const shot = await cdp.send("Page.captureScreenshot", { format: "jpeg", quality: 93 });
  fs.writeFileSync(path.join(salida, `f${String(k).padStart(5, "0")}.jpg`), Buffer.from(shot.data, "base64"));
}
fs.writeFileSync(path.join(salida, "grabacion.json"), JSON.stringify({ url: URL, fecha: FECHA, fps: FPS, tn_inicio: T0, tn_fin: T1, fotogramas: N, acciones: log }, null, 1));
await b.close();
console.log(`${N} fotogramas, tn ${T0}–${T1}`);
