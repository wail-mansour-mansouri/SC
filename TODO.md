# Plan de travail — Préparation au module de Séries Chronologiques (SC)

> Objectif global : à partir du cours du Pr. Fadoua BADAOUI (INSEA) et du recueil de
> questions `sc.txt`, produire **3 documents PDF** soignés, rigoureux et orientés examen :
> 1. **`Questions_SC.pdf`** — toutes les questions/exercices extraits de `sc.txt`,
>    nettoyés, traduits/formatés en LaTeX, **regroupés par catégories**, **dédoublonnés**.
> 2. **`Solutions_SC.pdf`** — corrigé **détaillé** de chaque question, **basé sur le cours**,
>    avec une **section séparée « Hors programme »** pour ce qui dépasse le cours BADAOUI.
> 3. **`Cours_SC.pdf`** — réécriture **complète, structurée et mathématiquement rigoureuse**
>    du cours, orientée vers la résolution des questions de `sc.txt` (pas un résumé).

## Sources analysées (cours prof = tous les PDF sauf sc.txt)
- `SC-1-49 (3).pdf`, `SC-50-89-1.pdf`, `SC-90-129-1.pdf`, `SC 2024-127-148.pdf`,
  `SC 2024-161-184.pdf` → cours principal (190 diapositives).
- `decomposition (1).pdf`, `resumé decomposition-1.pdf`,
  `ajustements des coeficient saisonniers (1).pdf` → décomposition / coeff. saisonniers.
- `Série 1 (1).pdf`, `serie 2 sc.pdf` → feuilles de TD.
- `sc.txt` → recueil d'anciennes questions d'examen (OCR, très répétitif).

## Catégories de questions identifiées dans `sc.txt`
- A. QCM théoriques (stationnarité, MM, MM4, AR/MA/ARMA/SARIMA, validation, X11, Holt-Winters, lissage).
- B. Stationnarité / causalité / inversibilité de processus donnés.
- C. Représentations MA(∞) et AR(∞) (coefficients ψ_k, π_k).
- D. Autocorrélations simples ρ(k) et partielles (PACF).
- E. Prévision ponctuelle + variance d'erreur + intervalle de confiance.
- F. Intégration / ARIMA / tests de Dickey-Fuller.
- G. Estimation / équations de Yule-Walker.
- H. Décomposition (tendance, saisonnalité, MM, CVS) — TD Série 1, IPI, etc.
- I. Identification graphique (séries ↔ graphes, corrélogrammes ACF/PACF).
- J. Exercices de synthèse (Y=X+bruit, variance de moyenne, sous-échantillonnage…).
- Z. **Hors programme BADAOUI** (bruit blanc fort/faible, stationnarité mutuelle,
  projection orthogonale L², inverses d'opérateurs façon Charpentier…).

## Découpage en 5 phases (max)

### Phase 1 — Infrastructure + Document des QUESTIONS  ✅ cible
- [x] Installer chaîne LaTeX + pymupdf ; extraire texte/figures des PDF.
- [x] Analyser cours + sc.txt en détail ; cataloguer/ dédoublonner les questions.
- [x] Créer préambule LaTeX commun (`preamble.tex`).
- [x] Rédiger `Questions_SC.tex` (toutes les questions, par catégories, sans doublons).
- [x] Compiler `Questions_SC.pdf`. Commit + push. (10 pages)

### Phase 2 — SOLUTIONS (partie 1 : théorie + algèbre des processus)
- [x] Corrigés : A (QCM), B (stationnarité/causalité/inversibilité),
      C (représentations MA∞/AR∞).
- [x] Compiler une première version de `Solutions_SC.pdf`. Commit + push.

### Phase 3 — SOLUTIONS (partie 2 : ACF/PACF, prévision, ARIMA, décomposition, hors-prog)
- [x] Corrigés : D (ACF/PACF), E (prévision+IC), F (ARIMA/Dickey-Fuller),
      G (Yule-Walker), H (décomposition), I (identification), J (synthèse).
- [x] Section **Hors programme** (Z) clairement isolée.
- [x] Compiler `Solutions_SC.pdf` complet. Commit + push. (17 pages)

### Phase 4 — COURS réécrit (rigoureux, orienté questions)
- [x] Rédiger `Cours_SC.tex` : définitions, théorèmes (avec preuves clés),
      méthodes pas-à-pas, encadrés « recette d'examen » reliés aux questions.
- [x] Compiler `Cours_SC.pdf`. Commit + push. (14 pages, 5 chapitres)

### Phase 5 — Revue finale & cohérence
- [ ] Relecture croisée (questions ↔ solutions ↔ cours), vérif. numérique des calculs.
- [ ] Corrections, harmonisation typographique, table des matières/index.
- [ ] Recompilation des 3 PDF + commit + push final.

## Conventions retenues
- Langue : **français** (cours et questions sont en français).
- Notations alignées sur le cours BADAOUI : `B` opérateur retard, `a_t` bruit blanc,
  `Φ(B)`, `Θ(B)`, `ρ(k)`, `P(k)`/FAP, `γ(k)`, `ψ_k` (MA∞), `π_k` (AR∞).
- Les QCM sont fournis **avec corrigé** (bonne réponse justifiée).
- Tout point dépassant le cours BADAOUI est marqué et placé en section « Hors programme ».
