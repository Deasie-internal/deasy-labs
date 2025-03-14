# Deasy

Types:

```python
from Deasy.types import RetrieveResponse
```

Methods:

- <code title="get /">client.<a href="./src/Deasy/_client.py">retrieve</a>() -> <a href="./src/Deasy/types/retrieve_response.py">object</a></code>

# Admin

## Token

Types:

```python
from Deasy.types.admin import CreateRequest, CreateResponse, DeleteResponse, ListResponse
```

Methods:

- <code title="post /admin/token/create">client.admin.token.<a href="./src/Deasy/resources/admin/token.py">create</a>(\*\*<a href="src/Deasy/types/admin/token_create_params.py">params</a>) -> <a href="./src/Deasy/types/admin/create_response.py">CreateResponse</a></code>
- <code title="get /admin/token/list">client.admin.token.<a href="./src/Deasy/resources/admin/token.py">list</a>() -> <a href="./src/Deasy/types/admin/list_response.py">ListResponse</a></code>
- <code title="delete /admin/token/delete/{token_id}">client.admin.token.<a href="./src/Deasy/resources/admin/token.py">delete</a>(token_id) -> <a href="./src/Deasy/types/admin/delete_response.py">DeleteResponse</a></code>

# Console

Types:

```python
from Deasy.types import ConsoleFetchTiersResponse
```

Methods:

- <code title="get /console/fetch_tiers">client.console.<a href="./src/Deasy/resources/console/console.py">fetch_tiers</a>() -> <a href="./src/Deasy/types/console_fetch_tiers_response.py">ConsoleFetchTiersResponse</a></code>

## Token

Methods:

- <code title="post /console/token/create">client.console.token.<a href="./src/Deasy/resources/console/token.py">create</a>(\*\*<a href="src/Deasy/types/console/token_create_params.py">params</a>) -> <a href="./src/Deasy/types/admin/create_response.py">CreateResponse</a></code>
- <code title="get /console/token/list">client.console.token.<a href="./src/Deasy/resources/console/token.py">list</a>() -> <a href="./src/Deasy/types/admin/list_response.py">ListResponse</a></code>
- <code title="delete /console/token/{token_id}">client.console.token.<a href="./src/Deasy/resources/console/token.py">delete</a>(token_id, \*\*<a href="src/Deasy/types/console/token_delete_params.py">params</a>) -> <a href="./src/Deasy/types/admin/delete_response.py">DeleteResponse</a></code>

## Subscription

Types:

```python
from Deasy.types.console import SubscriptionRetrieveResponse
```

Methods:

- <code title="get /console/subscription">client.console.subscription.<a href="./src/Deasy/resources/console/subscription/subscription.py">retrieve</a>() -> <a href="./src/Deasy/types/console/subscription_retrieve_response.py">SubscriptionRetrieveResponse</a></code>

### Stripe

Types:

```python
from Deasy.types.console.subscription import (
    StripeCancelResponse,
    StripeCreateSessionResponse,
    StripeValidateResponse,
)
```

Methods:

- <code title="post /console/subscription/stripe/unsubscribe">client.console.subscription.stripe.<a href="./src/Deasy/resources/console/subscription/stripe.py">cancel</a>() -> <a href="./src/Deasy/types/console/subscription/stripe_cancel_response.py">StripeCancelResponse</a></code>
- <code title="post /console/subscription/stripe/payment">client.console.subscription.stripe.<a href="./src/Deasy/resources/console/subscription/stripe.py">create_session</a>(\*\*<a href="src/Deasy/types/console/subscription/stripe_create_session_params.py">params</a>) -> <a href="./src/Deasy/types/console/subscription/stripe_create_session_response.py">StripeCreateSessionResponse</a></code>
- <code title="post /console/subscription/stripe/validate">client.console.subscription.stripe.<a href="./src/Deasy/resources/console/subscription/stripe.py">validate</a>() -> <a href="./src/Deasy/types/console/subscription/stripe_validate_response.py">StripeValidateResponse</a></code>

