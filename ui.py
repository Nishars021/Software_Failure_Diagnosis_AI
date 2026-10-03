import streamlit as st

from src.main import diagnose
from src.evidence import Evidence


# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="Software Failure Diagnosis AI",
    page_icon="🔍",
    layout="wide"
)


# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.title("🔍 Software Failure Diagnosis AI")
st.caption("Evidence-Grounded Diagnostic Assistant")

st.divider()


# ---------------------------------------------------------
# INPUT SECTION
# ---------------------------------------------------------

st.subheader("Describe the Software Failure")

problem = st.text_area(
    "Failure Description",
    placeholder=(
        "Example: The application is failing because it cannot "
        "connect to the customer database."
    ),
    height=120
)

st.subheader("Evidence")

evidence_text = st.text_area(
    "Enter the available evidence",
    placeholder=(
        "Enter one evidence item per line.\n\n"
        "Example:\n"
        "Database connection timeout detected\n"
        "Database health check is normal"
    ),
    height=150
)


# ---------------------------------------------------------
# DIAGNOSE BUTTON
# ---------------------------------------------------------

if st.button("🔍 Diagnose Failure", type="primary"):

    if not problem.strip():
        st.warning("Please describe the software failure.")

    else:

        # Convert each evidence line into an Evidence object
        evidence_list = []

        evidence_lines = [
            line.strip()
            for line in evidence_text.splitlines()
            if line.strip()
        ]

        for index, description in enumerate(evidence_lines, start=1):

            evidence = Evidence(
                id=f"UI_E{index}",
                description=description,
                source="User Input",
                source_id=f"UI_SOURCE_{index}",
                reliability=1.0
            )

            evidence_list.append(evidence)

        # -------------------------------------------------
        # RUN EXISTING DIAGNOSIS ENGINE
        # -------------------------------------------------

        with st.spinner("Analyzing failure and evaluating hypotheses..."):

            result = diagnose(
                problem,
                evidence_list
            )

        st.success("Diagnosis completed successfully.")

        st.divider()


        # -------------------------------------------------
        # DIAGNOSTIC RESULTS
        # -------------------------------------------------

        st.subheader("📊 Diagnostic Results")

        scores = result["scores"]
        decision = result["decision"]
        stopping = result["stopping"]


        # -------------------------------------------------
        # SUMMARY METRICS
        # -------------------------------------------------

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Hypotheses",
                len(result["hypotheses"])
            )

        with col2:
            st.metric(
                "Evidence Items",
                len(evidence_list)
            )

        with col3:
            st.metric(
                "Decision",
                decision.outcome
            )


        st.divider()


        # -------------------------------------------------
        # HYPOTHESIS SCORES
        # -------------------------------------------------

        st.subheader("🧠 Hypothesis Confidence")

        for score in sorted(
            scores,
            key=lambda x: x.confidence,
            reverse=True
        ):

            hypothesis = next(
                (
                    h for h in result["hypotheses"]
                    if h.id == score.hypothesis_id
                ),
                None
            )

            if hypothesis is None:
                continue

            st.markdown(
                f"### {hypothesis.id} — {hypothesis.cause}"
            )

            st.progress(
                min(int(score.confidence), 100)
            )

            col1, col2, col3 = st.columns(3)

            with col1:
                st.write(
                    f"**Confidence:** {score.confidence:.2f}%"
                )

            with col2:
                st.write(
                    f"**Supporting weight:** "
                    f"{score.supporting_weight:.2f}"
                )

            with col3:
                st.write(
                    f"**Contradicting weight:** "
                    f"{score.contradicting_weight:.2f}"
                )

            st.divider()


        # -------------------------------------------------
        # FINAL DECISION
        # -------------------------------------------------

        st.subheader("🎯 Final Decision")

        if decision.outcome == "SELECT":

            st.success(
                f"✓ SELECT — "
                f"{', '.join(decision.selected_hypotheses)}"
            )

        elif decision.outcome == "COMBINE":

            st.info(
                f"🔗 COMBINE — "
                f"{', '.join(decision.selected_hypotheses)}"
            )

        elif decision.outcome == "TEST":

            st.warning(
                f"🧪 TEST — "
                f"{', '.join(decision.selected_hypotheses)}"
            )

        else:

            st.error(
                "⚠ ABSTAIN — Insufficient evidence"
            )


        st.write("**Explanation:**")

        st.write(decision.explanation)


        # -------------------------------------------------
        # STOPPING ANALYSIS
        # -------------------------------------------------

        st.subheader("⏹ Investigation Status")

        if isinstance(stopping, tuple):
            stop, reason = stopping
        elif isinstance(stopping, dict):
            stop = stopping.get("stop", False)
            reason = stopping.get("reason", "No stopping reason available.")
        else:
            stop = False
            reason = "No stopping reason available."


        if stop:
            st.success("Investigation stopped")
        else:
            st.info("Investigation can continue")

        st.write(f"**Reason:** {reason}")