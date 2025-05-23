from server import mcp
import scanpy as sc
from mofapy2.run.entry_point import entry_point

@mcp.tool()
def run_mofa_from_liana(adata_path: str, out_model: str = "mofa_model.h5ad", factors: int = 10) -> str:
    """
    Run MOFA+ integration on LIANA scores stored in AnnData object.

    Args:
        adata_path: AnnData file with LIANA results.
        out_model: Output file path.
        factors: Number of MOFA+ factors.

    Returns:
        Path to saved MOFA+ model file.
    """
    adata = sc.read_h5ad(adata_path)
    # MOFA expects LIANA scores in a proper data structure
    scores = adata.uns['liana_res'].pivot(index='ligand_complex', columns='receptor_complex', values='magnitude_rank').fillna(0)

    ent = entry_point()
    ent.set_data_matrix([scores])
    ent.set_model_options(factors=factors)
    ent.set_train_options(iter=1000)
    ent.build()
    ent.run()

    adata.obsm["X_mofa"] = ent.model.getFactors()[0]
    adata.write(out_model)
    return out_model
