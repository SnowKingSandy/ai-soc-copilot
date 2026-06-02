from langgraph.graph import StateGraph

from app.agents.state import (
    IncidentState
)

from app.agents.investigator import (
    investigator_agent
)

from app.agents.risk_agent import (
    risk_agent
)

from app.agents.reporter import (
    reporter_agent
)

builder = StateGraph(
    IncidentState
)

builder.add_node(
    "investigator",
    investigator_agent
)

builder.add_node(
    "risk",
    risk_agent
)

builder.add_edge(
    "investigator",
    "risk"
)

builder.add_node(
    "reporter",
    reporter_agent
)

builder.add_edge(
    "risk",
    "reporter"
)

builder.set_entry_point(
    "investigator"
)

builder.set_finish_point(
    "reporter"
)

graph = builder.compile()