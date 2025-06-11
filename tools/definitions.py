"""
MCP Tool Definitions
Defines all available tools and their input schemas for the kwrds.ai API

Read more about kwrds.ai at https://www.kwrds.ai
"""

def get_tool_definitions():
    """Return all available MCP tool definitions"""
    return {
        "keywords_with_volumes": {
            "name": "keywords_with_volumes",
            "description": "Research keywords with search volumes, competition data, and search intent analysis. Returns comprehensive keyword data including volume, CPC, competition, and search intent.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "search_question": {"type": "string", "description": "The main keyword/query to research"},
                    "search_country": {"type": "string", "description": "Country and language code (e.g., 'en-US', 'es-ES', 'fr-FR')"},
                    "api_key": {"type": "string", "description": "Your kwrds.ai API key"},
                    "limit": {"type": "integer", "description": "Limit number of results returned", "minimum": 1},
                    "version": {"type": "string", "description": "API version (default: '1')", "default": "1"}
                },
                "required": ["search_question", "search_country", "api_key"]
            }
        },
        
        "search_volume": {
            "name": "search_volume", 
            "description": "Get search volumes for a list of seed keywords. Returns volume, CPC, competition, and search intent data.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "keywords": {"type": "array", "items": {"type": "string"}, "description": "List of keywords to get volumes for"},
                    "search_country": {"type": "string", "description": "Country and language code (e.g., 'en-US')"},
                    "api_key": {"type": "string", "description": "Your kwrds.ai API key"},
                    "version": {"type": "string", "description": "API version (default: '1')", "default": "1"}
                },
                "required": ["keywords", "search_country", "api_key"]
            }
        },
        
        "serp": {
            "name": "serp",
            "description": "Analyze SERP (Search Engine Results Page) for a keyword. Returns top ranking pages, People Also Search For, and trending queries.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "search_question": {"type": "string", "description": "Keyword to analyze SERP for"},
                    "search_country": {"type": "string", "description": "Country and language code (e.g., 'en-US')"},
                    "api_key": {"type": "string", "description": "Your kwrds.ai API key"},
                    "volume": {"type": "integer", "description": "Search volume (optional)", "default": 0},
                },
                "required": ["search_question", "search_country", "api_key"]
            }
        },
        
        "serp_detailed": {
            "name": "serp_detailed",
            "description": "Get detailed meta tags and SEO information from a specific URL found in SERP results.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "url": {"type": "string", "description": "URL to analyze for meta tags and SEO data"},
                    "api_key": {"type": "string", "description": "Your kwrds.ai API key"},
                },
                "required": ["url", "api_key"]
            }
        },
        
        "ai": {
            "name": "ai",
            "description": "AI-powered keyword research using various prompts like longtail keywords, seed keywords, ecommerce keywords, funnel-based keywords, etc.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "search_question": {"type": "string", "description": "Main keyword/topic for AI analysis"},
                    "search_country": {"type": "string", "description": "Country and language code (e.g., 'en-US')"},
                    "api_key": {"type": "string", "description": "Your kwrds.ai API key"},
                    "prompt": {
                        "type": "string", 
                        "description": "AI prompt type",
                        "enum": [
                            "Get_Longtail_Keywords", "Get_Good_Seed_Keywords", "Get_Bad_Seed_Keywords",
                            "Get_Related_Keywords", "Get_Ecommerce_Keywords", "Get_Best_Keyword_Ideas",
                            "Get_Buy_Keyword_Ideas", "Get_Price_Keyword_Ideas", "Get_Near_me_Keyword_Ideas",
                            "Get_Reviews_Keyword_Ideas", "Get_Broad_Keywords", "Get_Top_of_Funnel_Keywords",
                            "Get_Middle_of_Funnel_Keywords", "Get_Bottom_of_Funnel_Keywords", "Ai_keywords",
                            "Get_Branded_Keywords", "Get_Non_Branded_Keywords"
                        ]
                    }
                },
                "required": ["search_question", "search_country", "prompt", "api_key"]
            }
        },
        
        "ai_content": {
            "name": "ai_content",
            "description": "AI-powered content generation including SEO outlines, 7W1H questions, and meta titles/descriptions.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "search_question": {"type": "string", "description": "Main topic/keyword for content generation"},
                    "search_country": {"type": "string", "description": "Country and language code (e.g., 'en-US')"},
                    "api_key": {"type": "string", "description": "Your kwrds.ai API key"},
                    "prompt": {
                        "type": "string",
                        "description": "Content generation type",
                        "enum": ["Get_SEO_Outline", "Get_7W_1H_Keywords", "Get_Meta_Titles_Descriptions"]
                    },
                    "title": {"type": "string", "description": "Optional title for SEO outline"},
                    "description": {"type": "string", "description": "Optional description for SEO outline"}
                },
                "required": ["search_question", "search_country", "prompt", "api_key"]
            }
        },
        
        "lsi": {
            "name": "lsi",
            "description": "Generate LSI (Latent Semantic Indexing) keywords using AI analysis, SERP analysis, and Google autosuggest data.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "search_question": {"type": "string", "description": "Main keyword for LSI analysis"},
                    "search_country": {"type": "string", "description": "Country and language code (e.g., 'en-US')"},
                    "api_key": {"type": "string", "description": "Your kwrds.ai API key"},
                },
                "required": ["search_question", "search_country", "api_key"]
            }
        },
        
        "url_rankings": {
            "name": "url_rankings",
            "description": "Analyze what keywords a specific URL/domain is ranking for, including ranking positions and estimated traffic.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "url": {"type": "string", "description": "Domain or URL to analyze rankings for (e.g., 'example.com')"},
                    "search_country": {"type": "string", "description": "Country and language code (e.g., 'en-US')"},
                    "api_key": {"type": "string", "description": "Your kwrds.ai API key"},
                },
                "required": ["url", "search_country", "api_key"]
            }
        },
        
        "related_keywords": {
            "name": "related_keywords",
            "description": "Find semantically related keywords that don't necessarily contain the main keyword but are topically relevant.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "search_question": {"type": "string", "description": "Main keyword to find related terms for"},
                    "search_country": {"type": "string", "description": "Country and language code (e.g., 'en-US')"},
                    "api_key": {"type": "string", "description": "Your kwrds.ai API key"},
                    "limit": {"type": "integer", "description": "Limit number of results", "minimum": 1}
                },
                "required": ["search_question", "search_country", "api_key"]
            }
        },
        
        "paa": {
            "name": "paa",
            "description": "Get People Also Ask (PAA) questions for a keyword from Google search results.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "keyword": {"type": "string", "description": "Main search query"},
                    "search_country": {"type": "string", "description": "Country code (e.g., 'US', 'GB')"},
                    "search_language": {"type": "string", "description": "Language code (e.g., 'en', 'es')"},
                    "api_key": {"type": "string", "description": "Your kwrds.ai API key"},
                },
                "required": ["keyword", "search_country", "search_language", "api_key"]
            }
        },
        
        "paa_ai": {
            "name": "paa_ai",
            "description": "AI-powered analysis of People Also Ask (PAA) questions with detailed answers.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "search_question": {"type": "string", "description": "Main search query"},
                    "search_country": {"type": "string", "description": "Country and language code (e.g., 'en-US')"},
                    "question": {"type": "string", "description": "Specific PAA question to analyze"},
                    "prompt": {"type": "string", "description": "Analysis prompt type"},
                    "api_key": {"type": "string", "description": "Your kwrds.ai API key"},
                },
                "required": ["search_question", "search_country", "question", "prompt", "api_key"]
            }
        },
        
        "usage_count": {
            "name": "usage_count",
            "description": "Get current API usage statistics and remaining quotas for the API key.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "api_key": {"type": "string", "description": "Your kwrds.ai API key"},
                },
                "required": ["api_key"]
            }
        }
    } 