## Vdbconnector

Types:

```python
from Deasy.types.console import (
    VdbconnectorCreateResponse,
    VdbconnectorDeleteResponse,
    VdbconnectorGetDeleteStatsResponse,
)
```

Methods:

- <code title="post /console/vdbconnector/create">client.console.vdbconnector.<a href="./src/Deasy/resources/console/vdbconnector.py">create</a>(\*\*<a href="src/Deasy/types/console/vdbconnector_create_params.py">params</a>) -> <a href="./src/Deasy/types/console/vdbconnector_create_response.py">VdbconnectorCreateResponse</a></code>
- <code title="post /console/vdbconnector/delete">client.console.vdbconnector.<a href="./src/Deasy/resources/console/vdbconnector.py">delete</a>(\*\*<a href="src/Deasy/types/console/vdbconnector_delete_params.py">params</a>) -> <a href="./src/Deasy/types/console/vdbconnector_delete_response.py">VdbconnectorDeleteResponse</a></code>
- <code title="post /console/vdbconnector/delete_stats">client.console.vdbconnector.<a href="./src/Deasy/resources/console/vdbconnector.py">get_delete_stats</a>(\*\*<a href="src/Deasy/types/console/vdbconnector_get_delete_stats_params.py">params</a>) -> <a href="./src/Deasy/types/console/vdbconnector_get_delete_stats_response.py">VdbconnectorGetDeleteStatsResponse</a></code>

## Secret

Types:

```python
from Deasy.types.console import SecretGetResponse, SecretStoreResponse
```

Methods:

- <code title="post /console/secret/get">client.console.secret.<a href="./src/Deasy/resources/console/secret.py">get</a>(\*\*<a href="src/Deasy/types/console/secret_get_params.py">params</a>) -> <a href="./src/Deasy/types/console/secret_get_response.py">SecretGetResponse</a></code>
- <code title="post /console/secret/store">client.console.secret.<a href="./src/Deasy/resources/console/secret.py">store</a>(\*\*<a href="src/Deasy/types/console/secret_store_params.py">params</a>) -> <a href="./src/Deasy/types/console/secret_store_response.py">SecretStoreResponse</a></code>

## LlmProvider

Types:

```python
from Deasy.types.console import LlmProviderValidateResponse
```

Methods:

- <code title="post /console/llm-provider/validate">client.console.llm_provider.<a href="./src/Deasy/resources/console/llm_provider.py">validate</a>(\*\*<a href="src/Deasy/types/console/llm_provider_validate_params.py">params</a>) -> <a href="./src/Deasy/types/console/llm_provider_validate_response.py">LlmProviderValidateResponse</a></code>

## Marketplace

Types:

```python
from Deasy.types.console import MarketplaceSignupResponse
```

Methods:

- <code title="post /console/marketplace/signup">client.console.marketplace.<a href="./src/Deasy/resources/console/marketplace.py">signup</a>(\*\*<a href="src/Deasy/types/console/marketplace_signup_params.py">params</a>) -> <a href="./src/Deasy/types/console/marketplace_signup_response.py">MarketplaceSignupResponse</a></code>

## VectorDB

Types:

```python
from Deasy.types.console import VectorDBCheckIndexesResponse, VectorDBValidateResponse
```

Methods:

- <code title="post /console/vector-db/check-index-fields">client.console.vector_db.<a href="./src/Deasy/resources/console/vector_db.py">check_indexes</a>(\*\*<a href="src/Deasy/types/console/vector_db_check_indexes_params.py">params</a>) -> <a href="./src/Deasy/types/console/vector_db_check_indexes_response.py">VectorDBCheckIndexesResponse</a></code>
- <code title="post /console/vector-db/validate">client.console.vector_db.<a href="./src/Deasy/resources/console/vector_db.py">validate</a>(\*\*<a href="src/Deasy/types/console/vector_db_validate_params.py">params</a>) -> <a href="./src/Deasy/types/console/vector_db_validate_response.py">VectorDBValidateResponse</a></code>

