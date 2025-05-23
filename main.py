from server import mcp

# Import all LIANA MCP tools
from tools.basic_liana_tool import run_basic_liana
from tools.network_summary_tool import summarize_c2c_network
from tools.targeted_plot_tool import plot_targeted_interaction
from tools.mofa_integration_tool import run_mofa_from_liana
from tools.multi_condition_tool import aggregate_multicondition_liana, plot_multicondition_dotplot

if __name__ == "__main__":
    mcp.run()
