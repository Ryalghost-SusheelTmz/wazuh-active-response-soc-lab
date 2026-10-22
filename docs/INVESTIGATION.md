# SOC Level 1 investigation — example

**Illustrative exercise, not a verified historical incident.**

## Scenario
An endpoint sends Wazuh FIM events for a benign file created and edited in the isolated watched folder.

## L1 workflow
1. **Review alert:** record rule ID, UTC time, agent name, observed path, file attributes and hash (if available).
2. **Validate telemetry:** compare with approved test change and look at raw events, not just the alert title.
3. **Scope:** search for repeat activity, other affected files, process context and other endpoints.
4. **Enrich:** compare hash with baselines and optionally VirusTotal under organizational policy. Avoid treating a single reputation label as proof.
5. **Classify:** benign test only when authorized activity is corroborated; otherwise mark unresolved/suspicious.
6. **Escalate:** send relevant details and severity assessment for additional review.
7. **Document:** record evidence, reasoning and next steps.

## Sample escalation template

    Case ID: [ticket]
    Event timestamp UTC: [time]
    Host / agent: [redacted]
    Detection rule: [actual rule ID]
    File / SHA256: [if available]
    Supporting telemetry: [references]
    Related activity: [search scope]
    Confidence & rationale: [notes]
    Action taken: [none / authorized activity]
    Next steps / escalation: [recommended investigation]

Map activity to MITRE ATT&CK only when specific supporting evidence exists. Basic file modification does **not** establish an attack technique.
