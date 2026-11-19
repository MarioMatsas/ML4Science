# Data provenance and alignment with Chapter 3

The group datasets are derived from the frozen selective-delegation
reproduction package associated with Chapter 3.

## Headline binary comparison

The direct-versus-routed rows come from
`reference_outputs/paired_d0_d2.csv`. This is the authoritative 1,099-row
paired table used for the Chapter 3 Stage 1 and Stage 2 results. It compares
the direct `D=0,T=2` run with the routed `D=2,T=2` Orchestrator across five
base-model families and 228 unique questions. Its SHA-256 is
`802f600f7cfef86e43499c836d391146fa29d8dab5901b3052a7e1c2f884211a`.

## Question metadata

Question source, text, date partition, and forecast-time market probability
come from the same 12 question-set JSON files used to construct the
228-question benchmark. For the 28 label-flipped augmented questions, the
market probability is transformed from `p` to `1-p`.

## Direct-response text

Group 2 adds only the model-generated `reasoning` or `full` field from the
matching direct `D=0,T=2` JSON result. Tool-call payloads, prompts, routed
traces, subagent outputs, credentials, and local paths are excluded. Seven
source direct responses have no text and remain missing.

## Multi-budget actions

Group 3 uses the `summary.csv` files for the logged `D=0`, `D=2`, `D=3`, and
`D=5` configurations. The primary three-action matrix keeps the fully matched
`direct_D0_T2`, `routed_D2_T2`, and `routed_D3_T2` actions for each of the
1,099 headline contexts. The optional six-action table has incomplete action
coverage and must not treat missing actions as failures.

## Split and test protection

The split is chronological and defined at the question level: 151 training,
34 validation, and 43 test questions. Every model and action associated with a
question stays in the same split. Student files blank all test targets and
action outcomes. Private answer keys are stored outside the distribution
packages.

The Chapter 3 reproduction verifier passes for all 11 frozen reference outputs
at absolute tolerance `1e-9`.

