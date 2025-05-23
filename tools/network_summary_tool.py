from server import mcp
import liana as li
import scanpy as sc
import pandas as pd

@mcp.tool()
def summarize_c2c_network(adata_path: str, score: str = "magnitude_rank", method: str = "mean", out_path: str = "cell_network.csv") -> str:
    """
    Summarize cell-cell interaction network as adjacency matrix.

    Args:
        adata_path: Path to AnnData (.h5ad) with liana results.
        score: Score column to use.
        method: Aggregation method.
        out_path: Output CSV file.

    Returns:
        Path to saved network CSV.
    """
    adata = sc.read_h5ad(adata_path)
    df = li.get_ccc_matrix(adata, score=score, how=method)
    df.to_csv(out_path)
    return out_path
