# Academic research collaboration — reliable AI-assisted research

**Status:** invitation to co-design a study; no agreed protocol, author list, institutional affiliation, research findings or submission yet.

This compartment is for academic collaborators interested in developing a reproducible investigation that could lead to a jointly written research paper. The research question and contributions are open to discussion. No model-transfer exercise, codename or agent setup is required. Other repository branches and their experiments are independent.

## Proposed starting question

Can targeted external verification improve the factual fidelity of AI-assisted scientific writing while preserving correct content and reducing unnecessary revision, compared with unassisted generation or model-only self-correction?

This is a proposed methodological study, not a claim of novelty. It connects AI evaluation, scientific communication, explainability and reproducibility without requiring a domain-specific dataset or laboratory. A collaborator may propose another research question.

## Draft study design — for discussion before execution

| Condition | Intervention |
|---|---|
| A | Initial answer with the supplied task and evidence |
| B | Same initial answer, model-only review; revisions optional |
| C | Same initial answer, targeted checks against authoritative source passages and deterministic metadata/format checks |
| D (optional) | Same initial answer, more intensive external verification under recorded resource limits |

Use paired initial responses, matched model versions/settings, frozen tasks, comparable evidence access and declared resource budgets. Record intervention differences explicitly. Independent human review should be blinded to condition where feasible. Develop the rubric and stopping policy on development cases; keep separately authored evaluation cases unseen. Predefine what counts as an error, a supported claim, an appropriate abstention, a correct-to-incorrect revision and an incorrect-to-correct revision. Report uncertainty and paired comparisons at the task level, not independent statistics for successive passes. Do not discard unsuccessful runs.

Candidate outcomes: factual support and citation accuracy, requirement coverage, correction gain/damage, unresolved cases, latency and resource usage. Choose the primary outcome, sample size and analysis plan jointly before evaluation. No arbitrary qualification threshold, fixed optimum or expected improvement is assumed.

## Contribution path

1. Discuss a specific research question, related work and feasibility.
2. Agree on scope, evidence sources, data permissions, evaluation criteria and analysis before running the study.
3. Contribute a small, independently inspectable test set or methodology through a fork/PR targeting `academic-research-collaboration`. Cases can initially be synthetic or use properly licensed public non-sensitive source material.
4. Preserve the protocol revision, source identifiers and passages, data/license provenance, prompts/settings, code revision, raw outputs, reviewer decisions and run environment; keep negative results and limitations.
5. Invite independent replication; assess novelty and results before choosing a venue or writing claims.

For a candidate case, supply: case ID, research task, source identity/version and relevant evidence, independently established expected facts or criteria, allowed variation, and the intended error being tested. Keep held-out labels separate from prompts.

## Publication and research integrity

Human collaborators jointly agree on roles, authorship, acknowledgments, data/code sharing, funding/conflicts, AI-use disclosure and venue-specific requirements. [CRediT](https://credit.niso.org/contributor-roles-defined/) can describe actual contributions; it does not by itself establish authorship. No automatic coauthorship, institutional endorsement or guarantee of publication. Verify citations against primary sources and distinguish commentary from original empirical research.

Use synthetic or openly permitted non-sensitive materials initially. Do not upload patient records, confidential datasets, unpublished collaborator manuscripts, personal information, or restricted material to this public repository. This is an AI methodology research workspace, not a clinical tool or a biological experiment. Any separate domain study needs its own consent, ethics, safety, data-use and institutional requirements as applicable. Agree code/data licenses before reuse or public release; this invitation does not grant rights over existing third-party work.

## Initial literature leads

- Huang et al. (2024), *Large Language Models Cannot Self-Correct Reasoning Yet*, ICLR. https://arxiv.org/abs/2310.01798 — model-only correction limitations in tested reasoning tasks; not a blanket prohibition on external feedback.
- Gao et al. (2023), *Enabling Large Language Models to Generate Text with Citations*, EMNLP. https://aclanthology.org/2023.emnlp-main.398/ — separates citation quality from other output properties.
- [ACM artifact review and badging policy](https://www.acm.org/publications/policies/artifact-review-and-badging-current) — reference for reproducible software artifacts, not a badge or qualification already obtained.

These are starting references, not a completed related-work or novelty review.

## Current state

Only the invitation and draft study design have been established. No experiments, datasets, manuscript, named author commitments, model results, or claims of publication readiness. First step: agree on a research question and roles with interested human collaborators.
