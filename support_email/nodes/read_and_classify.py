from typing import Literal
from langgraph.graph import StateGraph, START, END
from langgraph.types import interrupt, Command, RetryPolicy
from langchain.messages import HumanMessage

from support_email.state import EmailAgentState, EmailClassification
from support_email.utils.llm import llm


def read_email(state: EmailAgentState) -> dict:
    """Extract and parse email content"""
    
    # In production, this would connect to the email service
    return {
        "messages": [HumanMessage(content=f"Processing email: {state['email_content']}")]
    }
    
def classify_intent(state: EmailAgentState) -> Command[Literal["search_documentation", "human_review", "draft_response", "bug_tracking"]]:
    """Use LLM to classify email intent and urgency, then route accordingly"""
    
    # Create structured LLM that returns EmailClassification dict 
    structured_llm = llm.with_structured_output(EmailClassification)
    
    # Format the prompt on-demamnd, not stored in state
    classification_prompt = f"""
    Analyze this customer email and classify it:
    
    Email: {state['email_content']}
    From: {state['sender_email']}
    
    Provide classification including intent, urgency, topic and summary.str
    """
    
    # Get structured response directly as dict
    classification = structured_llm.invoke(classification_prompt)
    
    # Determine next node based on classification 
    if classification['intent'] == 'billing' or classification['urgency'] == 'critical':
        goto = "human_review"
    elif classification['intent'] in ['question', 'feature']:
        goto = "search_documentation"
    elif classification['intent'] == "bug":
        goto = "bug_tracking"
    else: 
        goto = "draft_response"

    # Store classification as a single dict in state
    return Command(
        update={"classification": classification},
        goto=goto
    )    
    