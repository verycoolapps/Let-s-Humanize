# Software and Technical Craft Playbook

## Improve the code's real job

Establish expected behavior, users, interfaces, constraints, existing conventions, and failure modes before editing. Inspect nearby code and tests first. Prefer a small, reviewable change that fixes the root problem over a rewrite that makes the code look more fashionable.

## Readability and boundaries

- Use names that reveal domain intent; avoid vague buckets and numbered handlers.
- Keep functions focused. Split responsibilities when doing so makes behavior easier to test or change.
- Follow local conventions unless they are the source of a demonstrated problem.
- Comment on non-obvious constraints and reasons, not on lines that already explain themselves.
- Add an abstraction only when it removes real duplication or isolates a change likely to recur.

## Correctness and failure behavior

Check empty input, malformed data, cancellation, timeouts, offline states, duplicate actions, and boundary values that actually matter to this feature. Catch an error only when you can recover, add context, or surface a useful message. Do not silently swallow failure. Validate untrusted input at the boundary and avoid logging secrets or personal data.

Do not invent APIs, package names, flags, or framework behavior. Confirm against repository code, tests, or authoritative documentation; if a detail cannot be checked, state the uncertainty and avoid relying on it.

## Maintainability without ceremony

- Prefer the smallest dependency footprint that meets the requirement.
- Do not build speculative frameworks, configuration systems, or factories around a one-off branch.
- Preserve backward compatibility when callers or persisted data depend on behavior.
- Keep security-sensitive decisions explicit and reviewable.
- Update documentation when a user-visible contract changes.

## Verification ladder

Choose checks proportional to risk:

1. Existing focused unit tests or a minimal reproduction.
2. Type checks, lint, or static analysis relevant to changed files.
3. Integration/build checks for affected boundaries.
4. Manual smoke test for user-visible flows and error states.
5. Security/privacy review for auth, input, storage, network, or logging changes.

Report which checks actually ran and their results. Never say “tested” if only code was inspected. If a test cannot run, explain the blocker and provide the precise command or next verification step.

## Review framing

Prioritize findings by impact and likelihood. For each: give the location, failure scenario, consequence, and a concrete remedy. Distinguish correctness/security defects from style preference. Do not bury a release blocker beneath cosmetic suggestions.

## Example

**Generic review:** “Improve error handling.”

**Useful review:** “If the request times out after the user clicks Save, this handler leaves the button enabled and can create a duplicate record on retry. Disable the action while the request is pending, make the server operation idempotent if supported, and test the timeout/retry path.”

Only recommend idempotency if the actual endpoint and data model support it; otherwise describe the risk and ask for the contract.

## Exercise

Pick one change. Write a short behavior contract with one success case and two realistic failure cases. Find the existing convention and test command. Make the smallest change that meets the contract, then capture the exact verification result.

## Further reading

- Martin Fowler, “Refactoring”: https://refactoring.com/
- Google Engineering Practices, “Code Review Developer Guide”: https://google.github.io/eng-practices/review/
- OWASP Cheat Sheet Series: https://cheatsheetseries.owasp.org/
- Language and framework official documentation for the specific codebase.

These references inform practice; the repository's verified contract and security needs take precedence.