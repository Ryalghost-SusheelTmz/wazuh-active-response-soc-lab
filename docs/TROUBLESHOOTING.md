# Troubleshooting

| Problem | Check |
|---|---|
| Agent offline | Manager address, routing, firewall rules and Wazuh-supported ports |
| Missing FIM alerts | Correct watched path, agent permissions, FIM configuration and Wazuh version |
| Unexpected timestamps | NTP/timezone synchronization and dashboard time filters |
| VirusTotal missing | API key security, integration configuration, quotas and event eligibility |
| No file hashes | Confirm raw event fields; not every event necessarily contains a hash |
| Active Response absent | Trigger, version-specific protocol and permissions; do not test destructive operations prematurely |

Keep snapshots and original logs. Change one setting at a time and record actual results.
