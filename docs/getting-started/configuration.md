# Configuration

## Configuration Files
XX Shell uses the following configuration files:
- `~/.xx/config.yaml`: Main configuration file
- `~/.xx/plugins/`: Directory for plugin configurations
- `~/.xx/sessions/`: Directory for session files

## Basic Configuration
Example configuration file:
```yaml
# ~/.xx/config.yaml
core:
  prompt: "xx> "
  history_size: 1000
  auto_update: true

ui:
  theme: dark
  syntax_highlighting: true
  show_line_numbers: true

plugins:
  enabled:
    - mcp
    - git
    - docker
```

## Environment Variables
You can override configuration settings using environment variables:
- `XX_PROMPT`: Override the shell prompt
- `XX_THEME`: Set the UI theme (light/dark)
- `XX_HISTORY_SIZE`: Set command history size
- `XX_AUTO_UPDATE`: Enable/disable auto-update

## Plugin Configuration
Each plugin can have its own configuration file:
```yaml
# ~/.xx/plugins/mcp.yaml
mcp:
  servers:
    - name: local
      url: http://localhost:8000
    - name: production
      url: https://mcp.example.com
```

## Session Configuration
Session-specific settings can be stored in session files:
```yaml
# ~/.xx/sessions/default.yaml
environment:
  variables:
    API_KEY: "your-api-key"
  working_directory: "/projects/my-project"
```

## Reloading Configuration
To reload configuration without restarting:
```bash
xx-shell config reload
```