## User

Types:

```python
from Deasy.types.console import UserUpdateProfileResponse
```

Methods:

- <code title="post /console/user/profile">client.console.user.<a href="./src/Deasy/resources/console/user.py">update_profile</a>(\*\*<a href="src/Deasy/types/console/user_update_profile_params.py">params</a>) -> <a href="./src/Deasy/types/console/user_update_profile_response.py">UserUpdateProfileResponse</a></code>

## Webhook

Types:

```python
from Deasy.types.console import WebhookHandleStripeResponse
```

Methods:

- <code title="post /console/webhook/stripe">client.console.webhook.<a href="./src/Deasy/resources/console/webhook.py">handle_stripe</a>() -> <a href="./src/Deasy/types/console/webhook_handle_stripe_response.py">object</a></code>

# Classify

Types:

```python
from Deasy.types import ClassifyClassifyAllResponse, ClassifyClassifyFilesResponse
```

Methods:

- <code title="post /classify/all">client.classify.<a href="./src/Deasy/resources/classify.py">classify_all</a>(\*\*<a href="src/Deasy/types/classify_classify_all_params.py">params</a>) -> <a href="./src/Deasy/types/classify_classify_all_response.py">ClassifyClassifyAllResponse</a></code>
- <code title="post /classify">client.classify.<a href="./src/Deasy/resources/classify.py">classify_files</a>(\*\*<a href="src/Deasy/types/classify_classify_files_params.py">params</a>) -> <a href="./src/Deasy/types/classify_classify_files_response.py">ClassifyClassifyFilesResponse</a></code>

# SuggestHierarchy

Types:

```python
from Deasy.types import SuggestHierarchySuggestResponse
```

Methods:

- <code title="post /suggest_hierarchy">client.suggest_hierarchy.<a href="./src/Deasy/resources/suggest_hierarchy.py">suggest</a>(\*\*<a href="src/Deasy/types/suggest_hierarchy_suggest_params.py">params</a>) -> <a href="./src/Deasy/types/suggest_hierarchy_suggest_response.py">SuggestHierarchySuggestResponse</a></code>

# RefineTag

Types:

```python
from Deasy.types import RefineTagRefineResponse
```

Methods:

- <code title="post /refine_tag">client.refine_tag.<a href="./src/Deasy/resources/refine_tag.py">refine</a>(\*\*<a href="src/Deasy/types/refine_tag_refine_params.py">params</a>) -> <a href="./src/Deasy/types/refine_tag_refine_response.py">RefineTagRefineResponse</a></code>

# TagText

Types:

```python
from Deasy.types import TagTextClassifyResponse
```

Methods:

- <code title="post /tag_text">client.tag_text.<a href="./src/Deasy/resources/tag_text.py">classify</a>(\*\*<a href="src/Deasy/types/tag_text_classify_params.py">params</a>) -> <a href="./src/Deasy/types/tag_text_classify_response.py">TagTextClassifyResponse</a></code>

# GenerateFileTags

Types:

```python
from Deasy.types import GenerateFileTagCreateResponse
```

Methods:

- <code title="post /generate_file_tags">client.generate_file_tags.<a href="./src/Deasy/resources/generate_file_tags.py">create</a>(\*\*<a href="src/Deasy/types/generate_file_tag_create_params.py">params</a>) -> <a href="./src/Deasy/types/generate_file_tag_create_response.py">GenerateFileTagCreateResponse</a></code>

# Contextualize

Types:

```python
from Deasy.types import ContextualizeCreateResponse
```

Methods:

