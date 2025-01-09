# XX Shell Mode MCP Integration Guide

## Overview
This guide explains how to integrate MCP with XX Shell Mode, including server management, client integration, and plugin development.

## Server Management
### Starting a Server
```bash
xx mcp start --config ~/.xx/mcp/my_server.yaml
```

### Stopping a Server
```bash
xx mcp stop my_server
```

### Listing Servers
```bash
xx mcp list
```

## Client Integration
### Connecting to a Server
```bash
xx mcp connect http://localhost:8000
```

### Executing Queries
```bash
xx mcp query my_resource
```

### Listing Resources
```bash
xx mcp resources
```

## Plugin Development
### Creating a Plugin
```python
from xx_shell.plugins import MCPPlugin
from mcp import Resource

class MyPlugin(MCPPlugin):
    @Resource
    def my_resource(self):
        return {"data": "example"}
```

### Registering Resources
```python
class MyPlugin(MCPPlugin):
    def register_resources(self):
        self.register_resource("my_resource", self.my_resource)
```

### Error Handling
```python
class MyPlugin(MCPPlugin):
    def handle_error(self, error):
        self.log.error(f"Error in plugin: {error}")
```

## Session Management
### Saving Session State
```bash
xx session save
```

### Loading Session State
```bash
xx session load
```

### Listing Sessions
```bash
xx session list
```

## Documentation
- [MCP Python SDK Guide](docs/mcp_python_sdk.md)
- [MCP Specification](docs/mcp_specification.md)
- [XX Shell Documentation](docs/xx_shell.md)
# XX Shell Mode MCP Integration Guide

## Overview
This guide explains how to integrate MCP with XX Shell Mode, including server management, client integration, and plugin development.

## Server Management
### Starting a Server
```bash
xx mcp start --config ~/.xx/mcp/my_server.yaml
```

### Stopping a Server
```bash
xx mcp stop my_server
```

### Listing Servers
```bash
xx mcp list
```

## Client Integration
### Connecting to a Server
```bash
xx mcp connect http://localhost:8000
```

### Executing Queries
```bash
xx mcp query my_resource
```

### Listing Resources
```bash
xx mcp resources
```

## Plugin Development
### Creating a Plugin
```python
from xx_shell.plugins import MCPPlugin
from mcp import Resource

class MyPlugin(MCPPlugin):
    @Resource
    def my_resource(self):
        return {"data": "example"}
```

### Registering Resources
```python
class MyPlugin(MCPPlugin):
    def register_resources(self):
        self.register_resource("my_resource", self.my_resource)
```

### Error Handling
```python
class MyPlugin(MCPPlugin):
    def handle_error(self, error):
        self.log.error(f"Error in plugin: {error}")
```

## Session Management
### Saving Session State
```bash
xx session save
```

### Loading Session State
```bash
xx session load
```

### Listing Sessions
```bash
xx session list
```

## Documentation
- [MCP Python SDK Guide](mcp_python_sdk.md)
- [MCP Specification](mcp_specification.md)
- [XX Shell Documentation](index.md)
