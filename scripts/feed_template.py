"""Template padrão de feed Vexter (1080x1350). Tudo centralizado, mesmo layout por série.

Uso em Python:
    from feed_template import render_series, make_grid
    files = render_series(slides, "escuro", "saida/serie_x")
    make_grid(files, "saida/serie_x/_grade.png")   # conferência obrigatória (checklist)

Uso por linha de comando:
    python feed_template.py serie.json saida/serie_x
    (serie.json = {"tema": "escuro", "handle": "@somosvexter", "slides": [...]})

slides = lista de dicts:
    {tipo: capa|texto|lista|dado|cta, kicker, titulo, corpo, itens, big, fonte}
Use <b>palavra</b> no titulo (ou no corpo) para destacar em dourado.
Requer playwright (chromium) e Pillow. Fontes Poppins e Inter vão embutidas (assets/fonts),
então o resultado é igual em qualquer máquina, sem depender de fontes instaladas.
"""
import base64, html as _html, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
FONTS = ASSETS / "fonts"

THEMES = {  # um tema por série; nunca misturar dentro de uma sequência
    "escuro":  dict(bg="radial-gradient(circle at 50% 0%,#2a2210 0%,#000 62%)", fg="#FFFFFF", mut="#cfcfcf",
                    acc="#C8A34D", acc2="#DDBE7A", card="#1B1B1B", logo="logo_transparente_fundo_escuro.png"),
    "grafite": dict(bg="radial-gradient(circle at 50% 0%,#2b2b2b 0%,#1B1B1B 65%)", fg="#FFFFFF", mut="#d0d0d0",
                    acc="#C8A34D", acc2="#DDBE7A", card="#000000", logo="logo_transparente_fundo_escuro.png"),
    "claro":   dict(bg="linear-gradient(180deg,#FFFFFF 0%,#F5F5F5 100%)", fg="#000000", mut="#444444",
                    acc="#A8832F", acc2="#C8A34D", card="#FFFFFF", logo="logo_transparente_cores_originais.png"),
}
TIPOS = {"capa", "texto", "lista", "dado", "cta"}
_DASH = re.compile("[\u2013\u2014]")  # travessões proibidos pelo padrão


def _b64(p):
    return base64.b64encode(Path(p).read_bytes()).decode()


def _fontface():
    spec = [("Poppins", 600, "Poppins-SemiBold.woff2"), ("Poppins", 700, "Poppins-Bold.woff2"),
            ("Inter", 400, "Inter-Regular.woff2"), ("Inter", 500, "Inter-Medium.woff2"),
            ("Inter", 600, "Inter-SemiBold.woff2")]
    out = ""
    for fam, w, f in spec:
        p = FONTS / f
        if p.exists():
            out += f"@font-face{{font-family:'{fam}';font-weight:{w};src:url(data:font/woff2;base64,{_b64(p)}) format('woff2')}}"
    return out


def _rich(t):
    """Escapa o texto e libera apenas <b>...</b> como destaque dourado."""
    t = _html.escape(t or "", quote=False)
    return t.replace("&lt;b&gt;", "<span class='hl'>").replace("&lt;/b&gt;", "</span>")


def validate(slides, theme):
    """Erros que quebram o padrão de feed. Retorna lista de mensagens (vazia = ok)."""
    errs = []
    if theme not in THEMES:
        errs.append(f"tema '{theme}' inexistente; use {sorted(THEMES)}")
    for i, s in enumerate(slides, 1):
        if s.get("tipo") not in TIPOS:
            errs.append(f"slide {i}: tipo '{s.get('tipo')}' inválido; use {sorted(TIPOS)}")
        if not s.get("titulo"):
            errs.append(f"slide {i}: sem titulo")
        if s.get("tipo") == "dado" and not s.get("big"):
            errs.append(f"slide {i}: tipo dado exige 'big'")
        if len(s.get("itens", [])) > 5:
            errs.append(f"slide {i}: {len(s['itens'])} itens; máximo 5 por slide (divida em dois slides)")
        txt = " ".join(str(v) for v in s.values() if isinstance(v, str)) + " ".join(s.get("itens", []))
        if _DASH.search(txt):
            errs.append(f"slide {i}: contém travessão (– ou —); reescreva sem travessão")
    return errs


