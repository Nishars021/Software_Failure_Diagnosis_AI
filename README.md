# Software Failure Diagnosis AI

An AI-inspired diagnostic system for identifying possible causes of software failures from observed evidence.

## 1. Project Overview

Software failures can have multiple possible causes such as database failures, recent deployments, server/resource problems, external API failures, or configuration issues.

The **Software Failure Diagnosis AI** system investigates these possibilities instead of immediately selecting a single cause.

The system:

- Generates multiple alternative hypotheses
- Ensures hypotheses are meaningfully different
- Represents assumptions and predicted effects
- Classifies evidence as supporting, contradicting, missing, or dependent
- Calculates confidence scores
- Handles insufficient evidence through UNKNOWN/abstention
- Recommends discriminating tests when hypotheses are difficult to distinguish
- Combines compatible hypotheses when appropriate
- Uses an investigation budget and stopping rule
- Evaluates performance on test and held-out cases

---

## 2. Problem Statement

Given a software failure and a set of observed evidence, determine the most plausible underlying cause while avoiding premature conclusions.

The system must be able to:

1. Generate genuinely different hypotheses.
2. Compare hypotheses using multiple evidence dimensions.
3. Update confidence based on supporting and contradicting evidence.
4. Detect when available evidence is insufficient.
5. Recommend additional diagnostic tests when required.
6. Combine compatible hypotheses when multiple causes may contribute.
7. Stop investigation when further exploration is unnecessary or the investigation budget is exhausted.

---

## 3. System Architecture

The diagnostic pipeline follows these stages:

```text
Software Failure
       │
       ▼
Hypothesis Generation
       │
       ▼
Hypothesis Validation
       │
       ▼
Evidence Assessment
       │
       ▼
Confidence Scoring
       │
       ▼
Stopping Rule
       │
       ├───────────────┐
       ▼               ▼
   Selection       Close/Tied
                       │
              ┌────────┴────────┐
              ▼                 ▼
          Synthesis       Discriminating Test
              │                 │
              └────────┬────────┘
                       ▼
                 Final Decision