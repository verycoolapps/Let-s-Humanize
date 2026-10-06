# Visual and Product Design Playbook

## Design for a task, not a screenshot

Identify the person, context, primary task, device, constraints, and highest-cost failure. A page that looks distinctive but hides the action is not successful. Begin with information and interaction hierarchy; choose a visual direction after you know what must be understood first.

## Make a specific visual decision

Name an aesthetic direction in concrete terms and explain its fit: editorial typography, industrial utility, warm craft, or another intentional system. Set a small, coherent palette and typography hierarchy. Resist default template formulas—centered slogan, three identical cards, decorative icons—unless the content genuinely calls for them. Avoid purple-blue gradients, glow, and glass effects by default; use them only when they have a defensible product reason.

## Hierarchy and composition

- Give the primary action or fact the strongest visual position.
- Use size, weight, spacing, alignment, and contrast together; color alone is not hierarchy.
- Let density follow content. Use whitespace to separate ideas, not merely to make an empty interface look expensive.
- Keep one consistent icon and illustration language. Do not use emoji as a substitute for a designed icon system.
- Test the smallest supported viewport early. Mobile is a real layout, not a squeezed desktop.

## Interaction is part of the design

Specify behavior and appearance for:

- default, hover, focus-visible, pressed, disabled, selected;
- loading, success, empty, validation, network error, and destructive confirmation;
- keyboard navigation, touch targets, reduced motion, and screen-reader labels.

A control should look interactive only when it works. A blank empty state should explain the next step without inventing sample user data. Error text should say what happened and what the user can do.

## Accessibility checks

Use WCAG 2.2 AA as a practical baseline, while checking the requirements applicable to the product and jurisdiction. Do not rely on color alone to signal meaning. Check contrast for text and controls, semantic structure, visible focus, logical reading and tab order, keyboard operation, zoom/reflow, form labels, and reduced-motion behavior. Validate with tools and manual keyboard/screen-reader review; automated scans cannot prove accessibility.

## Design critique format

For each high-priority issue, state: **observation → user impact → recommended change → verification**. Separate usability blockers from aesthetic preference. Preserve what already works. When suggesting a visual change, name the component, state, and intended user effect; “make it modern” is not an actionable critique.

## Example

**Observation:** The main action has the same contrast and size as four secondary links.

**Impact:** A first-time visitor must scan the whole page to find how to start.

**Change:** Give the primary action one unmistakable button treatment and place it next to the decision context; retain secondary navigation as text links.

**Verify:** On a narrow viewport, keyboard through the page and confirm that the action is discoverable and focus is visible.

## Exercise

Choose one real screen and draw a grayscale hierarchy map before changing color. Mark the first five elements a user should notice. Then inspect each interactive state and use keyboard-only navigation. Fix the task hierarchy or missing states before adding polish.

## Further reading

- W3C, Web Content Accessibility Guidelines (WCAG) 2.2: https://www.w3.org/TR/WCAG22/
- W3C WAI, “Designing for Web Accessibility”: https://www.w3.org/WAI/tips/designing/
- Nielsen Norman Group, usability heuristics: https://www.nngroup.com/articles/ten-usability-heuristics/

Check current standards and product-specific requirements; this playbook is not a substitute for an accessibility audit.