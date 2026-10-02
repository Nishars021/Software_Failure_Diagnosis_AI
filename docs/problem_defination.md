# Problem Definition

## Domain
Software Failure Diagnosis

## Problem

Software applications can fail or experience performance problems for
many different reasons. A single failure may have multiple plausible
causes, and choosing one explanation too early can lead to incorrect
diagnosis.

## Goal

Build an evidence-grounded reasoning system that investigates software
failures by generating genuinely different possible causes, evaluating
evidence for and against each hypothesis, identifying missing information,
and recommending further diagnostic actions when the available evidence
is insufficient.

## Initial Failure Types

The first prototype will focus on:

- HTTP 500 errors
- Application crashes
- Slow application response
- Database-related failures
- External API failures

## Initial Example

Problem:

"The web application suddenly started returning HTTP 500 errors."

Possible causes may include:

- Database failure
- Recent software deployment
- Server/resource problem
- External API failure
- Configuration/environment problem
- Unknown cause