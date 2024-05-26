---
created: 2024-05-11 11:23:04-07:00
title: Obsidian Graph Analysis Plugin
updated: 2024-05-11 11:27:22-07:00
---

## Summary

An [Obsidian](Obsidian.md) plugin to find hidden connections between vault notes

## Jots

Every PKM should have this functionality, or at least make it easy to extract enough information to analyze externally.

## Analysis Types

 > 
 > **NOTE**
>
 > Extracted from the README

### Co-Citations

Count the number of times two notes are linked in the same note, with extra weight for link proximity within the linking note.

 > 
 > Think of co-citations as a **2nd-order backlinks** panel: Instead of showing *where* something is cited, it shows *why*, or with *whom* or *what* it is cited!

### Similarity

Measure how similar two notes are based on their graph connections.

#### Jaccard Similarity

$$
J(A,B) = \frac{|A \cap B|}{|A \cup B|} = \frac{|A \cap B|}{|A| + |B| - |A \cap B|}
$$

where $|A|$ and $|B|$ are the set of connections (in either direction) for any two pages

[Similarity functions - Neo4j Graph Data Science](https://neo4j.com/docs/graph-data-science/current/algorithms/similarity-functions/#alpha-algorithms-similarity-jaccard-context)

### Link Prediction

Measure the probability that two notes should connect to each other based on their connections in the graph.

#### Adamic Adair

[\[PDF\] Friends and neighbors on the Web | Semantic Scholar](https://www.semanticscholar.org/paper/Friends-and-neighbors-on-the-Web-Adamic-Adar/8dc9d11e3fc229a1b70bb00de72dc15d55848174)

$$
A(x, u) = \sum\_{u \in N(x) \cap N(y)} \frac{1}{\log{|N(u)|}}
$$

where $N(x)$ is the number of neighbors of $x$.

#### Common Neighbors

$$
CN(x,y) = |N(x) \cap N(y)|
$$

where $N(x)$ is the number of neighbors of $x$.

### Community Detection

Try to find groups of similar notes.

#### Label Propagation

 > 
 > Start by giving each node a unique label (its own name). Then, look at each node's neighbours, and change it's label to the most common among it's neighbours. Repeat this process iterations number of times.
 > 
 > At the end, show the nodes grouped by the last label they had.

#### Clustering Coefficient

The ratio of the number of triangles the page is a part of to the number of triangles it possibly could have been part of.

$$
C\_{i} = \frac { |{ e\_{jk} : v\_{j}, v\_{k} \in N\_{i}, e\_{jk} \in E }| } { k\_{i}(k\_{i} - 1) }
$$

## Related

* [GitHub - SkepticMystic/graph-analysis](https://github.com/SkepticMystic/graph-analysis)
  * [Obsidian's Graph Analysis plugin. Algorithms | Medium](https://medium.com/@ensleytan/obsidians-graph-analysis-plugin-c9c107da3331)