- <code title="post /contextualize">client.contextualize.<a href="./src/Deasy/resources/contextualize.py">create</a>(\*\*<a href="src/Deasy/types/contextualize_create_params.py">params</a>) -> <a href="./src/Deasy/types/contextualize_create_response.py">ContextualizeCreateResponse</a></code>

# SuggestDescription

Types:

```python
from Deasy.types import SuggestDescriptionCreateResponse
```

Methods:

- <code title="post /suggest_description">client.suggest_description.<a href="./src/Deasy/resources/suggest_description.py">create</a>(\*\*<a href="src/Deasy/types/suggest_description_create_params.py">params</a>) -> <a href="./src/Deasy/types/suggest_description_create_response.py">SuggestDescriptionCreateResponse</a></code>

# Data

Types:

```python
from Deasy.types import (
    DataGetDocumentTextResponse,
    DataGetVdbTotalFilesResponse,
    DataListPaginatedResponse,
)
```

Methods:

- <code title="post /data/document_text">client.data.<a href="./src/Deasy/resources/data/data.py">get_document_text</a>(\*\*<a href="src/Deasy/types/data_get_document_text_params.py">params</a>) -> <a href="./src/Deasy/types/data_get_document_text_response.py">DataGetDocumentTextResponse</a></code>
- <code title="post /data/file_count">client.data.<a href="./src/Deasy/resources/data/data.py">get_vdb_total_files</a>(\*\*<a href="src/Deasy/types/data_get_vdb_total_files_params.py">params</a>) -> <a href="./src/Deasy/types/data_get_vdb_total_files_response.py">DataGetVdbTotalFilesResponse</a></code>
- <code title="post /data/list_paginated">client.data.<a href="./src/Deasy/resources/data/data.py">list_paginated</a>(\*\*<a href="src/Deasy/types/data_list_paginated_params.py">params</a>) -> <a href="./src/Deasy/types/data_list_paginated_response.py">DataListPaginatedResponse</a></code>

## Metadata

Types:

```python
from Deasy.types.data import MetadataListResponse, MetadataDeleteResponse
```

Methods:

- <code title="post /data/metadata/list">client.data.metadata.<a href="./src/Deasy/resources/data/metadata.py">list</a>(\*\*<a href="src/Deasy/types/data/metadata_list_params.py">params</a>) -> <a href="./src/Deasy/types/data/metadata_list_response.py">MetadataListResponse</a></code>
- <code title="post /data/metadata/delete">client.data.metadata.<a href="./src/Deasy/resources/data/metadata.py">delete</a>(\*\*<a href="src/Deasy/types/data/metadata_delete_params.py">params</a>) -> <a href="./src/Deasy/types/data/metadata_delete_response.py">MetadataDeleteResponse</a></code>

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

- <code title="post /tags/create">client.tags.<a href="./src/Deasy/resources/tags/tags.py">create</a>(\*\*<a href="src/Deasy/types/tag_create_params.py">params</a>) -> <a href="./src/Deasy/types/tag_create_response.py">TagCreateResponse</a></code>
- <code title="put /tags/update">client.tags.<a href="./src/Deasy/resources/tags/tags.py">update</a>(\*\*<a href="src/Deasy/types/tag_update_params.py">params</a>) -> <a href="./src/Deasy/types/tag_response.py">TagResponse</a></code>
- <code title="get /tags/list">client.tags.<a href="./src/Deasy/resources/tags/tags.py">list</a>() -> <a href="./src/Deasy/types/tag_list_response.py">TagListResponse</a></code>
- <code title="delete /tags/delete">client.tags.<a href="./src/Deasy/resources/tags/tags.py">delete</a>(\*\*<a href="src/Deasy/types/tag_delete_params.py">params</a>) -> <a href="./src/Deasy/types/tag_response.py">TagResponse</a></code>
- <code title="post /tags/delete_stats">client.tags.<a href="./src/Deasy/resources/tags/tags.py">get_delete_stats</a>(\*\*<a href="src/Deasy/types/tag_get_delete_stats_params.py">params</a>) -> <a href="./src/Deasy/types/tag_get_delete_stats_response.py">TagGetDeleteStatsResponse</a></code>
- <code title="post /tags/upsert">client.tags.<a href="./src/Deasy/resources/tags/tags.py">upsert</a>(\*\*<a href="src/Deasy/types/tag_upsert_params.py">params</a>) -> <a href="./src/Deasy/types/tag_upsert_response.py">TagUpsertResponse</a></code>

