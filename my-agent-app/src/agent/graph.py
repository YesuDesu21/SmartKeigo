# src/agent/graph.py
from langgraph.graph import StateGraph, START, END
from .state import KeigoState
from .agent import language_analyzer, keigo_specialist, cultural_coach

# 1. Initialize the Graph
builder = StateGraph(KeigoState)

# 2. Register Nodes
builder.add_node("analyzer_node", language_analyzer)
builder.add_node("specialist_node", keigo_specialist)
builder.add_node("coach_node", cultural_coach)

# 3. Create Fixed Structural Edges
builder.add_edge(START, "analyzer_node")
builder.add_edge("analyzer_node", "specialist_node")
builder.add_edge("specialist_node", "coach_node")

# 4. Create the Loop Condition (Conditional Edge)
def route_approval(state: KeigoState):
    if state["is_approved"] == True:
        return "approved"
    else:
        return "rejected"

# If approved -> End the script. If rejected -> Route back to the Specialist
builder.add_conditional_edges(
    "coach_node",
    route_approval,
    {
        "approved": END,
        "rejected": "specialist_node"
    }
)

# 5. Compile everything into an executable app object
keigo_app = builder.compile()