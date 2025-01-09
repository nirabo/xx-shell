# Model Context Protocol (MCP) Specification

## Overview
MCP is an open protocol that standardizes how applications provide context to LLMs. It follows a client-server architecture and enables flexible integration with data sources and tools.

## Core Concepts
### Architecture
- **MCP Hosts**: Applications like Claude Desktop or IDEs that use MCP.
- **MCP Clients**: Protocol clients that connect to MCP servers.
- **MCP Servers**: Lightweight programs exposing capabilities through MCP.
- **Local Data Sources**: Files, databases, and services accessible by MCP servers.
- **Remote Services**: External systems (e.g., APIs) connected via MCP.

### Resources
- Expose data and content from servers to LLMs.
- Defined using the `@Resource` decorator in the Python SDK.

### Prompts
- Reusable prompt templates and workflows.
- Enable consistent interactions with LLMs.

### Tools
- Allow LLMs to perform actions through servers.
- Examples: API calls, database queries, file operations.

### Sampling
- Servers can request completions from LLMs.
- Supports dynamic context generation.

### Transports
- Communication mechanism between clients and servers.
- Supports HTTP, WebSocket, and other protocols.

## Specification Details
- [Full Specification](https://spec.modelcontextprotocol.io)
- [GitHub Repository](https://github.com/modelcontextprotocol)
