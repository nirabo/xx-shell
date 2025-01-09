# Plugin API Reference

## Classes
### Plugin
Base plugin class

```python
class Plugin:
    def __init__(self, name: str, version: str):
        """Initialize plugin with name and version"""
    
    def register_commands(self) -> list[Command]:
        """Register plugin commands"""
    
    def on_load(self):
        """Called when plugin is loaded"""
```

### PluginManager
Manage plugin lifecycle

```python
class PluginManager:
    def __init__(self, shell: Shell):
        """Initialize with reference to shell instance"""
    
    def load_plugin(self, plugin_path: str):
        """Load plugin from specified path"""
    
    def unload_plugin(self, plugin_name: str):
        """Unload plugin by name"""
```

## Functions
### discover_plugins
Discover available plugins

```python
def discover_plugins() -> list[str]:
    """Find available plugins in plugin directories"""
```

### validate_plugin
Validate plugin metadata

```python
def validate_plugin(plugin: Plugin) -> bool:
    """Validate plugin implementation"""
```