## Groups

Types:

```python
from Deasy.types.tags import (
    DeasyTagGroup,
    GroupCreateResponse,
    GroupUpdateResponse,
    GroupListResponse,
    GroupDeleteResponse,
)
```

Methods:

- <code title="post /tags/groups/create">client.tags.groups.<a href="./src/Deasy/resources/tags/groups.py">create</a>(\*\*<a href="src/Deasy/types/tags/group_create_params.py">params</a>) -> <a href="./src/Deasy/types/tags/group_create_response.py">GroupCreateResponse</a></code>
- <code title="put /tags/groups/update">client.tags.groups.<a href="./src/Deasy/resources/tags/groups.py">update</a>(\*\*<a href="src/Deasy/types/tags/group_update_params.py">params</a>) -> <a href="./src/Deasy/types/tags/group_update_response.py">GroupUpdateResponse</a></code>
- <code title="get /tags/groups/list">client.tags.groups.<a href="./src/Deasy/resources/tags/groups.py">list</a>() -> <a href="./src/Deasy/types/tags/group_list_response.py">GroupListResponse</a></code>
- <code title="delete /tags/groups/delete">client.tags.groups.<a href="./src/Deasy/resources/tags/groups.py">delete</a>(\*\*<a href="src/Deasy/types/tags/group_delete_params.py">params</a>) -> <a href="./src/Deasy/types/tags/group_delete_response.py">GroupDeleteResponse</a></code>

# Metadata

Types:

```python
from Deasy.types import (
    BasicMetadataRequest,
    HierarchyStatsNode,
    TagCondition,
    MetadataDeleteResponse,
    MetadataApplyStandardizationDBResponse,
    MetadataCountDistributionsResponse,
    MetadataFilterByConditionsResponse,
    MetadataGetBasicMetadataResponse,
    MetadataGetDistinctValuesResponse,
    MetadataGetDistributionsResponse,
    MetadataGetEvidenceResponse,
    MetadataGetFilteredMetadataResponse,
    MetadataGetOobTaggedFileCountResponse,
    MetadataGetTagStatisticsResponse,
    MetadataGetUniqueTagsResponse,
    MetadataSuggestStandardizationResponse,
)
```

Methods:

