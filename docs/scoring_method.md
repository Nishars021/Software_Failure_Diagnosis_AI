# Scoring Method

## 1. Purpose

The scoring module converts evidence assessments into a confidence value for each hypothesis.

The objective is to increase confidence when reliable supporting evidence is present and decrease confidence when reliable contradicting evidence is present.

---

## 2. Evidence Contributions

Each evidence item can contribute in one of four ways:

- Supporting
- Contradicting
- Missing
- Dependent

Only supporting and contradicting evidence directly contributes to the score.

Missing evidence does not increase or decrease the score.

Dependent evidence is excluded from independent evidence counting to avoid double-counting.

---

## 3. Evidence Reliability

Each evidence item has a reliability value.

The reliability value represents how strongly that evidence should influence the hypothesis score.

For example:

```text
High reliability evidence
        ↓
Greater contribution

Low reliability evidence
        ↓
Smaller contribution