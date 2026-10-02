from src.main import diagnose
from src.evidence import Evidence


problem = "The web application suddenly started returning HTTP 500 errors."


evidence_list = [

    Evidence(
        id="E1",
        description="Database connection timeout detected",
        source="Application logs",
        source_id="LOG001",
        reliability=0.9
    ),

    Evidence(
        id="E2",
        description="New version was deployed 10 minutes ago",
        source="Deployment system",
        source_id="DEP001",
        reliability=0.9
    ),

    Evidence(
        id="E3",
        description="Database health check is normal",
        source="Database monitoring",
        source_id="DB001",
        reliability=0.8
    ),

    Evidence(
        id="E4",
        description="Server CPU and memory are normal",
        source="Server monitoring",
        source_id="SRV001",
        reliability=0.8
    ),

    Evidence(
        id="E5",
        description="External API health check is normal",
        source="API monitoring",
        source_id="API001",
        reliability=0.8
    )
]


result = diagnose(
    problem,
    evidence_list
)