- <code title="post /metadata/delete">client.metadata.<a href="./src/Deasy/resources/metadata/metadata.py">delete</a>(\*\*<a href="src/Deasy/types/metadata_delete_params.py">params</a>) -> <a href="./src/Deasy/types/metadata_delete_response.py">MetadataDeleteResponse</a></code>
- <code title="post /metadata/standardization_db">client.metadata.<a href="./src/Deasy/resources/metadata/metadata.py">apply_standardization_db</a>(\*\*<a href="src/Deasy/types/metadata_apply_standardization_db_params.py">params</a>) -> <a href="./src/Deasy/types/metadata_apply_standardization_db_response.py">MetadataApplyStandardizationDBResponse</a></code>
- <code title="post /metadata/count_distributions">client.metadata.<a href="./src/Deasy/resources/metadata/metadata.py">count_distributions</a>(\*\*<a href="src/Deasy/types/metadata_count_distributions_params.py">params</a>) -> <a href="./src/Deasy/types/metadata_count_distributions_response.py">MetadataCountDistributionsResponse</a></code>
- <code title="post /metadata/conditional_filter">client.metadata.<a href="./src/Deasy/resources/metadata/metadata.py">filter_by_conditions</a>(\*\*<a href="src/Deasy/types/metadata_filter_by_conditions_params.py">params</a>) -> <a href="./src/Deasy/types/metadata_filter_by_conditions_response.py">MetadataFilterByConditionsResponse</a></code>
- <code title="post /metadata/basic">client.metadata.<a href="./src/Deasy/resources/metadata/metadata.py">get_basic_metadata</a>(\*\*<a href="src/Deasy/types/metadata_get_basic_metadata_params.py">params</a>) -> <a href="./src/Deasy/types/metadata_get_basic_metadata_response.py">MetadataGetBasicMetadataResponse</a></code>
- <code title="post /metadata/distinct_values">client.metadata.<a href="./src/Deasy/resources/metadata/metadata.py">get_distinct_values</a>(\*\*<a href="src/Deasy/types/metadata_get_distinct_values_params.py">params</a>) -> <a href="./src/Deasy/types/metadata_get_distinct_values_response.py">MetadataGetDistinctValuesResponse</a></code>
- <code title="post /metadata/distributions">client.metadata.<a href="./src/Deasy/resources/metadata/metadata.py">get_distributions</a>(\*\*<a href="src/Deasy/types/metadata_get_distributions_params.py">params</a>) -> <a href="./src/Deasy/types/metadata_get_distributions_response.py">MetadataGetDistributionsResponse</a></code>
- <code title="post /metadata/get_evidence">client.metadata.<a href="./src/Deasy/resources/metadata/metadata.py">get_evidence</a>(\*\*<a href="src/Deasy/types/metadata_get_evidence_params.py">params</a>) -> <a href="./src/Deasy/types/metadata_get_evidence_response.py">MetadataGetEvidenceResponse</a></code>
- <code title="post /metadata/filtered">client.metadata.<a href="./src/Deasy/resources/metadata/metadata.py">get_filtered_metadata</a>(\*\*<a href="src/Deasy/types/metadata_get_filtered_metadata_params.py">params</a>) -> <a href="./src/Deasy/types/metadata_get_filtered_metadata_response.py">MetadataGetFilteredMetadataResponse</a></code>
- <code title="post /metadata/oob_tag_file_count">client.metadata.<a href="./src/Deasy/resources/metadata/metadata.py">get_oob_tagged_file_count</a>(\*\*<a href="src/Deasy/types/metadata_get_oob_tagged_file_count_params.py">params</a>) -> <a href="./src/Deasy/types/metadata_get_oob_tagged_file_count_response.py">MetadataGetOobTaggedFileCountResponse</a></code>
- <code title="post /metadata/tag_statistics">client.metadata.<a href="./src/Deasy/resources/metadata/metadata.py">get_tag_statistics</a>(\*\*<a href="src/Deasy/types/metadata_get_tag_statistics_params.py">params</a>) -> <a href="./src/Deasy/types/metadata_get_tag_statistics_response.py">MetadataGetTagStatisticsResponse</a></code>
- <code title="post /metadata/get_unique_tags">client.metadata.<a href="./src/Deasy/resources/metadata/metadata.py">get_unique_tags</a>(\*\*<a href="src/Deasy/types/metadata_get_unique_tags_params.py">params</a>) -> <a href="./src/Deasy/types/metadata_get_unique_tags_response.py">MetadataGetUniqueTagsResponse</a></code>
- <code title="post /metadata/standardization_suggest">client.metadata.<a href="./src/Deasy/resources/metadata/metadata.py">suggest_standardization</a>(\*\*<a href="src/Deasy/types/metadata_suggest_standardization_params.py">params</a>) -> <a href="./src/Deasy/types/metadata_suggest_standardization_response.py">MetadataSuggestStandardizationResponse</a></code>

## File

Types:

```python
from Deasy.types.metadata import FileListResponse
```

Methods:

