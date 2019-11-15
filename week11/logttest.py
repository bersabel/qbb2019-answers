#!/usr/bin/env python3

import scanpy.api as sc
import seaborn as sns
import umap as umap

# Read 10x dataset
adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
# Make variable names (in this case the genes) unique
adata.var_names_make_unique()

sc.pp.filter_genes(adata, min_counts = 1) #only consider genes with more than 1 count
sc.pp.normalize_per_cell(adata, key_n_counts = 'n_counts_all') #normalize with total UMI count per cell

filter_result = sc.pp.filter_genes_dispersion(adata.X, flavor = 'cell_ranger', n_top_genes=1000, log = False)

adata = adata[:, filter_result.gene_subset] #filter genes
sc.pp.normalize_per_cell(adata)  # need to redo normalization after filtering
sc.pp.log1p(adata)
sc.pp.scale(adata)

sc.pp.neighbors(adata)
sc.tl.louvain(adata,  resolution = 0.3)    
sc.tl.umap(adata)


# sc.pl.umap(adata,color = ["louvain", "Igfbpl1", "Dbi", "Stmn2", "Nrxn3", "mt-Atp6", "Islr2", "Nrxn3", "Hbb-bs", "Sparc", "Reln", "Rgs5"], legend_loc='on data')
# sc.tl.rank_genes_groups(adata, 'louvain', method = 't-test')
# sc.pl.rank_genes_groups(adata)


# sc.pl.umap(adata,color = ["louvain", "Igfbpl1", "Dbi", "Stmn2", "Nrxn3", "mt-Atp6", "Islr2", "Nrxn3", "Hbb-bs", "Sparc", "Reln", "Rgs5"], legend_loc='on data')
#
# sc.pl.umap(adata,color = ["louvain", "Malat1", "Ccna2", "mt-Atp6", "Lhx6", "mt-Cytb", "Zbtb20", "Npas1", "Ftl1", "Trem2", "Reln", "Col3a1"], legend_loc='on data')

T-test

1. Igfbpl1- Granule neuroblasts, dentate gyrus -Telencephalon
2. Dbi Mus musculus diazepam binding inhibitor (Dbi)
3. Stmn2 Excitatory neurons, cerebral cortex
4. Nrxn3 Excitatory neurons, cerebral cortex
5. mt-Atp6 Cholinergic enteric neurons
6. Islr2 Mus musculus immunoglobulin superfamily containing leucine-rich repeat 2 (Islr2)
7. Nrxn3 Excitatory neurons, cerebral cortex
8. Hbb-bbs Mus musculus hemoglobin, beta adult s chain (Hbb-bs)
9. Sparc Cholinergic enteric neurons
10. Reln Mus musculus reelin (Reln)
11. Rgs5 Mus musculus regulator of G-protein signaling 5 (Rgs5)



logreg


1. Malat1 us musculus metastasis associated lung adenocarcinoma transcript 1 (non-coding RNA) (Malat1), long non-coding RNA Excitatory neurons, cerebral cortex
2. Ccna2 Mus musculus cyclin A2 (Ccna2) Neuronal intermidate progenitor cells
3. mt-Atp6 Cholinergic enteric neurons
4.lhx6 Mus musculus LIM homeobox protein 6 (Lhx6)
5. mt-Cytb Afferent nuclei of cranial nerves VI-XII
6. Zbtb20 Mus musculus zinc finger and BTB domain containing 20 (Zbtb20)
7. Npas1 Mus musculus neuronal PAS domain protein 1 (Npas1)
8.Ftl1 Mus musculus ferritin light polypeptide 1 (Ftl1) 
9. Trem2 Mus musculus triggering receptor expressed on myeloid cells 2 (Trem2)
10. Reln Mus musculus reelin (Reln)
11.Col3a1 Mus musculus collagen, type III, alpha 1 (Col3a1)


















