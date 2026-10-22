# Original Wazuh lab screenshot evidence

The screenshots referenced in this repository were supplied by Sushil Tamang from the original controlled lab. Each image documents a different part of the workflow. The screenshots are not synthetic recreations.

| File | Evidence |
|---|---|
| 01-network-architecture.jpg | Financial-enterprise lab topology design with pfSense / VMware |
| 02-wazuh-manager-service.png | Wazuh manager service active in terminal |
| 03-wazuh-dashboard-overview.png | Overview of security monitoring dashboard |
| 04-agent-inventory.png | LinuxUser active and Windows endpoint disconnected |
| 05-linux-security-assessment.png | Linux vulnerability and CIS configuration assessment, FIM activity |
| 06-windows-agent-inventory.png | Windows endpoint disconnected and security assessment |
| 07-fim-events.png | FIM add/remove logs (rules 554 and 553) |
| 08-virustotal-eicar.png | VirusTotal EICAR detection 65/67 |
| 09-threat-hunting-timeline.png | Related VirusTotal, FIM and response log timeline |
| 10-active-response-config.png | Custom rule 87105 and ossec.conf configuration |
| 11-active-response-script.png | Original remove-threats.sh editor screenshot |
| 12-active-response-evidence.png | Active Response log reporting successful file removal |
| 13-mitre-attack-mapping.png | Wazuh ATT&CK-mapped alert display |

## Screenshot upload

The 13 images are packaged separately in `Wazuh_Actual_Screenshots_Ready_For_GitHub.zip`, to be uploaded to this `screenshots/` directory. Before public upload, inspect for sensitive details and remove tokens, personal/private data, credentials and anything not intended for public disclosure.

Once uploaded, the main README and project guides will display the original evidence in place.
