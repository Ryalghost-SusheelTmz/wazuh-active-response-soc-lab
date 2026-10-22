# Step-by-step Wazuh SOC lab build

> Educational reconstruction based on Sushil Tamang's original lab experience. Validate exact software versions and network details locally. Work only in isolated, authorized VMs.

## 1. Prepare the environment
Create VMware VMs for pfSense, Wazuh server, a Windows endpoint and a Linux endpoint. Use an isolated virtual network and snapshots. Do not expose Wazuh dashboard or vulnerable lab systems publicly.

## 2. Configure pfSense
Place lab endpoints in a dedicated LAN/VLAN and assign private addresses for your actual subnet. Restrict ingress and unnecessary outbound connections. Permit only vendor-documented Wazuh communication ports.

## 3. Install Wazuh
Use the official installation instructions: https://documentation.wazuh.com/current/installation-guide/index.html . Document your installed Wazuh version, OS, memory/CPU allocation and manager address. Protect admin credentials.

## 4. Deploy agents
Use the Wazuh dashboard's agent deployment instructions to enroll Windows and Linux systems. Confirm each agent is healthy and logs arrive with synchronized timestamps. Save a redacted dashboard screenshot.

## 5. Configure FIM
Merge the sample at [../config/agent-fim-4x.xml](../config/agent-fim-4x.xml) into the Linux agent's existing configuration. This is only a fragment, not a complete ossec.conf. Use an authorized directory exclusively for testing and adjust the sample path.

## 6. Test harmless file events
On the isolated Linux agent create, edit and delete a harmless text file in the monitored directory. Inspect Wazuh FIM rule, timestamp, agent, path and hash information. Save genuine evidence; do not invent events.

## 7. Optional VirusTotal enrichment
Read the Wazuh integration documentation before configuring the Wazuh manager. See [../config/virustotal-manager-4x.xml](../config/virustotal-manager-4x.xml) for a sample fragment. Never commit the API key. A reputation result is only one triage signal.

## 8. Safe response validation
Start with the non-destructive [response simulator](../scripts/simulate_response.py) and tests. This is **not** a functioning Wazuh Active Response integration and it performs no deletion. A real response requires the version-specific Wazuh command protocol, safe allowlists, approval, evidence preservation and rollback.

## 9. Report
Complete the [investigation example](INVESTIGATION.md), [validation checklist](VALIDATION.md) and attach sanitized actual screenshots. Document limitations as well as successes.
