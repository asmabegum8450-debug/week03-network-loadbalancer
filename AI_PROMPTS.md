# AI Prompt Log

AI Tool: ChatGPT (OpenAI)

## User Prompts

1. "now do this"
2. "do it fro. begging step by steop"
3. "do all this from terminal"

## AI Assistance

ChatGPT generated:
- Python Flask backend code
- Dockerfile and dependencies
- Nginx reverse-proxy configuration
- Docker Compose network topology
- Terminal commands for QA testing

## AI Audit

The configuration was checked for backend port exposure, dual-homed load balancing, Docker DNS resolution, and timeout/retry behavior.

No confirmed initial configuration flaw was found. The generated configuration was validated through Docker Compose and live testing.

## Reflection

AI-generated infrastructure should be checked rather than trusted automatically. Testing confirms whether network separation and load distribution actually work.
