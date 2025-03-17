# Classify

Types:

```python
from Deasy.types import ClassifyClassifyFilesResponse
```

Methods:

- <code title="post /classify">client.classify.<a href="./src/Deasy/resources/classify.py">classify_files</a>(\*\*<a href="src/Deasy/types/classify_classify_files_params.py">params</a>) -> <a href="./src/Deasy/types/classify_classify_files_response.py">ClassifyClassifyFilesResponse</a></code>

# SuggestHierarchy

Types:

```python
from Deasy.types import SuggestHierarchySuggestResponse
```

Methods:

- <code title="post /suggest_hierarchy">client.suggest_hierarchy.<a href="./src/Deasy/resources/suggest_hierarchy.py">suggest</a>(\*\*<a href="src/Deasy/types/suggest_hierarchy_suggest_params.py">params</a>) -> <a href="./src/Deasy/types/suggest_hierarchy_suggest_response.py">SuggestHierarchySuggestResponse</a></code>

# SuggestDescription

Types:

```python
from Deasy.types import SuggestDescriptionCreateResponse
```

Methods:

- <code title="post /suggest_description">client.suggest_description.<a href="./src/Deasy/resources/suggest_description.py">create</a>(\*\*<a href="src/Deasy/types/suggest_description_create_params.py">params</a>) -> <a href="./src/Deasy/types/suggest_description_create_response.py">SuggestDescriptionCreateResponse</a></code>

# Tags

Types:

```python
from Deasy.types import DeasyTag, TagResponse, TagCreateResponse, TagListResponse, TagUpsertResponse
```

Methods:

- <code title="post /tags/create">client.tags.<a href="./src/Deasy/resources/tags/tags.py">create</a>(\*\*<a href="src/Deasy/types/tag_create_params.py">params</a>) -> <a href="./src/Deasy/types/tag_create_response.py">TagCreateResponse</a></code>
- <code title="put /tags/update">client.tags.<a href="./src/Deasy/resources/tags/tags.py">update</a>(\*\*<a href="src/Deasy/types/tag_update_params.py">params</a>) -> <a href="./src/Deasy/types/tag_response.py">TagResponse</a></code>
- <code title="get /tags/list">client.tags.<a href="./src/Deasy/resources/tags/tags.py">list</a>() -> <a href="./src/Deasy/types/tag_list_response.py">TagListResponse</a></code>
- <code title="delete /tags/delete">client.tags.<a href="./src/Deasy/resources/tags/tags.py">delete</a>(\*\*<a href="src/Deasy/types/tag_delete_params.py">params</a>) -> <a href="./src/Deasy/types/tag_response.py">TagResponse</a></code>
- <code title="post /tags/upsert">client.tags.<a href="./src/Deasy/resources/tags/tags.py">upsert</a>(\*\*<a href="src/Deasy/types/tag_upsert_params.py">params</a>) -> <a href="./src/Deasy/types/tag_upsert_response.py">TagUpsertResponse</a></code>

# Metadata

Types:

```python
from Deasy.types import TagCondition, MetadataDeleteResponse
```

Methods:

- <code title="post /metadata/delete">client.metadata.<a href="./src/Deasy/resources/metadata/metadata.py">delete</a>(\*\*<a href="src/Deasy/types/metadata_delete_params.py">params</a>) -> <a href="./src/Deasy/types/metadata_delete_response.py">MetadataDeleteResponse</a></code>

# Dataslice

Types:

```python
from Deasy.types import (
    DatasliceCreateResponse,
    DatasliceListResponse,
    DatasliceDeleteResponse,
    DatasliceGetFilesResponse,
    DatasliceGetMetricsResponse,
    DatasliceGetTagVdbDistributionResponse,
)
```

Methods:

