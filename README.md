# 🌌 2-Body Gravity Simulator

A CLI-based physics simulation of gravitational interaction between two bodies, rendered in real-time on a ASCII grid in the terminal.

---

## What It Does

- Places body **A** fixed at the center and body **B** in orbit
- Simulates gravity using **Newton's law of universal gravitation**
- Renders motion on a **40x40 ASCII grid** with a trailing path
- Tracks **kinetic energy, potential energy**, and whether the orbit is bound or unbound
- Detects **collision** and **escape** automatically and stops the simulation
- Offers a **replay** of the full simulation after it ends

---

## Physics

The simulation uses Euler integration at each time step:

- Gravitational force: `F = G * mA * mB / r²`
- Acceleration: `a = F / m`
- Velocity and position updated each tick by `dt`

Energy status is calculated each frame:
- `E < 0` → **Bound** (orbit)
- `E > 0` → **Unbound** (escape trajectory)
- `E = 0` → **Marginally Bound**

---

## Usage

```bash
python 2objectgravity.py
```

You will be prompted to enter:

| Input | Description |
|---|---|
| Mass of B | Mass of the orbiting body |
| Mass of A | Mass of the central body |
| Initial position of B | Starting x-coordinate of B |
| Velocity angle | Direction of initial velocity in degrees (0 = right, 90 = up) |
| Velocity magnitude | Speed of B at start |
| G | Gravitational constant (try `10000` for dramatic effect) |
| dt | Time step (try `0.001` for smooth motion) |

---

## Example Inputs (Circular-ish Orbit)
Mass of B: 10
Mass of A: 1000
Initial position: 100
Velocity angle: 90
Velocity magnitude: 100
G: 10000
dt: 0.01

---

## Controls

- The simulation runs automatically
- Press `Ctrl+C` to stop early
- Stops automatically on collision (`r < 5`) or escape (`r > 1000`)
- After stopping, you can replay the full trajectory

---

## Requirements

Standard library only — no installs needed.
math, time, os

---
