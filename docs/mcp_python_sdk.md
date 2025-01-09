# Model Context Protocol (MCP) Python SDK

## Overview
The MCP Python SDK provides tools to build MCP servers and clients in Python. It enables seamless integration with LLMs and standardized access to data sources and tools.

## Key Features
- **Server Development**: Build MCP servers to expose data and tools to LLMs.
- **Client Development**: Create MCP clients to connect to MCP servers.
- **Pre-built Integrations**: Use existing integrations for common data sources and tools.
- **Secure Data Access**: Follow best practices for securing data within your infrastructure.

## Installation
```bash
pip install mcp-python-sdk
```

## Quickstart
### Building a Server
```python
from mcp import Server, Resource

class MyServer(Server):
    @Resource
    def my_resource(self):
        return {"data": "example"}

server = MyServer()
server.run()
```

### Building a Client
```python
from mcp import Client

client = Client("http://localhost:8000")
response = client.get_resource("my_resource")
print(response)
```

## AI Pair Programming with Aider

The MCP Python SDK integrates well with Aider, an AI pair programming tool. Key features:

- Edit code in your local git repository
- Works with multiple LLMs (Claude, GPT-4, etc.)
- Automatic git commits with sensible messages
- Supports multiple files and complex changes
- Works with most popular programming languages

### Quickstart
```bash
pip install aider-install
aider-install
aider --model sonnet --anthropic-api-key YOUR_KEY
```

See [Aider Documentation](https://aider.chat/) for more details.

## Documentation
- [GitHub Repository](https://github.com/modelcontextprotocol/python-sdk)
- [API Reference](#) (Link to detailed API docs)
