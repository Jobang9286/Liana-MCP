from server import mcp
import liana as li
import scanpy as sc
import matplotlib.pyplot as plt

@mcp.tool()
def plot_targeted_interaction(adata_path: str, ligand: str, receptor: str, out_png: str = "targeted_dotplot.png") -> str:
    """
    Generate a dotplot for targeted ligand-receptor interaction.

    Args:
        adata_path: Path to AnnData file.
        ligand: Ligand gene.
        receptor: Receptor gene.
        out_png: Output PNG path.

    Returns:
        Path to saved image.
    """
    adata = sc.read_h5ad(adata_path)
    fig = li.pl.dotplot(adata, ligand=ligand, receptor=receptor, score='magnitude_rank')
    fig.savefig(out_png)
    return out_png
