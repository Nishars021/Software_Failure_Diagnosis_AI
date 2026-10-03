# Problem Definition

## 1. Problem

Software failures can occur because of several different underlying causes. A single observed symptom may therefore correspond to multiple plausible explanations.

The goal of Software Failure Diagnosis AI is to determine the most plausible cause of a software failure while explicitly handling uncertainty and alternative explanations.

## 2. Input

The system receives:

- A description of the software failure.
- A collection of observed evidence.
- Evidence provenance and reliability information.

## 3. Possible Causes

The current diagnostic system considers the following major causes:

1. Database failure
2. Recent software deployment
3. Server/resource problem
4. External API failure
5. Configuration/environment problem
6. UNKNOWN when the available evidence is insufficient

## 4. Diagnostic Requirements

The system should:

- Generate multiple alternative hypotheses.
- Ensure that hypotheses are meaningfully distinct.
- Represent assumptions and predicted effects.
- Evaluate evidence against each hypothesis.
- Distinguish supporting and contradicting evidence.
- Identify missing evidence.
- Avoid double-counting dependent evidence.
- Calculate confidence for each hypothesis.
- Select a leading hypothesis when evidence is sufficiently strong.
- Recommend a discriminating test when leading hypotheses remain close.
- Combine compatible hypotheses when multiple causes may contribute.
- Abstain when available evidence is insufficient.
- Operate within a defined investigation budget.

## 5. Output

The diagnostic engine produces one of the following outcomes:

### SELECT

A sufficiently supported hypothesis is selected.

### COMBINE

Two compatible hypotheses with sufficient supporting evidence are combined into a joint explanation.

### TEST

The leading hypotheses remain difficult to distinguish, so an additional diagnostic test is recommended.

### ABSTAIN / UNKNOWN

The evidence is insufficient to confidently identify a known cause.

## 6. Constraints

The system uses a bounded investigation process.

The investigation is limited by:

- Maximum number of hypotheses
- Maximum investigation rounds
- Maximum evidence checks

This prevents unlimited exploration and provides a defined stopping condition.

## 7. Unknown-Cause Handling

The system must not force every failure into one of the predefined causes.

If the evidence does not sufficiently support a known hypothesis, the system can return UNKNOWN or abstain.

This is important for failures that fall outside the current hypothesis space.

## 8. Objective

The overall objective is to build a structured diagnostic reasoning system that can:

```text
Failure
   ↓
Alternative Hypotheses
   ↓
Evidence Evaluation
   ↓
Confidence Scoring
   ↓
Decision / Test / Synthesis / Abstention