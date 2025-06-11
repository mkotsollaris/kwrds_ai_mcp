#!/usr/bin/env python3
"""
MCP Server for kwrds.ai API using stdio transport
Simple, standard implementation following MCP best practices
"""

import asyncio
import json
import os
import sys
from typing import Any, Dict, List, Optional

from mcp import types
from mcp.server import Server
from mcp.server.stdio import stdio_server

from .tools.definitions import get_tool_definitions
from .handlers.keyword_handlers import KeywordHandlers
from .handlers.analysis_handlers import AnalysisHandlers
from .handlers.ai_handlers import AIHandlers


class KwrdsApiMCPServer:
    def __init__(self):
        self.api_base_url = "https://keywordresearch.api.kwrds.ai"
        self.paa_base_url = "https://paa.api.kwrds.ai"
        
        # Get API key from environment
        self.api_key = (
            os.getenv('KWRDS_API_KEY') or 
            os.getenv('API_KEY') or
            os.getenv('KWRDS_AI_API_KEY')
        )
        
        # Initialize handlers
        self.keyword_handlers = KeywordHandlers(self.api_base_url)
        self.analysis_handlers = AnalysisHandlers(self.api_base_url, self.paa_base_url)
        self.ai_handlers = AIHandlers(self.api_base_url)
        
        # Get tool definitions and convert to MCP format
        self.tool_definitions = get_tool_definitions()
        
        # Create the MCP server
        self.server = Server("kwrds-ai")

    def setup_server(self):
        """Setup MCP server with tools and handlers"""
        
        @self.server.list_tools()
        async def list_tools() -> List[types.Tool]:
            """List all available tools"""
            tools = []
            for tool_def in self.tool_definitions.values():
                tools.append(types.Tool(
                    name=tool_def["name"],
                    description=tool_def["description"],
                    inputSchema=tool_def["inputSchema"]
                ))
            return tools

        @self.server.call_tool()
        async def call_tool(name: str, arguments: Dict[str, Any]) -> List[types.TextContent]:
            """Handle tool calls"""
            try:
                if not self.api_key:
                    raise ValueError("API key not found. Please set KWRDS_API_KEY environment variable.")
                
                # Route to appropriate handler
                result = await self._route_tool_call(name, arguments)
                
                # Return result as text content
                return [types.TextContent(
                    type="text",
                    text=json.dumps(result, indent=2, ensure_ascii=False)
                )]
                
            except Exception as e:
                error_result = {"error": str(e), "tool": name, "arguments": arguments}
                return [types.TextContent(
                    type="text", 
                    text=json.dumps(error_result, indent=2)
                )]

    async def _route_tool_call(self, tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Route tool calls to appropriate handlers"""
        
        # Keyword research tools
        if tool_name == "keywords":
            return self.keyword_handlers.handle_keywords(arguments, self.api_key)
        elif tool_name == "keywords_with_volumes":
            return self.keyword_handlers.handle_keywords_with_volumes(arguments, self.api_key)
        elif tool_name == "search_volume":
            return self.keyword_handlers.handle_search_volume(arguments, self.api_key)
        elif tool_name == "related_keywords":
            return self.keyword_handlers.handle_related_keywords(arguments, self.api_key)
        elif tool_name == "lsi":
            return self.keyword_handlers.handle_lsi(arguments, self.api_key)
            
        # Analysis tools
        elif tool_name == "serp":
            return self.analysis_handlers.handle_serp(arguments, self.api_key)
        elif tool_name == "serp_detailed":
            return self.analysis_handlers.handle_serp_detailed(arguments, self.api_key)
        elif tool_name == "url_rankings":
            return self.analysis_handlers.handle_url_rankings(arguments, self.api_key)
        elif tool_name == "paa":
            return self.analysis_handlers.handle_paa(arguments, self.api_key)
        elif tool_name == "paa_ai":
            return self.analysis_handlers.handle_paa_ai(arguments, self.api_key)
        elif tool_name == "usage_count":
            return self.analysis_handlers.handle_usage_count(arguments, self.api_key)
            
        # AI tools
        elif tool_name == "ai":
            return self.ai_handlers.handle_ai(arguments, self.api_key)
        elif tool_name == "ai_content":
            return self.ai_handlers.handle_ai_content(arguments, self.api_key)
            
        else:
            raise ValueError(f"Unknown tool: {tool_name}")

    async def run(self):
        """Run the MCP server"""
        self.setup_server()
        
        async with stdio_server() as streams:
            await self.server.run(
                streams[0],
                streams[1],
                self.server.create_initialization_options()
            )


async def main():
    """Main entry point"""
    server = KwrdsApiMCPServer()
    await server.run()


if __name__ == "__main__":
    asyncio.run(main()) 