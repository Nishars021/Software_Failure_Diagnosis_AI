from src.budget import InvestigationBudget


budget = InvestigationBudget(
    max_hypotheses=3,
    max_rounds=2,
    max_evidence_checks=5
)


print("Can generate hypothesis:",
      budget.can_generate_hypothesis())

budget.add_hypotheses(3)

print("Hypotheses generated:",
      budget.hypotheses_generated)

print("Can generate another:",
      budget.can_generate_hypothesis())

budget.use_round()

print("Rounds used:",
      budget.rounds_used)

print("Budget exhausted:",
      budget.budget_exhausted())