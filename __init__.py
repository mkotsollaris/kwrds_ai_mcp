"""
MCP (Model Context Protocol) Server Implementation for https://www.kwrds.ai
==================================================

This package provides MCP server functionality for the kwrds.ai API.
It exposes all API endpoints as MCP tools that can be used by AI assistants
and other MCP-compatible clients.

Features:
- API key authentication
- Comprehensive tool definitions
- Error handling and validation
- Standard MCP stdio protocol

Read more about kwrds.ai at https://www.kwrds.ai
"""

from .stdio_server import KwrdsApiMCPServer

__all__ = ['KwrdsApiMCPServer'] 