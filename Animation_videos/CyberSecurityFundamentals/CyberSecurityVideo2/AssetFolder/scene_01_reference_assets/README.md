# Scene 1 Reference-Broken Asset Pack

Each major visual from the reference asset sheet is provided as an
INDIVIDUAL PNG so Python can load and animate it independently.

Directories:
- icons/       client, API Gateway, ECS, RDS, attacker
- particles/   cyan request, cyan packet, red attack
- rings/       orange active ring, blue active ring
- panels/      orange, purple, blue, red popup frames
- arrows/      cyan, orange, red flow arrows
- reference_crops/ exact source-sheet crops for visual fidelity

The main PNGs preserve the reference visual treatment as much as possible.
The *_glow_core.png files are clean transparent animation layers.

For the actual AWS service icons, continue using the official AWS SVGs
already present in the project. These PNGs are the cinematic treatment
layers and visual reference components.

Recommended Python layering:
background
-> arrow
-> glow_core
-> icon tile / AWS SVG
-> ring
-> particle
-> panel
-> text
