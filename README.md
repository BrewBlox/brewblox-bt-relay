# brewblox-bt-relay

Proof of concept for having a separate Docker container that does nothing except relaying Bluetooth commands.
This allows other network traffic to be routed to well-behaved (non-host) containers.

## Getting started

```
bbt-localbuild
docker-compose up
```
