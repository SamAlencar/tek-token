#!/usr/bin/env python3
"""Confere a documentação do Tek Token (só documentação, sem código da plataforma).

1. Todo link Markdown relativo aponta para um arquivo existente no repositório.
2. docs/BACKLOG.md: itens TK-T001, TK-T002, ... em sequência, cada um com
   Entregável (em crase), Critério de aceite, Depende de, Fase e Status.
3. docs/DUVIDAS.md: dúvidas D-001, D-002, ... em sequência, cada uma com
   Origem, Pergunta, Decisão provisória, Fonte e Status.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXTERNO = ("http://", "https://", "mailto:", "tel:")
RE_LINK = re.compile(r"\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
RE_ITEM = re.compile(r"^### (TK-T(\d{3})) — (.+)$")
RE_DUVIDA = re.compile(r"^### (D-(\d{3})) — (.+)$")


def arquivos_md() -> list[Path]:
    return sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts and "node_modules" not in p.parts)


def conferir_links(erros: list[str]) -> int:
    total = 0
    for arq in arquivos_md():
        em_bloco = False
        for n, linha in enumerate(arq.read_text(encoding="utf-8").splitlines(), 1):
            if linha.lstrip().startswith("```"):
                em_bloco = not em_bloco
                continue
            if em_bloco:
                continue
            for alvo in RE_LINK.findall(re.sub(r"`[^`]*`", "", linha)):
                if alvo.startswith("#") or alvo.lower().startswith(EXTERNO):
                    continue
                caminho = alvo.split("#", 1)[0]
                if not caminho:
                    continue
                total += 1
                destino = (arq.parent / caminho).resolve()
                rel = arq.relative_to(ROOT)
                try:
                    destino.relative_to(ROOT)
                except ValueError:
                    erros.append(f"{rel}:{n}: link sai do repositório: {alvo}")
                    continue
                if not destino.exists():
                    erros.append(f"{rel}:{n}: link interno quebrado: {alvo}")
    return total


def secoes(caminho: Path, padrao: re.Pattern[str]) -> list[tuple[str, int, str]]:
    linhas = caminho.read_text(encoding="utf-8").splitlines()
    achados = [(i, padrao.match(l)) for i, l in enumerate(linhas)]
    achados = [(i, m) for i, m in achados if m]
    out = []
    for k, (i, m) in enumerate(achados):
        fim = achados[k + 1][0] if k + 1 < len(achados) else len(linhas)
        out.append((m.group(1), int(m.group(2)), "\n".join(linhas[i:fim])))
    return out


def conferir_lista(caminho: Path, padrao, prefixo: str, campos: tuple[str, ...], erros: list[str]) -> int:
    itens = secoes(caminho, padrao)
    rel = caminho.relative_to(ROOT)
    if not itens:
        erros.append(f"{rel}: nenhum item {prefixo}NNN encontrado")
    for esperado, (ident, num, corpo) in enumerate(itens, 1):
        if num != esperado:
            erros.append(f"{rel}: {ident} fora de sequência (esperado {prefixo}{esperado:03d})")
        for campo in campos:
            if not re.search(rf"(?m)^- {re.escape(campo)}", corpo):
                erros.append(f"{rel}: {ident} sem campo '- {campo}'")
        if not re.search(r"(?m)^- Status: \[[ xX]\]", corpo):
            erros.append(f"{rel}: {ident} sem linha '- Status: [ ]' ou '- Status: [x]'")
    return len(itens)


def main() -> int:
    erros: list[str] = []
    links = conferir_links(erros)
    itens = conferir_lista(ROOT / "docs" / "BACKLOG.md", RE_ITEM, "TK-T",
                           ("Entregável: `", "Critério de aceite:", "Depende de:", "Fase:"), erros)
    duvidas = conferir_lista(ROOT / "docs" / "DUVIDAS.md", RE_DUVIDA, "D-",
                             ("Origem:", "Pergunta:", "Decisão provisória", "Fonte:"), erros)
    if erros:
        print("\n".join(erros))
        return 1
    print(f"OK: {links} links internos, {itens} itens no backlog, {duvidas} dúvidas")
    return 0


if __name__ == "__main__":
    sys.exit(main())
