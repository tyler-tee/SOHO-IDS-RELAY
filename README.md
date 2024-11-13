# SOHO IDS

A small office/home office (SOHO) Intrusion Detection System (IDS) project that leverages Suricata to detect potential network threats and uses an LLM to process and analyze alerts via webhook integration.

## Purpose

This project is designed to relay Suricata alerts, captured in `eve.json`, to an external webhook and process the alerts through a Language Model for enhanced analysis and interpretation. This setup allows for more intelligent handling of alerts by reducing noise and prioritizing unique or critical events.

## Features

- **Webhook Integration**: Relays Suricata `eve.json` alerts to an external endpoint.
- **Alert Deduplication**: Only unique alerts are sent to reduce noise and optimize analysis.
- **LLM Processing**: Integrates with an LLM to provide insightful summaries and context for each alert.

## Folder Structure

- `prompts/`: Contains prompt templates for LLM alert processing.
- `scripts/`: Includes scripts for parsing `eve.json` and sending data to the webhook.

## Requirements

- Suricata for generating alerts in `eve.json`.
- Python 3.x for running scripts.
- An endpoint to receive and process alerts.

## License

This project is licensed under the MIT License.
