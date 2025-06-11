# kwrds.ai MCP Server

Model Context Protocol server for [kwrds.ai](https://www.kwrds.ai) keyword research and SEO tools.

## Setup

**Requires Python 3.11+**

1. **Get API key** from [kwrds.ai](https://www.kwrds.ai/api/documentation/API_Key_Setup)

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Add to Claude Desktop config** (`~/Library/Application Support/Claude/claude_desktop_config.json`):
   ```json
   {
     "mcpServers": {
       "kwrds-ai": {
         "command": "python3",
         "args": ["/path/to/this/project/run_server.py"],
         "env": {
           "KWRDS_API_KEY": "your-api-key-here"
         }
       }
     }
   }
   ```
   
   **Replace `/path/to/this/project/` with your actual project path**

4. **Restart Claude Desktop**

## Usage

Ask Claude:
- "Find keywords for 'digital marketing' in the US"
- "What does example.com rank for?"
- "Get People Also Ask questions for 'SEO tools'"
- "Generate an SEO outline for 'best laptops 2025'"

## Tools Available

- Keyword research with volumes & competition
- SERP analysis & ranking data
- People Also Ask questions
- AI content generation
- URL ranking analysis
- Usage statistics

## Support

Visit [kwrds.ai](https://www.kwrds.ai) for documentation.# kwrds_ai_mcp
