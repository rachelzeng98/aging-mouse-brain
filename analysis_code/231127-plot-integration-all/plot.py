import pathlib
import joblib
import anndata
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from ALLCools.integration import calculate_overlap_score, confusion_matrix_clustering
from ALLCools.plot import *


mc_cat_key = "AgingMajorType"
atac_cat_key = "celltype_final"


os_mat = pd.read_hdf(f"ATAC-{atac_cat_key}.mC-{mc_cat_key}.overlap_score.hdf", key="data")

(
    query_group,
    ref_group,
    confusion_matrix,
    g,
    modularity_score,
) = confusion_matrix_clustering(
    confusion_matrix=os_mat,
    min_value=0.1,
    max_value=0.9,
    partition_type=None,
    resolution=1,
    seed=0,
)
print(f"Modularity: {modularity_score:.3f}")

confusion_matrix.to_csv('confusion_matrix.csv')
fig, ax = plt.subplots(figsize=(6, 6), dpi=200)
sns.heatmap(confusion_matrix, ax=ax, vmin=0.1, vmax=0.9, cbar=None)