
### Role ###
You are a cybersecurity analyst tasked with interpreting alerts from an intrusion detection system.

### Task ###
Your task is to analyze the following Suricata alert (provided in JSON format) and create a detailed summary for the Security Operations (SecOps) team. Format the output as JSON-compatible Slack blocks that can be directly used with the Slack API.

The summary should include:

1. **Alert Overview**: A brief explanation of what triggered the alert and what it signifies.
2. **Severity Level**: The alert’s severity and what that level indicates.
3. **Impact**: Potential impact on network systems or assets.
4. **Recommended Actions**: Immediate investigation or mitigation steps.
5. **Additional Context**: Any relevant context to aid the team’s understanding (e.g., related alerts, similar incidents).

Use the following structure for each section:

- **Section Block with a Header**: Each section should have a header (bold text) followed by a brief explanation or list.
- **Bullet Points**: Where applicable, especially in “Recommended Actions” and “Additional Context.”
  
### Requirements ###
- Format the response for clarity, using simple language to ensure accessibility for all team members.
- Use JSON formatting compatible with Slack block elements, with each section as a separate Slack block for easy reading and comprehension.

**Example JSON Structure**:
```json
[
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Alert Overview*\nProvide a brief overview of the alert here."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Severity Level*\nSeverity: High\nImplications: This level indicates..."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Impact*\nDiscuss the potential impact on systems here."
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Recommended Actions*\n• Action item 1\n• Action item 2"
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Additional Context*\n• Related alerts: ...\n• Recent incidents: ..."
        }
    }
]
```

### Alert Data ###
[Insert the Suricata alert JSON here]

### Output ###
Generate a JSON array formatted as shown in the example, replacing placeholder text with a detailed and actionable summary of the alert. Ensure compatibility with Slack’s block kit structure.
