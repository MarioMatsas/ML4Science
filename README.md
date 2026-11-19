# Group 1: structured routing

Start with `data/student/structured_routing.csv` or the equivalent `Data`
worksheet in `structured_routing.xlsx`. The table contains 1,099 model-question
rows over 228 unique questions. Question text is separated into
`question_lookup.csv` for qualitative error analysis and is outside this
group's model feature set.

The predefined split contains 151 training, 34 validation, and 43 test
questions. Every version of a question stays in the same split. Test outcomes,
routed results, and targets are blank in student files. Complete
`submission_template.csv` and return it for evaluation against the private
answer key.

Use only columns marked `pre_routing_feature` in the data dictionary. The
resolved outcome, routed quantities, and derived improvement variables are
targets or evaluation fields. Agent-side cost is the primary policy cost.

The data are derived from the frozen `paired_d0_d2.csv` table behind Chapter
3's selective-delegation analysis. Do not randomly split rows because the same
question appears for several model families.

