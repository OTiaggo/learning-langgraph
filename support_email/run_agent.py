from langgraph.types import Command

from support_email.compile import app

# Test with an urgent billing issue 
initial_state = {
    "email_content": "I was charged twice for my description! This is urgent!",
    "sender_email": "customer@example.com",
    "email_id": "email_123",
    "messages": []
}

# Run with a thread_id for persistence
config = {"configurable": {"thread_id": "customer_123"}}
result = app.invoke(initial_state, config)

# The graph will pause at human_review
print(f"Human review interrupt: {result["__interrupt__"]}")


# When ready, provide human input to resume 
human_response = Command(
    resume={
        "approved": True,
        "edited_response":  "We sincerely apologize for the double charge. I've initiated an immediate refund..."
    }
)


# Resume execution 
final_result = app.invoke(human_response, config)
print(f"Email sent succesfully!")