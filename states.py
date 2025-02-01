# This stores the states of the agents

import operator
from dataclasses import dataclass, field
from typing_extensions import TypedDict, Annotated

# Dataclass SummaryState stores the research_topic, search_query, web_research_results, sources_gathered, research_loop_count, and running_summary
@dataclass(kw_only=True)
class SummaryState:
    research_topic: str = field(default=None)     
    search_query: str = field(default=None) 
    web_research_results: Annotated[list, operator.add] = field(default_factory=list) 
    sources_gathered: Annotated[list, operator.add] = field(default_factory=list) 
    research_loop_count: int = field(default=0) 
    running_summary: str = field(default=None) 

# Dataclass SummaryStateInput stores the research_topic
@dataclass(kw_only=True)
class SummaryStateInput:
    research_topic: str = field(default=None)    

# Dataclass SummaryStateOutput stores the running_summary
@dataclass(kw_only=True)
class SummaryStateOutput:
    running_summary: str = field(default=None) 