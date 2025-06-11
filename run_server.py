#!/usr/bin/env python3
"""
Simple launcher for the kwrds.ai MCP server
"""

import sys
import os

# Add the parent directory to the path so we can import our modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from stdio_server import main

if __name__ == "__main__":
    import asyncio
    asyncio.run(main()) 