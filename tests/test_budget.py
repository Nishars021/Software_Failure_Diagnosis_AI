from src.budget import InvestigationBudget


budget = InvestigationBudget(
    max_hypotheses=6,
    max_rounds=3,
    max_evidence_checks=10
)

print("INVESTIGATION BUDGET TEST")
print("=" * 60)

print("Initial state:")
print("Rounds used:", budget.rounds_used)
print("Budget exhausted:", budget.budget_exhausted())

print("\nUsing round 1...")
budget.use_round()

print("Rounds used:", budget.rounds_used)
print("Budget exhausted:", budget.budget_exhausted())

print("\nUsing round 2...")
budget.use_round()

print("Rounds used:", budget.rounds_used)
print("Budget exhausted:", budget.budget_exhausted())

print("\nUsing round 3...")
budget.use_round()

print("Rounds used:", budget.rounds_used)
print("Budget exhausted:", budget.budget_exhausted())

print("\nFINAL CHECK")

if budget.budget_exhausted():
    print("PASS: Investigation stops when the round budget is exhausted.")
else:
    print("FAIL: Budget should be exhausted after maximum rounds.")