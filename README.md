# UE Audio Skills

Agent skills for Unreal Engine 5 game audio development. Build complete audio systems spanning **MetaSounds** (DSP), **Blueprints** (game logic), and **Wwise** (mixing) from natural language.

Built for the [UE Audio MCP](https://github.com/koshimazaki/UE5-WWISE) server.

## Install

```bash
npx skills add koshimazaki/ue-audio-skills
```

Install specific skills:

```bash
npx skills add koshimazaki/ue-audio-skills --skill metasound-dsp
npx skills add koshimazaki/ue-audio-skills --skill unreal-bp
npx skills add koshimazaki/ue-audio-skills --skill build-system
npx skills add koshimazaki/ue-audio-skills --skill wwise-setup
npx skills add koshimazaki/ue-audio-skills --skill mcp-plugin
npx skills add koshimazaki/ue-audio-skills --skill add-command
```

## Skills

| Skill | What it does | Requires plugin? |
|-------|-------------|:---:|
| **metasound-dsp** | MetaSounds DSP specialist — 195 nodes across 23 categories, Builder API, signal flow patterns, graph templates | No |
| **unreal-bp** | Blueprint audio logic — game event detection, parameter wiring, asset scanning, audio component patterns | No |
| **build-system** | Full pipeline orchestrator — generates complete MetaSounds + Blueprint + Wwise systems from a single description, 10 audio patterns, AAA project scaffolding | No (offline mode) |
| **wwise-setup** | Wwise project automation via WAAPI — bus hierarchies, RTPCs, switches, events, SoundBanks, AudioLink setup | No (needs Wwise) |
| **mcp-plugin** | TCP plugin control — 42 commands for building MetaSounds graphs, editing Blueprints, spawning audio actors, scanning/exporting assets via the UE5 Editor plugin on port 9877 | Yes |
| **add-command** | Contributor guide — 6-file checklist for adding new C++ TCP commands + Python MCP tool wrappers to the plugin | Yes (source) |

The first four skills work standalone — they provide knowledge, patterns, templates, and WAAPI automation without needing the UE5 Editor plugin. The last two require the [companion plugin](#companion-plugin).

## Companion Plugin

These skills can drive the **[UE Audio MCP Plugin](https://github.com/koshimazaki/UE-AUDIO-MCP)** — a C++ TCP server running inside Unreal Editor with **42 commands** on port 9877:

- **MetaSounds Builder** — create graphs, add nodes, wire connections, set defaults, audition, build to asset
- **Blueprint Builder** — open BPs, add audio function calls, wire event graphs, compile
- **World Audio** — spawn emitters, place audio volumes, import sounds, set physical surfaces, place AnimNotify
- **Query & Export** — list assets, scan blueprints, export full MetaSounds graphs, discover node classes

The plugin is open source and works with UE 5.4+ (tested on 5.7).

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
- [UE Audio MCP](https://github.com/koshimazaki/UE5-WWISE) server (Python, for MCP tools)
- [UE Audio MCP Plugin](https://github.com/koshimazaki/UE-AUDIO-MCP) (C++, for Editor commands — optional)
- Wwise (optional, for full pipeline)

## Compatibility

Works with any AI agent that supports the skills standard:
- Claude Code
- Cursor
- Windsurf
- Codex
- And [35+ other agents](https://skills.sh)
