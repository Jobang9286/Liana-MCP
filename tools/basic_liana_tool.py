from server import mcp
import liana as li
import scanpy as sc

@mcp.tool()
def run_basic_liana(adata_path: str, groupby: str = "cell_type", out_path: str = "liana_basic_results.csv") -> str:
    """
    Run LIANA's rank_cci to infer cell-cell interactions.

    Args:
        adata_path: Path to AnnData (.h5ad) file.
        groupby: Column in adata.obs to group by.
        out_path: Output CSV path.

    Returns:
        Path to saved CSV with CCI results.
    """
    adata = sc.read_h5ad(adata_path)
    li.tl.rank_cci(adata, groupby=groupby)
    adata.uns['liana_res'].to_csv(out_path, index=False)
    return out_path
