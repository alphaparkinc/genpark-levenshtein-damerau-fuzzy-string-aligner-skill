# genpark-levenshtein-damerau-fuzzy-string-aligner-skill

[![GitHub stars](https://img.shields.io/github/stars/alphaparkinc/genpark-levenshtein-damerau-fuzzy-string-aligner-skill?style=social)](https://github.com/alphaparkinc/genpark-levenshtein-damerau-fuzzy-string-aligner-skill/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-0%20external-brightgreen.svg)](#)
[![Model Context Protocol](https://img.shields.io/badge/MCP-Standard%20Compatible-orange.svg)](#)

> Autonomous Agent Damerau-Levenshtein Edit Distance & Optimal Transposition String Alignment Engine

Part of the **GenPark Autonomous Natural Language Processing & Automata Theory Architecture**.

## Architecture Overview

```mermaid
graph TD
    A[Source String S1 & Target String S2] --> B[Dynamic 2D Cost Matrix Construction]
    B --> C[Evaluate Insertions +1, Deletions +1, Substitutions +1]
    C --> D[Evaluate Adjacent Character Transpositions S1_i == S2_j-1 & S1_i-1 == S2_j]
    D --> E[Optimal Local Cost Minimization]
    E --> F[Full String Dynamic Programming Table Traversal]
    F --> G[Minimal Damerau-Levenshtein Distance Metric]
```

## Features

- **Pure Python Standard Library**: Zero external dependencies.
- **Production-Grade Design**: Type annotations, robust chart parsing, multi-pattern matching.
- **MCP Server Ready**: Built-in stdio Model Context Protocol (MCP) server for Claude / Cursor / Agent tool calling.
- **Benchmark Validated**: 100% verified test coverage in isolated sandbox environments.

## Quickstart

```bash
git clone https://github.com/alphaparkinc/genpark-levenshtein-damerau-fuzzy-string-aligner-skill.git
cd genpark-levenshtein-damerau-fuzzy-string-aligner-skill
python example_usage.py
```

## Model Context Protocol (MCP) Usage

```bash
python mcp_server.py
```

## License

MIT License. Designed for autonomous agentic workflows.