def html(s, n, total, th, handle, fontcss=""):
    T = THEMES[th]; tipo = s["tipo"]
    css = f"""{fontcss}*{{box-sizing:border-box;margin:0;padding:0}}:root{{--acc:{T['acc']}}}
body{{font-family:'Inter',sans-serif}}.s{{width:1080px;height:1350px;position:relative;overflow:hidden;background:{T['bg']};color:{T['fg']};text-align:center}}
.hl{{color:var(--acc)}}
.h{{font-family:'Poppins',sans-serif;font-weight:700;letter-spacing:-1px;line-height:1.1}}
.big{{font-family:'Poppins',sans-serif;font-weight:700;color:var(--acc);white-space:nowrap;line-height:1;letter-spacing:-2px}}
.k{{font-weight:600;letter-spacing:5px;font-size:24px;color:{T['acc']};text-transform:uppercase}}
.top{{position:absolute;top:48px;left:0;right:0;display:flex;justify-content:center}}.top img{{height:150px}}
.mid{{position:absolute;left:90px;right:90px;top:240px;bottom:190px;display:flex;flex-direction:column;justify-content:center;align-items:center}}
.rule{{width:90px;height:4px;background:{T['acc']};margin:34px auto}}
.p{{font-size:36px;line-height:1.5;color:{T['mut']};max-width:860px}}
.card{{width:100%;background:{T['card']};border:2px solid {T['acc']}55;border-radius:18px;padding:24px 30px;margin-top:20px;font-size:32px;line-height:1.35}}
.foot{{position:absolute;left:0;right:0;bottom:56px;font-size:22px;color:{T['mut']};letter-spacing:2px}}
.src{{position:absolute;left:90px;right:90px;bottom:100px;font-size:20px;color:{T['mut']};opacity:.8}}
.bar{{position:absolute;left:90px;right:90px;bottom:36px;height:4px;background:{T['acc']}33}}.bar i{{display:block;height:4px;width:{int(100*n/total)}%;background:{T['acc']}}}"""
    body = f"<div class='k'>{_rich(s.get('kicker',''))}</div>"
    if tipo == "dado":
        body += f"<div class='big' style='font-size:240px;margin-top:20px'>{_rich(s['big'])}</div>"
    fs = 92 if tipo == "capa" else 64
    body += f"<div class='h t' style='font-size:{fs}px;margin-top:30px'>{_rich(s['titulo'])}</div><div class='rule'></div>"
    if s.get("corpo"):
        body += f"<div class='p'>{_rich(s['corpo'])}</div>"
    for it in s.get("itens", []):
        body += f"<div class='card'>{_rich(it)}</div>"
    if tipo == "cta":
        body += f"<div class='k' style='margin-top:40px'>{_html.escape(handle)}</div>"
    src = f"<div class='src'>{_rich(s['fonte'])}</div>" if s.get("fonte") else ""
    return (f"<!doctype html><html lang='pt-BR'><head><meta charset='utf-8'><style>{css}</style></head><body>"
            f"<div class='s'><div class='top'><img src='data:image/png;base64,{_b64(ASSETS/T['logo'])}'></div>"
            f"<div class='mid'>{body}</div>{src}<div class='foot'>{_html.escape(handle)} · {n}/{total}</div>"
            f"<div class='bar'><i></i></div></div></body></html>")


# Ajuste automático: número grande cabe na largura; conteúdo cabe na área segura (reduz escala, nunca corta).
_FIT_JS = """() => {
  const mid = document.querySelector('.mid'), big = document.querySelector('.big');
  if (big) { let f = 240; while (big.scrollWidth > mid.clientWidth && f > 80) { f -= 8; big.style.fontSize = f + 'px'; } }
  let k = 1, guard = 0;
  while (mid.scrollHeight > mid.clientHeight + 1 && guard++ < 30) {
    k -= 0.04;
    mid.querySelectorAll('.h,.p,.card,.big').forEach(e => {
      const base = e.dataset.base || (e.dataset.base = parseFloat(getComputedStyle(e).fontSize));
      e.style.fontSize = (base * k) + 'px';
    });
  }
  return {ok: mid.scrollHeight <= mid.clientHeight + 1, scale: Math.round(k * 100) / 100};
}"""


def render_series(slides, theme, out_dir, handle="@somosvexter", strict=True):
    errs = validate(slides, theme)
    if errs and strict:
        raise ValueError("Série fora do padrão:\n- " + "\n- ".join(errs))
    from playwright.sync_api import sync_playwright
    out = Path(out_dir); out.mkdir(parents=True, exist_ok=True); files = []
    fontcss = _fontface()
    with sync_playwright() as pw:
        b = pw.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1350})
        for i, s in enumerate(slides, 1):
            pg.set_content(html(s, i, len(slides), theme, handle, fontcss))
            pg.evaluate("async () => { await document.fonts.ready; return true }")
            fit = pg.evaluate(_FIT_JS)
            if not fit["ok"]:
                print(f"AVISO slide {i}: texto excede a área segura mesmo reduzido; encurte o conteúdo.")
            elif fit["scale"] < 0.85:
                print(f"AVISO slide {i}: texto reduzido para {int(fit['scale']*100)}%; considere encurtar.")
            f = out / f"slide_{i:02d}.png"; pg.screenshot(path=str(f)); files.append(f)
        b.close()
    return files


def make_grid(files, out_path, cols=3, thumb_w=360):
    """Miniatura em grade (como o perfil do Instagram) para conferir a coerência da série."""
    from PIL import Image
    files = [Path(f) for f in files]
    th = int(thumb_w * 1350 / 1080); gap = 6
    rows = (len(files) + cols - 1) // cols
    g = Image.new("RGB", (cols * thumb_w + (cols - 1) * gap, rows * th + (rows - 1) * gap), "#FFFFFF")
    for i, f in enumerate(files):
        im = Image.open(f).convert("RGB").resize((thumb_w, th))
        g.paste(im, ((i % cols) * (thumb_w + gap), (i // cols) * (th + gap)))
    Path(out_path).parent.mkdir(parents=True, exist_ok=True); g.save(out_path)
    return Path(out_path)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit("uso: python feed_template.py serie.json pasta_saida")
    cfg = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    fs = render_series(cfg["slides"], cfg.get("tema", "escuro"), sys.argv[2], cfg.get("handle", "@somosvexter"))
    print(make_grid(fs, Path(sys.argv[2]) / "_grade.png"))
