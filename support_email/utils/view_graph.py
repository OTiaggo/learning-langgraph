# Show
from IPython.display import Image, display
from support_email.compile import app

png_bytes = app.get_graph(xray=True).draw_mermaid_png()

with open("support_email/graph.png", "wb") as f:
    f.write(png_bytes)