- <code title="post /metadata/file/list">client.metadata.file.<a href="./src/Deasy/resources/metadata/file.py">list</a>(\*\*<a href="src/Deasy/types/metadata/file_list_params.py">params</a>) -> <a href="./src/Deasy/types/metadata/file_list_response.py">FileListResponse</a></code>

## Chunk

Types:

```python
from Deasy.types.metadata import ChunkListResponse
```

Methods:

- <code title="post /metadata/chunk/list">client.metadata.chunk.<a href="./src/Deasy/resources/metadata/chunk.py">list</a>(\*\*<a href="src/Deasy/types/metadata/chunk_list_params.py">params</a>) -> <a href="./src/Deasy/types/metadata/chunk_list_response.py">ChunkListResponse</a></code>

## Standardize

Types:

```python
from Deasy.types.metadata import (
    StandardizeListResponse,
    StandardizeInsertResponse,
    StandardizeTagDistributionResponse,
)
```

Methods:

- <code title="post /metadata/standardize/list">client.metadata.standardize.<a href="./src/Deasy/resources/metadata/standardize.py">list</a>(\*\*<a href="src/Deasy/types/metadata/standardize_list_params.py">params</a>) -> <a href="./src/Deasy/types/metadata/standardize_list_response.py">object</a></code>
- <code title="post /metadata/standardize/insert">client.metadata.standardize.<a href="./src/Deasy/resources/metadata/standardize.py">insert</a>(\*\*<a href="src/Deasy/types/metadata/standardize_insert_params.py">params</a>) -> <a href="./src/Deasy/types/metadata/standardize_insert_response.py">object</a></code>
- <code title="post /metadata/standardize/tag_distribution">client.metadata.standardize.<a href="./src/Deasy/resources/metadata/standardize.py">tag_distribution</a>(\*\*<a href="src/Deasy/types/metadata/standardize_tag_distribution_params.py">params</a>) -> <a href="./src/Deasy/types/metadata/standardize_tag_distribution_response.py">StandardizeTagDistributionResponse</a></code>

# Dataslice

Types:

