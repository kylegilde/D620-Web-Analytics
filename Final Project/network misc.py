import networkx as nx
from networkx import bipartite as bi

dtm_col_indices_to_keep = np.in1d(unigram_feature_names, top_terms.feature_name)
words = list(np.extract(dtm_col_indices_to_keep, unigram_feature_names))

unigram_dtm_top_terms = unigram_dtm[:, dtm_col_indices_to_keep]
zero_rows_to_remove = np.all(np.equal(unigram_dtm_top_terms.toarray(), 0), axis=1)
unigram_tdm_top_terms = np.transpose(unigram_dtm_top_terms[~zero_rows_to_remove])

bipartite_g = bi.from_biadjacency_matrix(unigram_tdm_top_terms,
                                               edge_attribute='tfidf')
bipartite_g.add_nodes_from(words, bipartite=0)
# weighted_projected_graph
word_g = bi.weighted_projected_graph(bipartite_g, words)


pos = nx.spring_layout(word_g)
nx.draw_networkx_edges(word_g, pos, alpha=.3)
nx.draw_networkx_labels(word_g, pos, words, font_size=14)
plt.title('Word Graph', size=14)
plt.show()
