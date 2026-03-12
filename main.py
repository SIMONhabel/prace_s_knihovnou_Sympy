import sympy as sp

print("--- Úloha 1 & 2: Kinetická energie ---")
# 1. 
m, v = sp.symbols('m v')
# 2.
E = sp.Rational(1, 2) * m * v**2
print(f"Vzorec pro E: {E}")

# Úloha 2
E_hodnota = E.subs({m: 1200, v: 25})
print(f"Číselná hodnota (přesně): {E_hodnota}")
print(f"Číselná hodnota (.evalf()): {E_hodnota.evalf()} J")
print()

print("--- Úloha 3: Zjednodušování výrazů ---")
A, B = sp.symbols('A B')
vyraz3 = (A + B)**2 - (A**2 + 2*A*B)
print(f"Původní výraz: {vyraz3}")
print(f"Po expand(): {vyraz3.expand()}")
print(f"Po simplify(): {sp.simplify(vyraz3)}")
print("Odpověď: Po zjednodušení zůstane pouze B**2.")
print()

print("--- Úloha 4: Rozklad výrazu ---")
x = sp.symbols('x')
vyraz4 = x**2 - 25
print(f"Rozložený výraz: {sp.factor(vyraz4)}")
print("Odpověď: Připomíná to vzorec pro rozdíl čtverců (a^2 - b^2) = (a-b)(a+b).")
print()

print("--- Úloha 5: Řešení rovnice (Dráha) ---")
s, t = sp.symbols('s t')

rovnice5 = sp.Eq(s, v * t)

cas_t = sp.solve(rovnice5, t)[0]
print(f"Vyjádřený čas t: {cas_t}")

vysledek_cas = cas_t.subs({s: 150, v: 75})
print(f"Výsledný čas: {vysledek_cas} hodin")
print()

print("--- Úloha 6: Kvadratická rovnice (Míč) ---")

h = sp.symbols('h')
rovnice6 = sp.Eq(h, -5*t**2 + 20*t)

casy = sp.solve(rovnice6.subs(h, 0), t)
print(f"Časy, kdy je výška 0: {casy}")
print("Odpověď: První čas (0) je okamžik výkopu/odpalu. Druhý čas (4) je okamžik dopadu na zem.")
print()

print("--- Úloha 7: Soustava rovnic ---")
c_sesit, c_tuzka = sp.symbols('c_sesit c_tuzka')
rovnice7_1 = sp.Eq(3*c_sesit + 2*c_tuzka, 44)
rovnice7_2 = sp.Eq(2*c_sesit + 5*c_tuzka, 46)
reseni7 = sp.solve((rovnice7_1, rovnice7_2), (c_sesit, c_tuzka))
print(f"Ceny: Sešit = {reseni7[c_sesit]} Kč, Tužka = {reseni7[c_tuzka]} Kč")
print()

print("--- Úloha 8: Ohmův zákon ---")
U, R, I = sp.symbols('U R I')
ohm = sp.Eq(U, R * I)
print(f"Odpor R: {sp.solve(ohm, R)[0]}")
print(f"Proud I: {sp.solve(ohm, I)[0]}")
print()

print("--- Úloha 9: Vícenásobné dosazování (Hustota) ---")
rho, V = sp.symbols('rho V')
hustota_rovnice = sp.Eq(rho, m / V)
hmotnost_vyjadrena = sp.solve(hustota_rovnice, m)[0]
vysledna_hmotnost = hmotnost_vyjadrena.subs({rho: 7800, V: 0.002})
print(f"Hmotnost je: {vysledna_hmotnost.evalf()} kg")
print("Odpověď: Hustotu 7800 kg/m3 má ocel nebo železo.")
print()

print("--- Úloha 10: Rozvoj výrazu ---")
p, q = sp.symbols('p q')
vyraz10 = (p + q)**3
rozvinuty_vyraz = vyraz10.expand()
print(f"Rozvinutý výraz: {rozvinuty_vyraz}")
print("Odpověď: Výsledný výraz má 4 členy.")
print()

print("--- Úloha 11: Ověření rovnosti ---")
a, b = sp.symbols('a b')
vyraz11_a = (a + b)**2
vyraz11_b = a**2 + 2*a*b + b**2
rozdil = sp.simplify(vyraz11_a - vyraz11_b)
print(f"Rozdíl výrazů: {rozdil}")
print("Odpověď: Výrazy jsou stejné, pokud jejich rozdíl po zjednodušení dá 0.")
print()

print("--- Úloha 12: Vyjádření proměnné ---")
rovnice12 = sp.Eq(v, s / t)
print(f"Dráha s: {sp.solve(rovnice12, s)[0]}")
print(f"Čas t: {sp.solve(rovnice12, t)[0]}")
print("Odpověď: Ve vzorci v = s/t je rychlost 'v' závislá proměnná (její hodnota závisí na s a t).")
print()

print("--- Úloha 13: Kontrola řešení ---")
rovnice13 = sp.Eq(3*x + 7, 25)
reseni13 = sp.solve(rovnice13, x)[0]
print(f"Kořen rovnice x = {reseni13}")
kontrola = rovnice13.subs(x, reseni13)
print(f"Kontrola dosazením: {kontrola}")
print("Odpověď: Dosazení ověří, že jsme neudělali chybu (např. znaménkovou) a levá strana se opravdu rovná pravé.")
print()

print("--- Úloha 14: Symbolický model ceny ---")
C, d = sp.symbols('C d')
rovnice14 = sp.Eq(C, p * q + d)
pocet_kusu_q = sp.solve(rovnice14, q)[0]
vysledek_kusy = pocet_kusu_q.subs({C: 550, p: 45, d: 100})
print(f"Vzorec pro počet kusů: {pocet_kusu_q}")
print(f"Lze koupit kusů: {vysledek_kusy}")
print()

print("--- Úloha 15: Vlastní příklad (Zahradní bazén) ---")

r_bazen, h_bazen = sp.symbols('r_bazen h_bazen')
objem_V = sp.symbols('objem_V')
rovnice_bazen = sp.Eq(objem_V, sp.pi * r_bazen**2 * h_bazen)


vyska_h = sp.solve(rovnice_bazen, h_bazen)[0]
konkretni_vyska = vyska_h.subs({objem_V: 10, r_bazen: 2}).evalf(4)

print(f"Vzorec pro výšku bazénu: {vyska_h}")
print(f"Potřebná výška hladiny: {konkretni_vyska} m")

