# SOHO IDS Relay

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
- `tines/`: Ready-to-import Tines story with multiple LLM examples.

## Requirements

- Suricata for generating alerts in `eve.json`.
- Python 3.x for running scripts.
- An endpoint to receive and process alerts.

## Example Alerts
*In each of the below examples, the raw alert is included in the primary message's 🧵*
  
- Without LLM Processing:

  ![image](https://github.com/user-attachments/assets/bcf820f1-bde9-4e30-80ff-be82b400426e)


- With LLM Processing:
  
  ![image](https://github.com/user-attachments/assets/dfc072e7-81b9-4783-83a9-0fe7a7e7c198)


## License

This project is licensed under the MIT License.
