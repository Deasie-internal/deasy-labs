# ClassifyBulk

Types:

```python
from Deasy.types import ConditionInput, ClassifyBulkClassifyResponse
```

Methods:

- <code title="post /classify_bulk">client.classify_bulk.<a href="./src/Deasy/resources/classify_bulk.py">classify</a>(\*\*<a href="src/Deasy/types/classify_bulk_classify_params.py">params</a>) -> <a href="./src/Deasy/types/classify_bulk_classify_response.py">ClassifyBulkClassifyResponse</a></code>

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
from Deasy.types import SuggestHierarchyCreateResponse
```

Methods:

- <code title="post /suggest_hierarchy">client.suggest_hierarchy.<a href="./src/Deasy/resources/suggest_hierarchy.py">create</a>(\*\*<a href="src/Deasy/types/suggest_hierarchy_create_params.py">params</a>) -> <a href="./src/Deasy/types/suggest_hierarchy_create_response.py">SuggestHierarchyCreateResponse</a></code>

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
from Deasy.types import (
    DeasyTag,
    TagResponse,
    TagCreateResponse,
    TagListResponse,
    TagGetDeleteStatsResponse,
    TagUpsertResponse,
)
```

Methods:

- <code title="post /tags/create">client.tags.<a href="./src/Deasy/resources/tags.py">create</a>(\*\*<a href="src/Deasy/types/tag_create_params.py">params</a>) -> <a href="./src/Deasy/types/tag_create_response.py">TagCreateResponse</a></code>
- <code title="put /tags/update">client.tags.<a href="./src/Deasy/resources/tags.py">update</a>(\*\*<a href="src/Deasy/types/tag_update_params.py">params</a>) -> <a href="./src/Deasy/types/tag_response.py">TagResponse</a></code>
- <code title="get /tags/list">client.tags.<a href="./src/Deasy/resources/tags.py">list</a>() -> <a href="./src/Deasy/types/tag_list_response.py">TagListResponse</a></code>
- <code title="delete /tags/delete">client.tags.<a href="./src/Deasy/resources/tags.py">delete</a>(\*\*<a href="src/Deasy/types/tag_delete_params.py">params</a>) -> <a href="./src/Deasy/types/tag_response.py">TagResponse</a></code>
- <code title="post /tags/delete_stats">client.tags.<a href="./src/Deasy/resources/tags.py">get_delete_stats</a>(\*\*<a href="src/Deasy/types/tag_get_delete_stats_params.py">params</a>) -> <a href="./src/Deasy/types/tag_get_delete_stats_response.py">TagGetDeleteStatsResponse</a></code>
- <code title="post /tags/upsert">client.tags.<a href="./src/Deasy/resources/tags.py">upsert</a>(\*\*<a href="src/Deasy/types/tag_upsert_params.py">params</a>) -> <a href="./src/Deasy/types/tag_upsert_response.py">TagUpsertResponse</a></code>

# Metadata

Types:

```python
from Deasy.types import (
    MetadataListResponse,
    MetadataDeleteResponse,
    MetadataListPaginatedResponse,
    MetadataUpsertResponse,
)
```

Methods:

- <code title="post /metadata/list">client.metadata.<a href="./src/Deasy/resources/metadata.py">list</a>(\*\*<a href="src/Deasy/types/metadata_list_params.py">params</a>) -> <a href="./src/Deasy/types/metadata_list_response.py">MetadataListResponse</a></code>
- <code title="post /metadata/delete">client.metadata.<a href="./src/Deasy/resources/metadata.py">delete</a>(\*\*<a href="src/Deasy/types/metadata_delete_params.py">params</a>) -> <a href="./src/Deasy/types/metadata_delete_response.py">MetadataDeleteResponse</a></code>
- <code title="post /metadata/list_paginated">client.metadata.<a href="./src/Deasy/resources/metadata.py">list_paginated</a>(\*\*<a href="src/Deasy/types/metadata_list_paginated_params.py">params</a>) -> <a href="./src/Deasy/types/metadata_list_paginated_response.py">MetadataListPaginatedResponse</a></code>
- <code title="post /metadata/upsert">client.metadata.<a href="./src/Deasy/resources/metadata.py">upsert</a>(\*\*<a href="src/Deasy/types/metadata_upsert_params.py">params</a>) -> <a href="./src/Deasy/types/metadata_upsert_response.py">MetadataUpsertResponse</a></code>

# VdbConnector

Types:

```python
from Deasy.types import (
    ConnectorResponse,
    DeleteConnector,
    ListVdbConnector,
    PsqlConnectorConfig,
    QdrantConnectorConfig,
    S3ConnectorConfig,
    SharepointConnectorConfig,
    VdbConnectorGetDeleteStatsResponse,
)
```

Methods:

