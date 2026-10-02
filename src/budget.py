from dataclasses import dataclass


@dataclass
class InvestigationBudget:
    max_hypotheses: int = 6
    max_rounds: int = 3
    max_evidence_checks: int = 10

    hypotheses_generated: int = 0
    rounds_used: int = 0
    evidence_checks_used: int = 0

    def can_generate_hypothesis(self) -> bool:
        return self.hypotheses_generated < self.max_hypotheses

    def can_continue_round(self) -> bool:
        return self.rounds_used < self.max_rounds

    def can_check_evidence(self) -> bool:
        return self.evidence_checks_used < self.max_evidence_checks

    def add_hypotheses(self, count: int = 1):
        self.hypotheses_generated += count

    def use_round(self):
        self.rounds_used += 1

    def use_evidence_check(self):
        self.evidence_checks_used += 1

    def budget_exhausted(self) -> bool:
        return (
            self.hypotheses_generated >= self.max_hypotheses
            or self.rounds_used >= self.max_rounds
            or self.evidence_checks_used >= self.max_evidence_checks
        )