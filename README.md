# Week 03: Multi-Subnet Network Topology & Load Balancer

## Project Overview

This project demonstrates a multi-subnet Docker network using Nginx and two Python Flask backend servers.

## Network Architecture

```text
              Mac / Browser
              localhost:8080
                    |
                    v
       PUBLIC SUBNET 172.28.10.0/24
                    |
            Nginx Load Balancer
                    |
       PRIVATE SUBNET 172.28.20.0/24
              /             \
             v               v
         Backend 1        Backend 2
         Flask:5000       Flask:5000
```

Only Nginx connects to both networks.

The backend servers are connected only to the private subnet and do not publish host ports.

## Technologies

- Docker Compose
- Nginx
- Python Flask
- Docker bridge networking

## Setup Instructions

```bash
docker compose up --build -d
docker compose ps
```

Application URL: http://localhost:8080

## Load Balancing

Nginx uses round-robin to distribute traffic between backend_1 and backend_2.

Test:

```bash
for i in {1..10}; do
  curl -s http://localhost:8080/
  echo
done
```

Observed: Requests alternated between backend_1 and backend_2.

## Failover Test

```bash
docker compose stop backend_1
curl http://localhost:8080/
docker compose start backend_1
```

Expected: When Backend 1 is stopped, Backend 2 continues responding.

## Network Isolation

The backend services do not publish ports to the host.

Verified using:

```bash
docker compose ps
docker port "$(docker compose ps -q backend_1)"
docker port "$(docker compose ps -q backend_2)"
```

Both docker port commands returned no mappings.

Backend 1 was verified to be connected only to private_subnet.

Nginx was verified to be connected to public_subnet and private_subnet.

## Health Check

Command:

```bash
curl -i http://localhost:8080/healthz
```

Observed:

HTTP/1.1 200 OK

Response:

{"server":"backend_1","status":"healthy"}

## AI Disclosure

AI Tool: ChatGPT (OpenAI)

ChatGPT assisted in generating the Docker Compose configuration, Flask application, Nginx configuration, and testing commands.

## AI Configuration Audit

The generated configuration was reviewed for:

1. Backend port exposure.
2. Network segmentation.
3. Load balancer dual-homing.
4. Docker DNS service discovery.
5. Round-robin balancing.
6. Nginx connection timeouts and retry configuration.

The configuration avoids publishing backend ports directly to the host.

No specific initial AI misconfiguration has been demonstrated in this project. The audit focused on checking for potential errors rather than claiming an error was found.

## QA Summary

| Test | Result |
|---|---|
| Round-robin distribution | Passed |
| Backend port publication check | Passed |
| Public/private network membership | Passed |
| HTTP health check | Passed |
| Nginx request logs | Passed |
| Failover | Passed: 10/10 requests returned HTTP 200 from backend_2 |
| Browser DevTools | Pending |

## Cleanup

```bash
docker compose down
```

## Conclusion

This project demonstrates how a load balancer distributes requests between multiple application instances while separating public ingress from private backend services.

Network segmentation reduces direct exposure of application services, while load balancing improves availability and traffic distribution.
