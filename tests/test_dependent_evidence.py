from src.evidence import Evidence, check_evidence_dependency


evidence_1 = Evidence(
    id="E1",
    description="CPU usage reached 95%",
    source="Server monitoring system",
    source_id="SERVER_MONITOR_001",
    reliability=0.95
)


evidence_2 = Evidence(
    id="E2",
    description="Server CPU usage was extremely high",
    source="Independent monitoring service",
    source_id="EXTERNAL_MONITOR_002",
    reliability=0.90
)


dependent = check_evidence_dependency(
    evidence_1,
    evidence_2
)


print("Evidence 1:", evidence_1.description)
print("Evidence 2:", evidence_2.description)
print("Same source:", dependent)

if dependent:
    print("Result: DEPENDENT evidence")
else:
    print("Result: Potentially independent evidence")