- <code title="post /dataslice/create">client.dataslice.<a href="./src/Deasy/resources/dataslice/dataslice.py">create</a>(\*\*<a href="src/Deasy/types/dataslice_create_params.py">params</a>) -> <a href="./src/Deasy/types/dataslice_create_response.py">DatasliceCreateResponse</a></code>
- <code title="get /dataslice/list">client.dataslice.<a href="./src/Deasy/resources/dataslice/dataslice.py">list</a>() -> <a href="./src/Deasy/types/dataslice_list_response.py">DatasliceListResponse</a></code>
- <code title="delete /dataslice/delete">client.dataslice.<a href="./src/Deasy/resources/dataslice/dataslice.py">delete</a>(\*\*<a href="src/Deasy/types/dataslice_delete_params.py">params</a>) -> <a href="./src/Deasy/types/dataslice_delete_response.py">DatasliceDeleteResponse</a></code>
- <code title="post /dataslice/files">client.dataslice.<a href="./src/Deasy/resources/dataslice/dataslice.py">get_files</a>(\*\*<a href="src/Deasy/types/dataslice_get_files_params.py">params</a>) -> <a href="./src/Deasy/types/dataslice_get_files_response.py">DatasliceGetFilesResponse</a></code>
- <code title="post /dataslice/metrics">client.dataslice.<a href="./src/Deasy/resources/dataslice/dataslice.py">get_metrics</a>(\*\*<a href="src/Deasy/types/dataslice_get_metrics_params.py">params</a>) -> <a href="./src/Deasy/types/dataslice_get_metrics_response.py">DatasliceGetMetricsResponse</a></code>
- <code title="post /dataslice/tag_vdb_distribution">client.dataslice.<a href="./src/Deasy/resources/dataslice/dataslice.py">get_tag_vdb_distribution</a>(\*\*<a href="src/Deasy/types/dataslice_get_tag_vdb_distribution_params.py">params</a>) -> <a href="./src/Deasy/types/dataslice_get_tag_vdb_distribution_response.py">DatasliceGetTagVdbDistributionResponse</a></code>

## Export

Types:

```python
from Deasy.types.dataslice import ExportExportMetadataResponse
```

Methods:

- <code title="post /dataslice/export/metadata">client.dataslice.export.<a href="./src/Deasy/resources/dataslice/export.py">export_metadata</a>(\*\*<a href="src/Deasy/types/dataslice/export_export_metadata_params.py">params</a>) -> <a href="./src/Deasy/types/dataslice/export_export_metadata_response.py">object</a></code>

# Graph

Types:

```python
from Deasy.types import GraphOperation, GraphListResponse
```

Methods:

- <code title="post /graph/create">client.graph.<a href="./src/Deasy/resources/graph.py">create</a>(\*\*<a href="src/Deasy/types/graph_create_params.py">params</a>) -> <a href="./src/Deasy/types/graph_operation.py">GraphOperation</a></code>
- <code title="post /graph/update">client.graph.<a href="./src/Deasy/resources/graph.py">update</a>(\*\*<a href="src/Deasy/types/graph_update_params.py">params</a>) -> <a href="./src/Deasy/types/graph_operation.py">GraphOperation</a></code>
- <code title="post /graph/list">client.graph.<a href="./src/Deasy/resources/graph.py">list</a>(\*\*<a href="src/Deasy/types/graph_list_params.py">params</a>) -> <a href="./src/Deasy/types/graph_list_response.py">GraphListResponse</a></code>
- <code title="delete /graph/delete">client.graph.<a href="./src/Deasy/resources/graph.py">delete</a>(\*\*<a href="src/Deasy/types/graph_delete_params.py">params</a>) -> <a href="./src/Deasy/types/graph_operation.py">GraphOperation</a></code>
- <code title="post /graph/upsert">client.graph.<a href="./src/Deasy/resources/graph.py">upsert</a>(\*\*<a href="src/Deasy/types/graph_upsert_params.py">params</a>) -> <a href="./src/Deasy/types/graph_operation.py">GraphOperation</a></code>