- <code title="post /vdb_connector/create">client.vdb_connector.<a href="./src/Deasy/resources/vdb_connector.py">create</a>(\*\*<a href="src/Deasy/types/vdb_connector_create_params.py">params</a>) -> <a href="./src/Deasy/types/connector_response.py">ConnectorResponse</a></code>
- <code title="post /vdb_connector/update">client.vdb_connector.<a href="./src/Deasy/resources/vdb_connector.py">update</a>(\*\*<a href="src/Deasy/types/vdb_connector_update_params.py">params</a>) -> <a href="./src/Deasy/types/connector_response.py">ConnectorResponse</a></code>
- <code title="post /vdb_connector/list">client.vdb_connector.<a href="./src/Deasy/resources/vdb_connector.py">list</a>() -> <a href="./src/Deasy/types/list_vdb_connector.py">ListVdbConnector</a></code>
- <code title="post /vdb_connector/delete">client.vdb_connector.<a href="./src/Deasy/resources/vdb_connector.py">delete</a>(\*\*<a href="src/Deasy/types/vdb_connector_delete_params.py">params</a>) -> <a href="./src/Deasy/types/connector_response.py">ConnectorResponse</a></code>
- <code title="post /vdb_connector/delete_stats">client.vdb_connector.<a href="./src/Deasy/resources/vdb_connector.py">get_delete_stats</a>(\*\*<a href="src/Deasy/types/vdb_connector_get_delete_stats_params.py">params</a>) -> <a href="./src/Deasy/types/vdb_connector_get_delete_stats_response.py">VdbConnectorGetDeleteStatsResponse</a></code>

# LlmConnector

Types:

```python
from Deasy.types import OpenAIConfig
```

Methods:

- <code title="post /llm_connector/create">client.llm_connector.<a href="./src/Deasy/resources/llm_connector.py">create</a>(\*\*<a href="src/Deasy/types/llm_connector_create_params.py">params</a>) -> <a href="./src/Deasy/types/connector_response.py">ConnectorResponse</a></code>
- <code title="post /llm_connector/update">client.llm_connector.<a href="./src/Deasy/resources/llm_connector.py">update</a>(\*\*<a href="src/Deasy/types/llm_connector_update_params.py">params</a>) -> <a href="./src/Deasy/types/connector_response.py">ConnectorResponse</a></code>
- <code title="post /llm_connector/list">client.llm_connector.<a href="./src/Deasy/resources/llm_connector.py">list</a>() -> <a href="./src/Deasy/types/list_vdb_connector.py">ListVdbConnector</a></code>
- <code title="post /llm_connector/delete">client.llm_connector.<a href="./src/Deasy/resources/llm_connector.py">delete</a>(\*\*<a href="src/Deasy/types/llm_connector_delete_params.py">params</a>) -> <a href="./src/Deasy/types/connector_response.py">ConnectorResponse</a></code>

# Dataslice

Types:

```python
from Deasy.types import (
    ConditionOutput,
    DatasliceCreateResponse,
    DatasliceListResponse,
    DatasliceDeleteResponse,
    DatasliceGetFileCountResponse,
    DatasliceGetFilesResponse,
    DatasliceGetMetricsResponse,
    DatasliceGetTagVdbDistributionResponse,
)
```

Methods:

- <code title="post /dataslice/create">client.dataslice.<a href="./src/Deasy/resources/dataslice/dataslice.py">create</a>(\*\*<a href="src/Deasy/types/dataslice_create_params.py">params</a>) -> <a href="./src/Deasy/types/dataslice_create_response.py">DatasliceCreateResponse</a></code>
- <code title="get /dataslice/list">client.dataslice.<a href="./src/Deasy/resources/dataslice/dataslice.py">list</a>() -> <a href="./src/Deasy/types/dataslice_list_response.py">DatasliceListResponse</a></code>
- <code title="delete /dataslice/delete">client.dataslice.<a href="./src/Deasy/resources/dataslice/dataslice.py">delete</a>(\*\*<a href="src/Deasy/types/dataslice_delete_params.py">params</a>) -> <a href="./src/Deasy/types/dataslice_delete_response.py">DatasliceDeleteResponse</a></code>
- <code title="post /dataslice/file_count">client.dataslice.<a href="./src/Deasy/resources/dataslice/dataslice.py">get_file_count</a>(\*\*<a href="src/Deasy/types/dataslice_get_file_count_params.py">params</a>) -> <a href="./src/Deasy/types/dataslice_get_file_count_response.py">DatasliceGetFileCountResponse</a></code>
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
from Deasy.types import GraphOperationResponse, GraphListResponse
```

Methods:

- <code title="post /graph/create">client.graph.<a href="./src/Deasy/resources/graph.py">create</a>(\*\*<a href="src/Deasy/types/graph_create_params.py">params</a>) -> <a href="./src/Deasy/types/graph_operation_response.py">GraphOperationResponse</a></code>
- <code title="post /graph/update">client.graph.<a href="./src/Deasy/resources/graph.py">update</a>(\*\*<a href="src/Deasy/types/graph_update_params.py">params</a>) -> <a href="./src/Deasy/types/graph_operation_response.py">GraphOperationResponse</a></code>
- <code title="post /graph/list">client.graph.<a href="./src/Deasy/resources/graph.py">list</a>(\*\*<a href="src/Deasy/types/graph_list_params.py">params</a>) -> <a href="./src/Deasy/types/graph_list_response.py">GraphListResponse</a></code>
- <code title="delete /graph/delete">client.graph.<a href="./src/Deasy/resources/graph.py">delete</a>(\*\*<a href="src/Deasy/types/graph_delete_params.py">params</a>) -> <a href="./src/Deasy/types/graph_operation_response.py">GraphOperationResponse</a></code>
- <code title="post /graph/upsert">client.graph.<a href="./src/Deasy/resources/graph.py">upsert</a>(\*\*<a href="src/Deasy/types/graph_upsert_params.py">params</a>) -> <a href="./src/Deasy/types/graph_operation_response.py">GraphOperationResponse</a></code>
