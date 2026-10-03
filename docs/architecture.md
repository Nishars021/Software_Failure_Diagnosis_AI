# System Architecture

## 1. Overview

Software Failure Diagnosis AI follows a modular diagnostic pipeline.

The system separates hypothesis generation, validation, evidence assessment, scoring, decision making, testing, synthesis, budgeting, and stopping.

This modular design makes each reasoning stage independently testable.

## 2. Architecture Flow

```text
                    ┌─────────────────────┐
                    │   Failure Input     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Hypothesis Generator│
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Hypothesis Validator│
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Evidence Assessment │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Confidence Scoring  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Stopping Rule     │
                    └──────────┬──────────┘
                               │
                ┌──────────────┼──────────────┐
                │              │              │
                ▼              ▼              ▼
            SELECT         COMBINE          TEST
                │              │              │
                │              ▼              │
                │         Synthesis           │
                │              │              │
                └──────────────┼──────────────┘
                               │
                               ▼
                         Final Decision
                               │
                               ▼
                         ABSTAIN / UNKNOWN