```python
from Deasy.types import (
    Condition,
    DatasliceCreateResponse,
    DatasliceListResponse,
    DatasliceDeleteResponse,
    DatasliceCheckSyncScoreResponse,
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
- <code title="post /dataslice/sync_score">client.dataslice.<a href="./src/Deasy/resources/dataslice/dataslice.py">check_sync_score</a>(\*\*<a href="src/Deasy/types/dataslice_check_sync_score_params.py">params</a>) -> <a href="./src/Deasy/types/dataslice_check_sync_score_response.py">DatasliceCheckSyncScoreResponse</a></code>
- <code title="post /dataslice/file_count">client.dataslice.<a href="./src/Deasy/resources/dataslice/dataslice.py">get_file_count</a>(\*\*<a href="src/Deasy/types/dataslice_get_file_count_params.py">params</a>) -> <a href="./src/Deasy/types/dataslice_get_file_count_response.py">DatasliceGetFileCountResponse</a></code>
- <code title="post /dataslice/files">client.dataslice.<a href="./src/Deasy/resources/dataslice/dataslice.py">get_files</a>(\*\*<a href="src/Deasy/types/dataslice_get_files_params.py">params</a>) -> <a href="./src/Deasy/types/dataslice_get_files_response.py">DatasliceGetFilesResponse</a></code>
- <code title="post /dataslice/metrics">client.dataslice.<a href="./src/Deasy/resources/dataslice/dataslice.py">get_metrics</a>(\*\*<a href="src/Deasy/types/dataslice_get_metrics_params.py">params</a>) -> <a href="./src/Deasy/types/dataslice_get_metrics_response.py">DatasliceGetMetricsResponse</a></code>
- <code title="post /dataslice/tag_vdb_distribution">client.dataslice.<a href="./src/Deasy/resources/dataslice/dataslice.py">get_tag_vdb_distribution</a>(\*\*<a href="src/Deasy/types/dataslice_get_tag_vdb_distribution_params.py">params</a>) -> <a href="./src/Deasy/types/dataslice_get_tag_vdb_distribution_response.py">DatasliceGetTagVdbDistributionResponse</a></code>

## Export

Types:

```python
from Deasy.types.dataslice import ExportExportMetadataResponse, ExportExportToVdbResponse
```

Methods:

- <code title="post /dataslice/export/metadata">client.dataslice.export.<a href="./src/Deasy/resources/dataslice/export.py">export_metadata</a>(\*\*<a href="src/Deasy/types/dataslice/export_export_metadata_params.py">params</a>) -> <a href="./src/Deasy/types/dataslice/export_export_metadata_response.py">object</a></code>
- <code title="post /dataslice/export/vdb">client.dataslice.export.<a href="./src/Deasy/resources/dataslice/export.py">export_to_vdb</a>(\*\*<a href="src/Deasy/types/dataslice/export_export_to_vdb_params.py">params</a>) -> <a href="./src/Deasy/types/dataslice/export_export_to_vdb_response.py">ExportExportToVdbResponse</a></code>

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

# Ocr

Types:

```python
from Deasy.types import OcrIngestResponse, OcrSyncStatsResponse
```

Methods:

- <code title="post /ocr/ingest">client.ocr.<a href="./src/Deasy/resources/ocr.py">ingest</a>(\*\*<a href="src/Deasy/types/ocr_ingest_params.py">params</a>) -> <a href="./src/Deasy/types/ocr_ingest_response.py">object</a></code>
- <code title="post /ocr/sync_stats">client.ocr.<a href="./src/Deasy/resources/ocr.py">sync_stats</a>(\*\*<a href="src/Deasy/types/ocr_sync_stats_params.py">params</a>) -> <a href="./src/Deasy/types/ocr_sync_stats_response.py">object</a></code>

# ProgressTracker

Types:

```python
from Deasy.types import (
    ProgressTrackerAbortProgressTrackerResponse,
    ProgressTrackerDeleteProgressTrackersResponse,
    ProgressTrackerListProgressTrackersResponse,
    ProgressTrackerRetrieveTaskStatusResponse,
)
```

Methods:

- <code title="put /progress_tracker/abort_progress_tracker/{tracker_id}">client.progress_tracker.<a href="./src/Deasy/resources/progress_tracker.py">abort_progress_tracker</a>(tracker_id) -> <a href="./src/Deasy/types/progress_tracker_abort_progress_tracker_response.py">object</a></code>
- <code title="post /progress_tracker/delete_progress_trackers">client.progress_tracker.<a href="./src/Deasy/resources/progress_tracker.py">delete_progress_trackers</a>(\*\*<a href="src/Deasy/types/progress_tracker_delete_progress_trackers_params.py">params</a>) -> <a href="./src/Deasy/types/progress_tracker_delete_progress_trackers_response.py">ProgressTrackerDeleteProgressTrackersResponse</a></code>
- <code title="get /progress_tracker/get_progress_trackers">client.progress_tracker.<a href="./src/Deasy/resources/progress_tracker.py">list_progress_trackers</a>() -> <a href="./src/Deasy/types/progress_tracker_list_progress_trackers_response.py">ProgressTrackerListProgressTrackersResponse</a></code>
- <code title="get /progress_tracker/task_status/{job_id}">client.progress_tracker.<a href="./src/Deasy/resources/progress_tracker.py">retrieve_task_status</a>(job_id) -> <a href="./src/Deasy/types/progress_tracker_retrieve_task_status_response.py">ProgressTrackerRetrieveTaskStatusResponse</a></code>

# Health

Types:

```python
from Deasy.types import HealthCheckResponse
```

Methods:

- <code title="get /health">client.health.<a href="./src/Deasy/resources/health.py">check</a>() -> <a href="./src/Deasy/types/health_check_response.py">object</a></code>
