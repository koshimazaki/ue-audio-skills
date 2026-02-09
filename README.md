# UE Audio Skills

Agent skills for Unreal Engine 5 game audio development. Build complete audio systems spanning **MetaSounds** (DSP), **Blueprints** (game logic), and **Wwise** (mixing) from natural language.

Built for the [UE Audio MCP](https://github.com/radeksvarz/UE5-WWISE) server.

## Install

```bash
npx skills add radeksvarz/ue-audio-skills
```

Install specific skills:

```bash
npx skills add radeksvarz/ue-audio-skills --skill mcp-plugin
npx skills add radeksvarz/ue-audio-skills --skill metasound-dsp
npx skills add radeksvarz/ue-audio-skills --skill unreal-bp
npx skills add radeksvarz/ue-audio-skills --skill build-system
```

## Skills

| Skill | What it does |
|-------|-------------|
| **mcp-plugin** | TCP plugin control — 24 commands for building MetaSounds graphs, scanning blueprints, listing assets via the UE5 Editor plugin on port 9877 |
| **metasound-dsp** | MetaSounds DSP specialist — 144 nodes across 20 categories, Builder API, signal flow patterns, graph templates |
| **unreal-bp** | Blueprint audio logic — game event detection, parameter wiring, asset scanning, audio component patterns |
| **build-system** | Full pipeline orchestrator — generates complete MetaSounds + Blueprint + Wwise systems from a single description, 10 audio patterns, AAA project scaffolding |

## Architecture

Three-layer game audio system:

```
Blueprint (WHEN)  →  MetaSounds (WHAT)  →  Wwise (HOW)
Game events          DSP synthesis          Mixing & routing
Parameter wiring     Builder API            RTPC, buses, spatial
Asset scanning       Graph templates        SoundBanks
```

## Requirements

- Unreal Engine 5.4+ (MetaSounds Builder API)
- [UE Audio MCP](https://github.com/radeksvarz/UE5-WWISE) server + C++ plugin
- Wwise (optional, for full pipeline)

## Compatibility

Works with any AI agent that supports the skills standard:
- Claude Code
- Cursor
- Windsurf
- Codex
- And [35+ other agents](https://skills.sh)
