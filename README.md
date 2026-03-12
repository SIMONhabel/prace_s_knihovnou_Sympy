# Řešení úloh v Pythonu pomocí SymPy

Tento repozitář slouží k odevzdání vypracovaných úloh zaměřených na symbolickou matematiku v Pythonu s využitím knihovny `sympy`. 

## Co program dělá

Skript obsahuje řešení celkem 15 úloh, které ukazují různé možnosti práce se symbolickou matematikou. Po spuštění program do konzole postupně vypíše:
* Vytváření a úpravy matematických výrazů (např. vzorec pro kinetickou energii, Ohmův zákon).
* Zjednodušování a rozklady výrazů (pomocí funkcí `expand()`, `simplify()`, `factor()`).
* Řešení lineárních i kvadratických rovnic a soustav rovnic (pomocí funkce `solve()`).
* Zpětné dosazování a numerické vyhodnocení výsledků (`subs()`, `.evalf()`).
* Vlastní praktický příklad (výpočet výšky hladiny bazénu na základě objemu a poloměru).

V konzoli se také rovnou tisknou odpovědi na doplňující textové otázky ze zadání.

## Jak program spustit

**1. Požadavky**
Pro spuštění kódu je potřeba mít nainstalovaný Python 3 a knihovnu `sympy`. Knihovnu nainstalujete přes terminál pomocí příkazu:
```bash
pip install sympy