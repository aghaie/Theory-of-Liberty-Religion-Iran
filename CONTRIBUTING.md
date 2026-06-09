# Contributing

This project welcomes contributions from logicians, philosophers, political scientists, formal methods researchers, and anyone interested in computational philosophy.

## What You Can Contribute

### Audit Challenges
Found a flaw in the audit methodology? Identified a counterexample we missed? Open an issue using the **Audit Challenge** template. Challenges must:
- Specify which file and which claim is being challenged
- Provide a formal counterargument (not an assertion)
- Apply equal standards to competing systems

### Competing Systems
Know of a system that might pass the 10-criterion CFS test suite in `audit/phase2_uniqueness/73_cfs_test_suite.json`? Submit it as an issue. We will run it through the full suite and publish results.

### Formalization
If you can translate any kernel axiom or theorem candidate into Lean 4, Coq, or Isabelle, submit a pull request to `scripts/` with your formalization file. Even partial formalizations are valuable.

### Translation
The source text is in Persian. If you can verify or improve the English representation of any claim, open an issue.

### Methodology Improvements
Suggestions for improving the audit methodology, scoring rubrics, or phase design are welcome via the Methodology Question template.

## What This Project Does NOT Accept

- Arguments about whether Islam, religion, or God exists
- Arguments about historical facts in Iran
- Arguments about whether the author's political positions are correct
- Pull requests that modify audit conclusions without full re-running the methodology

The audit is adversarial and structural — not political.

## Opening Issues

Use the templates in `.github/ISSUE_TEMPLATE/`. Plain issues without a template will be triaged.

## Pull Requests

1. Fork the repository
2. Create a branch: `git checkout -b your-contribution`
3. Make your changes
4. Reference the specific file(s) and claim ID(s) in your PR description
5. Submit — PRs are reviewed for methodological consistency, not political alignment

## Code Style (Scripts)

- Python 3.9+
- No external dependencies beyond the standard library + `json`
- All output files must be valid JSON or JSONL
- File naming: `NNN_descriptive_name.json` / `.jsonl` / `.md`

## Questions

Open a Methodology Question issue or start a Discussion.
