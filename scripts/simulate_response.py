#!/usr/bin/env python3
"""Educational, OFFLINE triage decision demo. No deletion or network actions."""
import argparse
import json

def decide(alert):
    if not isinstance(alert, dict):
        raise TypeError("alert must be a dictionary")
    rule = alert.get("rule") or {}
    try:
        level = int(rule.get("level", 0)) if isinstance(rule, dict) else 0
    except (TypeError, ValueError):
        level = 0
    agent = alert.get("agent") or {}
    host = agent.get("name", "unknown") if isinstance(agent, dict) else "unknown"
    if alert.get("approved_lab_test") is True:
        action = "document_approved_benign_test"
    elif level >= 10:
        action = "escalate_for_human_review"
    else:
        action = "investigate_and_document"
    return {
        "host": host,
        "rule_level": level,
        "recommended_action": action,
        "action_performed": "none",
        "warning": "Not a Wazuh Active Response implementation; analyst validation required."
    }

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--example", action="store_true")
    parser.add_argument("--input", help="Local JSON alert file")
    args = parser.parse_args()
    if not args.example and not args.input:
        parser.error("Supply --example or --input FILE")
    if args.example:
        alert = {"agent": {"name": "demo-agent"}, "rule": {"level": 7},
                 "approved_lab_test": True}
    else:
        with open(args.input, encoding="utf-8") as f:
            alert = json.load(f)
    print(json.dumps(decide(alert), indent=2))

if __name__ == "__main__":
    main()
