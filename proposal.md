# Learning an Interpretable Router from Structured Pre-Routing Signals

## Background

An agentic forecasting system can answer a question with a relatively inexpensive direct workflow or spend additional inference compute through retrieval and delegation. Additional compute is useful on some questions and harmful or wasteful on others. A fixed policy therefore leaves a natural allocation problem: can a system recognize, before routing, which questions are likely to benefit from a more expensive workflow?

Chapter 3 studied this problem using 228 resolved binary forecasting questions and five base-model families. Direct-forecast uncertainty was positively associated with the realized Brier-score improvement from routing for every model family. However, only three of five Orchestrators spent significantly more compute when the direct forecast was uncertain. This project turns that diagnostic result into an explicit machine-learning policy.

No forecasting agents need to be rerun. The project uses logged direct and routed forecasts, costs, and outcomes from the Chapter 3 experiments.

## Research question

**Can structured information available after a cheap direct forecast, but before routing, predict the marginal value of additional agentic compute and improve the held-out quality-cost frontier?**

For each model-question pair, the policy chooses between:

1. **Stop:** return the direct `D=0,T=2` probability forecast.
2. **Route:** use the more expensive `D=2,T=2` Orchestrator forecast.

If `p_direct` and `p_routed` are the two probability forecasts and `y` is the eventual binary outcome, the realized benefit of routing is

`Delta Brier = (p_direct - y)^2 - (p_routed - y)^2`.

Positive values mean that routing improved the probability forecast. The main task is to predict this quantity, or a carefully justified decision target derived from it, without using the resolved outcome or any routed-run information.

## Data

The primary table contains 1,099 matched model-question pairs from five base-model families. Four families cover all 228 questions; DeepSeek has 187 complete headline pairs because some routed source runs are missing. Every row contains the same direct-versus-routed comparison used in the Chapter 3 selective-delegation analysis.

Permitted structured features include:

- direct probability and direct-baseline uncertainty;
- model family, question source, date, and augmentation status;
- the external prediction-market probability frozen at forecast time;
- market uncertainty and direct-model versus market disagreement;
- question length; and
- direct-run token, call, tool-use, parsability, and cost measures.

Question text is supplied only for qualitative error analysis and must not be converted into model features in this group. Group 2 studies text separately. Columns marked `target` or `evaluation_only` must never enter the feature matrix.

The 228 questions are divided chronologically into 151 training, 34 validation, and 43 test questions. All observations for one question remain in the same split. Test outcomes and routed-run results are withheld. Students submit predictions and routing scores for final evaluation against an instructor-held answer key.

## Objectives

The project should answer four questions:

1. How predictable is realized Brier improvement from structured pre-routing signals?
2. Does a learned router outperform a direct-uncertainty threshold selected on development data?
3. Which signals add out-of-sample value beyond direct uncertainty?
4. Does the resulting policy generalize across model families and forecasting sources?

The analysis is predictive rather than causal. Each logged configuration is generally represented by one stochastic realization per model-question pair.

## Suggested work plan

### 1. Audit and reproduce the development data

Verify model coverage, missingness, outcome balance, feature distributions, and the supplied split. Reproduce the uncertainty-versus-improvement relationship on the training and validation observations. Confirm that no test target or evaluation-only field enters preprocessing, model selection, or threshold tuning.

### 2. Establish baselines

Report at least four transparent policies: always stop, always route, random routing at matched routing rates, and a threshold on direct uncertainty. Tune thresholds on training and validation data only. An ex-post oracle may be shown as an unattainable upper reference, but it must not be presented as a feasible policy.

### 3. Develop interpretable models

Students are free to choose methods, but suitable models include ridge or elastic-net regression, logistic regression, shallow decision trees, random forests, and gradient-boosted trees. With only 228 unique questions, model complexity and hyperparameter search should remain limited.

The primary formulation should predict continuous Brier improvement. Useful alternatives include predicting the probability that routing helps, pairwise ranking, or direct optimization of a cost-penalized decision. Compare methods using identical development folds and report calibration as well as discrimination when the prediction is probabilistic.

### 4. Translate predictions into routing decisions

Evaluate both:

- a **cost-penalized rule**, routing when predicted benefit exceeds `lambda` times expected incremental agent cost; and
- a **budget-constrained rule**, ranking questions by predicted benefit per expected cost and routing until a fixed average budget is exhausted.

Sweep the penalty or budget to obtain a quality-cost curve. Agent-side cost is primary because the router controls it. Total pipeline cost should be a secondary sensitivity analysis.

### 5. Evaluate and interpret

Use mean Brier score and mean agent-side cost as the primary policy outcomes. Also report accuracy, log loss, routing rate, rescues, harms, and paired question-level bootstrap intervals. Compare uncertainty-only, market-only, usage-only, and combined feature sets. Use permutation importance, coefficients, or another defensible method to explain out-of-sample predictions.

Robustness checks may include grouped cross-validation within the development sample, leave-one-model-out transfer, and results by source or question date. Avoid selecting the final specification by repeatedly inspecting the held-out test result.

## Freedom and expected contribution

The project fixes the decision problem and evaluation protocol, not the algorithm. A strong project may propose a more suitable loss function, uncertainty treatment, or policy objective. Negative results are scientifically useful if they show that flexible models fail to improve on a simple uncertainty threshold.

The result will establish whether Chapter 3's correlational uncertainty signal can support a practical, interpretable allocation rule. It will also provide a structured baseline for the semantic and multi-budget projects. A convincing held-out gain would motivate prospective evaluation on newly resolved questions; it would not, by itself, establish that routing causally improves outcomes.

## Deliverables

1. Reproducible code and environment instructions.
2. A data audit and leakage-control checklist.
3. The required baselines and at least two justified ML methods.
4. Feature-set ablations and interpretable model analysis.
5. Held-out quality-cost curves with question-level uncertainty intervals.
6. A submission file containing predictions and routing scores for every test model-question pair.
7. A concise report separating established Chapter 3 findings from new results.

The final goal is a defensible answer to whether structured pre-routing signals can improve allocation beyond fixed workflows and direct uncertainty alone.

