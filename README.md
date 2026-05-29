# Séries Chronologiques — Préparation au module (INSEA)

Préparation complète au module de **Séries Chronologiques** à partir du cours du
Pr. Fadoua **BADAOUI** (INSEA) et du recueil d'anciennes questions d'examen
(`sc.txt`).

## Livrables (dossier `latex/`)

| Document | Description | Pages |
|---|---|---|
| **`Questions_SC.pdf`** | Toutes les questions/exercices de `sc.txt`, nettoyés, reformulés, **classés par thème** et **dédoublonnés** (11 sections + hors-programme). | 10 |
| **`Solutions_SC.pdf`** | **Corrigé détaillé** de chaque question (même numérotation), entièrement **fondé sur le cours BADAOUI**. Section « Hors programme » isolée. | 17 |
| **`Cours_SC.pdf`** | **Cours réécrit**, structuré et rigoureux (définitions, théorèmes démontrés, encadrés « Recette d'examen » reliés aux questions). 5 chapitres. | 14 |

Les sources LaTeX (`*.tex`, `preamble.tex`) sont fournies dans `latex/`.

## Thèmes couverts
QCM théoriques · stationnarité / causalité / inversibilité · représentations
MA(∞) et AR(∞) · autocorrélations ACF/PACF · prévision et intervalles de
confiance · intégration / ARIMA / tests de Dickey–Fuller · estimation et
équations de Yule–Walker · décomposition (tendance, saisonnalité, moyennes
mobiles, CVS) · identification graphique · exercices de synthèse.

## Recompiler les PDF
Pré-requis : une distribution LaTeX (TeX Live) avec `latexmk` et `babel-french`.
```bash
cd latex
latexmk -pdf Questions_SC.tex
latexmk -pdf Solutions_SC.tex
latexmk -pdf Cours_SC.tex
```

## Plan de travail
Voir `TODO.md` (déroulé en 5 phases).
