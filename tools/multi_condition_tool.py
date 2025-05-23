from server import mcp
import liana as li
import scanpy as sc
import pandas as pd
import matplotlib.pyplot as plt

@mcp.tool()
def aggregate_multicondition_liana(h5ad_paths: list, out_ranked_csv: str = "multi_ranked.csv") -> str:
    """
    Aggregate LIANA results from multiple conditions and perform rank aggregation.

    Args:
        h5ad_paths: List of paths to AnnData (.h5ad) files with LIANA results.
        out_ranked_csv: Output path for ranked interactions.

    Returns:
        Path to saved aggregated rankings.
    """
    adatas = [sc.read_h5ad(p) for p in h5ad_paths]
    group_df = li.multi.group_estimates(adatas)
    ranked = li.multi.rank_aggregate(group_df)
    ranked.to_csv(out_ranked_csv, index=False)
    return out_ranked_csv

@mcp.tool()
def plot_multicondition_dotplot(h5ad_paths: list, out_png: str = "multi_dotplot.png") -> str:
    """
    Generate a complex dotplot across conditions for LR interactions.

    Args:
        h5ad_paths: List of paths to AnnData (.h5ad) files.
        out_png: Output PNG path.

    Returns:
        Path to saved plot.
    """
    adatas = [sc.read_h5ad(p) for p in h5ad_paths]
    fig = li.multi.complex_dotplot(adatas)
    fig.savefig(out_png)
    return out_png
