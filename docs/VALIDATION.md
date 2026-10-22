# Validation and evidence checklist

| Test | Expected observation | Evidence needed |
|---|---|---|
| Agents | Manager recognizes monitored endpoints | Actual redacted agent list |
| FIM create | Alert showing new test file | Sanitized event JSON and dashboard |
| FIM edit/delete | File change/remove activity | Actual time-ordered alerts |
| VirusTotal (optional) | Hash enrichment or documented limitation | Redacted integration result |
| Security assessment | Wazuh policy findings | Real SCA output |
| Active response | Controlled response workflow | Verified action and rollback evidence |

## Measuring response latency

The original project reported file removal in under two seconds in a controlled test. That is **not** a benchmark validated by this repository. To reproduce, precisely log event time, alert processing time, response start time, confirmed completion time and clock synchronization. Repeat trials; report median and range.

| Trial | Event UTC | Alert UTC | Action start UTC | Completion UTC | Outcome |
|---|---|---|---|---|---|
| 1 | pending | pending | pending | pending | unverified |
| 2 | pending | pending | pending | pending | unverified |

Never confuse script runtime with full event-to-containment latency.
