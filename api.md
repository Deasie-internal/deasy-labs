# DeasyLabs

Types:

```python
from Deasy_Labs.types import RetrieveResponse
```

Methods:

- <code title="get /">client.<a href="./src/Deasy_Labs/_client.py">retrieve</a>() -> <a href="./src/Deasy_Labs/types/retrieve_response.py">object</a></code>

# Admin

## Token

Types:

```python
from Deasy_Labs.types.admin import (
    TokenCreateRequest,
    TokenCreateResponse,
    TokenDeleteResponse,
    TokenListResponse,
)
```

Methods:

- <code title="post /admin/token/create">client.admin.token.<a href="./src/Deasy_Labs/resources/admin/token.py">create</a>(\*\*<a href="src/Deasy_Labs/types/admin/token_create_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/admin/token_create_response.py">TokenCreateResponse</a></code>
- <code title="get /admin/token/list">client.admin.token.<a href="./src/Deasy_Labs/resources/admin/token.py">list</a>() -> <a href="./src/Deasy_Labs/types/admin/token_list_response.py">TokenListResponse</a></code>
- <code title="delete /admin/token/delete/{token_id}">client.admin.token.<a href="./src/Deasy_Labs/resources/admin/token.py">delete</a>(token_id) -> <a href="./src/Deasy_Labs/types/admin/token_delete_response.py">TokenDeleteResponse</a></code>

# Console

Types:

```python
from Deasy_Labs.types import ConsoleFetchTiersResponse
```

Methods:

- <code title="get /console/fetch_tiers">client.console.<a href="./src/Deasy_Labs/resources/console/console.py">fetch_tiers</a>() -> <a href="./src/Deasy_Labs/types/console_fetch_tiers_response.py">ConsoleFetchTiersResponse</a></code>

## Token

Methods:

- <code title="post /console/token/create">client.console.token.<a href="./src/Deasy_Labs/resources/console/token.py">create</a>(\*\*<a href="src/Deasy_Labs/types/console/token_create_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/admin/token_create_response.py">TokenCreateResponse</a></code>
- <code title="get /console/token/list">client.console.token.<a href="./src/Deasy_Labs/resources/console/token.py">list</a>() -> <a href="./src/Deasy_Labs/types/admin/token_list_response.py">TokenListResponse</a></code>
- <code title="delete /console/token/{token_id}">client.console.token.<a href="./src/Deasy_Labs/resources/console/token.py">delete</a>(token_id, \*\*<a href="src/Deasy_Labs/types/console/token_delete_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/admin/token_delete_response.py">TokenDeleteResponse</a></code>

## Subscription

Types:

```python
from Deasy_Labs.types.console import SubscriptionRetrieveResponse
```

Methods:

- <code title="get /console/subscription">client.console.subscription.<a href="./src/Deasy_Labs/resources/console/subscription/subscription.py">retrieve</a>() -> <a href="./src/Deasy_Labs/types/console/subscription_retrieve_response.py">SubscriptionRetrieveResponse</a></code>

### Stripe

Types:

```python
from Deasy_Labs.types.console.subscription import (
    StripeCancelResponse,
    StripeCreateSessionResponse,
    StripeValidateResponse,
)
```

Methods:

- <code title="post /console/subscription/stripe/unsubscribe">client.console.subscription.stripe.<a href="./src/Deasy_Labs/resources/console/subscription/stripe.py">cancel</a>() -> <a href="./src/Deasy_Labs/types/console/subscription/stripe_cancel_response.py">StripeCancelResponse</a></code>
- <code title="post /console/subscription/stripe/payment">client.console.subscription.stripe.<a href="./src/Deasy_Labs/resources/console/subscription/stripe.py">create_session</a>(\*\*<a href="src/Deasy_Labs/types/console/subscription/stripe_create_session_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/console/subscription/stripe_create_session_response.py">StripeCreateSessionResponse</a></code>
- <code title="post /console/subscription/stripe/validate">client.console.subscription.stripe.<a href="./src/Deasy_Labs/resources/console/subscription/stripe.py">validate</a>() -> <a href="./src/Deasy_Labs/types/console/subscription/stripe_validate_response.py">StripeValidateResponse</a></code>

## Secret

Types:

```python
from Deasy_Labs.types.console import SecretGetResponse, SecretStoreResponse
```

Methods:

- <code title="post /console/secret/get">client.console.secret.<a href="./src/Deasy_Labs/resources/console/secret.py">get</a>(\*\*<a href="src/Deasy_Labs/types/console/secret_get_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/console/secret_get_response.py">SecretGetResponse</a></code>
- <code title="post /console/secret/store">client.console.secret.<a href="./src/Deasy_Labs/resources/console/secret.py">store</a>(\*\*<a href="src/Deasy_Labs/types/console/secret_store_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/console/secret_store_response.py">SecretStoreResponse</a></code>

## Vdbconnector

Types:

```python
from Deasy_Labs.types.console import VdbconnectorDeleteResponse, VdbconnectorGetDeleteStatsResponse
```

Methods:

- <code title="post /console/vdbconnector/delete">client.console.vdbconnector.<a href="./src/Deasy_Labs/resources/console/vdbconnector.py">delete</a>(\*\*<a href="src/Deasy_Labs/types/console/vdbconnector_delete_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/console/vdbconnector_delete_response.py">VdbconnectorDeleteResponse</a></code>
- <code title="post /console/vdbconnector/delete_stats">client.console.vdbconnector.<a href="./src/Deasy_Labs/resources/console/vdbconnector.py">get_delete_stats</a>(\*\*<a href="src/Deasy_Labs/types/console/vdbconnector_get_delete_stats_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/console/vdbconnector_get_delete_stats_response.py">VdbconnectorGetDeleteStatsResponse</a></code>

## LlmProvider

Types:

```python
from Deasy_Labs.types.console import LlmProviderValidateResponse
```

Methods:

- <code title="post /console/llm-provider/validate">client.console.llm_provider.<a href="./src/Deasy_Labs/resources/console/llm_provider.py">validate</a>(\*\*<a href="src/Deasy_Labs/types/console/llm_provider_validate_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/console/llm_provider_validate_response.py">LlmProviderValidateResponse</a></code>

## Marketplace

Types:

```python
from Deasy_Labs.types.console import MarketplaceSignupResponse
```

Methods:

- <code title="post /console/marketplace/signup">client.console.marketplace.<a href="./src/Deasy_Labs/resources/console/marketplace.py">signup</a>(\*\*<a href="src/Deasy_Labs/types/console/marketplace_signup_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/console/marketplace_signup_response.py">MarketplaceSignupResponse</a></code>

## VectorDB

Types:

```python
from Deasy_Labs.types.console import VectorDBCheckIndexesResponse, VectorDBValidateResponse
```

Methods:

- <code title="post /console/vector-db/check-index-fields">client.console.vector_db.<a href="./src/Deasy_Labs/resources/console/vector_db.py">check_indexes</a>(\*\*<a href="src/Deasy_Labs/types/console/vector_db_check_indexes_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/console/vector_db_check_indexes_response.py">VectorDBCheckIndexesResponse</a></code>
- <code title="post /console/vector-db/validate">client.console.vector_db.<a href="./src/Deasy_Labs/resources/console/vector_db.py">validate</a>(\*\*<a href="src/Deasy_Labs/types/console/vector_db_validate_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/console/vector_db_validate_response.py">VectorDBValidateResponse</a></code>

## User

Types:

```python
from Deasy_Labs.types.console import UserUpdateProfileResponse
```

Methods:

- <code title="post /console/user/profile">client.console.user.<a href="./src/Deasy_Labs/resources/console/user.py">update_profile</a>(\*\*<a href="src/Deasy_Labs/types/console/user_update_profile_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/console/user_update_profile_response.py">UserUpdateProfileResponse</a></code>

## Webhook

Types:

```python
from Deasy_Labs.types.console import WebhookHandleStripeResponse
```

Methods:

- <code title="post /console/webhook/stripe">client.console.webhook.<a href="./src/Deasy_Labs/resources/console/webhook.py">handle_stripe</a>() -> <a href="./src/Deasy_Labs/types/console/webhook_handle_stripe_response.py">object</a></code>

# Classify

Types:

```python
from Deasy_Labs.types import ClassifyClassifyAllResponse, ClassifyClassifyFilesResponse
```

Methods:

- <code title="post /classify/all">client.classify.<a href="./src/Deasy_Labs/resources/classify.py">classify_all</a>(\*\*<a href="src/Deasy_Labs/types/classify_classify_all_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/classify_classify_all_response.py">ClassifyClassifyAllResponse</a></code>
- <code title="post /classify">client.classify.<a href="./src/Deasy_Labs/resources/classify.py">classify_files</a>(\*\*<a href="src/Deasy_Labs/types/classify_classify_files_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/classify_classify_files_response.py">ClassifyClassifyFilesResponse</a></code>

# SuggestHierarchy

Types:

```python
from Deasy_Labs.types import SuggestHierarchySuggestResponse
```

Methods:

- <code title="post /suggest_hierarchy">client.suggest_hierarchy.<a href="./src/Deasy_Labs/resources/suggest_hierarchy.py">suggest</a>(\*\*<a href="src/Deasy_Labs/types/suggest_hierarchy_suggest_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/suggest_hierarchy_suggest_response.py">SuggestHierarchySuggestResponse</a></code>

# RefineTag

Types:

```python
from Deasy_Labs.types import RefineTagRefineResponse
```

Methods:

- <code title="post /refine_tag">client.refine_tag.<a href="./src/Deasy_Labs/resources/refine_tag.py">refine</a>(\*\*<a href="src/Deasy_Labs/types/refine_tag_refine_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/refine_tag_refine_response.py">RefineTagRefineResponse</a></code>

# TagText

Types:

```python
from Deasy_Labs.types import TagTextClassifyResponse
```

Methods:

- <code title="post /tag_text">client.tag_text.<a href="./src/Deasy_Labs/resources/tag_text.py">classify</a>(\*\*<a href="src/Deasy_Labs/types/tag_text_classify_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/tag_text_classify_response.py">TagTextClassifyResponse</a></code>

# GenerateFileTags

Types:

```python
from Deasy_Labs.types import GenerateFileTagCreateResponse
```

Methods:

- <code title="post /generate_file_tags">client.generate_file_tags.<a href="./src/Deasy_Labs/resources/generate_file_tags.py">create</a>(\*\*<a href="src/Deasy_Labs/types/generate_file_tag_create_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/generate_file_tag_create_response.py">GenerateFileTagCreateResponse</a></code>

# Contextualize

Types:

```python
from Deasy_Labs.types import ContextualizeCreateResponse
```

Methods:

- <code title="post /contextualize">client.contextualize.<a href="./src/Deasy_Labs/resources/contextualize.py">create</a>(\*\*<a href="src/Deasy_Labs/types/contextualize_create_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/contextualize_create_response.py">ContextualizeCreateResponse</a></code>

# SuggestDescription

Types:

```python
from Deasy_Labs.types import SuggestDescriptionCreateResponse
```

Methods:

- <code title="post /suggest_description">client.suggest_description.<a href="./src/Deasy_Labs/resources/suggest_description.py">create</a>(\*\*<a href="src/Deasy_Labs/types/suggest_description_create_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/suggest_description_create_response.py">SuggestDescriptionCreateResponse</a></code>

# Data

Types:

```python
from Deasy_Labs.types import (
    DataGetDocumentTextResponse,
    DataGetVdbTotalFilesResponse,
    DataListPaginatedResponse,
)
```

Methods:

- <code title="post /data/document_text">client.data.<a href="./src/Deasy_Labs/resources/data/data.py">get_document_text</a>(\*\*<a href="src/Deasy_Labs/types/data_get_document_text_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/data_get_document_text_response.py">DataGetDocumentTextResponse</a></code>
- <code title="post /data/file_count">client.data.<a href="./src/Deasy_Labs/resources/data/data.py">get_vdb_total_files</a>(\*\*<a href="src/Deasy_Labs/types/data_get_vdb_total_files_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/data_get_vdb_total_files_response.py">DataGetVdbTotalFilesResponse</a></code>
- <code title="post /data/list_paginated">client.data.<a href="./src/Deasy_Labs/resources/data/data.py">list_paginated</a>(\*\*<a href="src/Deasy_Labs/types/data_list_paginated_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/data_list_paginated_response.py">DataListPaginatedResponse</a></code>

## Metadata

Types:

```python
from Deasy_Labs.types.data import MetadataListResponse, MetadataDeleteResponse
```

Methods:

- <code title="post /data/metadata/list">client.data.metadata.<a href="./src/Deasy_Labs/resources/data/metadata.py">list</a>(\*\*<a href="src/Deasy_Labs/types/data/metadata_list_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/data/metadata_list_response.py">MetadataListResponse</a></code>
- <code title="post /data/metadata/delete">client.data.metadata.<a href="./src/Deasy_Labs/resources/data/metadata.py">delete</a>(\*\*<a href="src/Deasy_Labs/types/data/metadata_delete_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/data/metadata_delete_response.py">MetadataDeleteResponse</a></code>

# Tags

Types:

```python
from Deasy_Labs.types import (
    DeasyTag,
    TagCreateResponse,
    TagUpdateResponse,
    TagListResponse,
    TagDeleteResponse,
    TagGetDeleteStatsResponse,
)
```

Methods:

- <code title="post /tags/create">client.tags.<a href="./src/Deasy_Labs/resources/tags/tags.py">create</a>(\*\*<a href="src/Deasy_Labs/types/tag_create_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/tag_create_response.py">TagCreateResponse</a></code>
- <code title="put /tags/update">client.tags.<a href="./src/Deasy_Labs/resources/tags/tags.py">update</a>(\*\*<a href="src/Deasy_Labs/types/tag_update_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/tag_update_response.py">TagUpdateResponse</a></code>
- <code title="get /tags/list">client.tags.<a href="./src/Deasy_Labs/resources/tags/tags.py">list</a>() -> <a href="./src/Deasy_Labs/types/tag_list_response.py">TagListResponse</a></code>
- <code title="delete /tags/delete">client.tags.<a href="./src/Deasy_Labs/resources/tags/tags.py">delete</a>(\*\*<a href="src/Deasy_Labs/types/tag_delete_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/tag_delete_response.py">TagDeleteResponse</a></code>
- <code title="post /tags/delete_stats">client.tags.<a href="./src/Deasy_Labs/resources/tags/tags.py">get_delete_stats</a>(\*\*<a href="src/Deasy_Labs/types/tag_get_delete_stats_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/tag_get_delete_stats_response.py">TagGetDeleteStatsResponse</a></code>

## Groups

Types:

```python
from Deasy_Labs.types.tags import (
    DeasyTagGroup,
    GroupCreateResponse,
    GroupUpdateResponse,
    GroupListResponse,
    GroupDeleteResponse,
)
```

Methods:

- <code title="post /tags/groups/create">client.tags.groups.<a href="./src/Deasy_Labs/resources/tags/groups.py">create</a>(\*\*<a href="src/Deasy_Labs/types/tags/group_create_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/tags/group_create_response.py">GroupCreateResponse</a></code>
- <code title="put /tags/groups/update">client.tags.groups.<a href="./src/Deasy_Labs/resources/tags/groups.py">update</a>(\*\*<a href="src/Deasy_Labs/types/tags/group_update_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/tags/group_update_response.py">GroupUpdateResponse</a></code>
- <code title="get /tags/groups/list">client.tags.groups.<a href="./src/Deasy_Labs/resources/tags/groups.py">list</a>() -> <a href="./src/Deasy_Labs/types/tags/group_list_response.py">GroupListResponse</a></code>
- <code title="delete /tags/groups/delete">client.tags.groups.<a href="./src/Deasy_Labs/resources/tags/groups.py">delete</a>(\*\*<a href="src/Deasy_Labs/types/tags/group_delete_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/tags/group_delete_response.py">GroupDeleteResponse</a></code>

# Metadata

Types:

```python
from Deasy_Labs.types import (
    BasicMetadataRequest,
    HierarchyStatsNode,
    TagCondition,
    MetadataDeleteResponse,
    MetadataApplyStandardizationDBResponse,
    MetadataFilterByConditionsResponse,
    MetadataGetBasicMetadataResponse,
    MetadataGetCountDistributionsResponse,
    MetadataGetDistinctValuesResponse,
    MetadataGetDistributionsResponse,
    MetadataGetEvidenceResponse,
    MetadataGetFilteredMetadataResponse,
    MetadataGetOobTagFileCountResponse,
    MetadataGetTagStatisticsResponse,
    MetadataGetUniqueTagsResponse,
    MetadataSuggestStandardizationResponse,
)
```

Methods:

- <code title="post /metadata/delete">client.metadata.<a href="./src/Deasy_Labs/resources/metadata/metadata.py">delete</a>(\*\*<a href="src/Deasy_Labs/types/metadata_delete_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/metadata_delete_response.py">MetadataDeleteResponse</a></code>
- <code title="post /metadata/standardization_db">client.metadata.<a href="./src/Deasy_Labs/resources/metadata/metadata.py">apply_standardization_db</a>(\*\*<a href="src/Deasy_Labs/types/metadata_apply_standardization_db_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/metadata_apply_standardization_db_response.py">MetadataApplyStandardizationDBResponse</a></code>
- <code title="post /metadata/conditional_filter">client.metadata.<a href="./src/Deasy_Labs/resources/metadata/metadata.py">filter_by_conditions</a>(\*\*<a href="src/Deasy_Labs/types/metadata_filter_by_conditions_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/metadata_filter_by_conditions_response.py">MetadataFilterByConditionsResponse</a></code>
- <code title="post /metadata/basic">client.metadata.<a href="./src/Deasy_Labs/resources/metadata/metadata.py">get_basic_metadata</a>(\*\*<a href="src/Deasy_Labs/types/metadata_get_basic_metadata_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/metadata_get_basic_metadata_response.py">MetadataGetBasicMetadataResponse</a></code>
- <code title="post /metadata/count_distributions">client.metadata.<a href="./src/Deasy_Labs/resources/metadata/metadata.py">get_count_distributions</a>(\*\*<a href="src/Deasy_Labs/types/metadata_get_count_distributions_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/metadata_get_count_distributions_response.py">MetadataGetCountDistributionsResponse</a></code>
- <code title="post /metadata/distinct_values">client.metadata.<a href="./src/Deasy_Labs/resources/metadata/metadata.py">get_distinct_values</a>(\*\*<a href="src/Deasy_Labs/types/metadata_get_distinct_values_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/metadata_get_distinct_values_response.py">MetadataGetDistinctValuesResponse</a></code>
- <code title="post /metadata/distributions">client.metadata.<a href="./src/Deasy_Labs/resources/metadata/metadata.py">get_distributions</a>(\*\*<a href="src/Deasy_Labs/types/metadata_get_distributions_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/metadata_get_distributions_response.py">MetadataGetDistributionsResponse</a></code>
- <code title="post /metadata/get_evidence">client.metadata.<a href="./src/Deasy_Labs/resources/metadata/metadata.py">get_evidence</a>(\*\*<a href="src/Deasy_Labs/types/metadata_get_evidence_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/metadata_get_evidence_response.py">MetadataGetEvidenceResponse</a></code>
- <code title="post /metadata/filtered">client.metadata.<a href="./src/Deasy_Labs/resources/metadata/metadata.py">get_filtered_metadata</a>(\*\*<a href="src/Deasy_Labs/types/metadata_get_filtered_metadata_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/metadata_get_filtered_metadata_response.py">MetadataGetFilteredMetadataResponse</a></code>
- <code title="post /metadata/oob_tag_file_count">client.metadata.<a href="./src/Deasy_Labs/resources/metadata/metadata.py">get_oob_tag_file_count</a>(\*\*<a href="src/Deasy_Labs/types/metadata_get_oob_tag_file_count_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/metadata_get_oob_tag_file_count_response.py">MetadataGetOobTagFileCountResponse</a></code>
- <code title="post /metadata/tag_statistics">client.metadata.<a href="./src/Deasy_Labs/resources/metadata/metadata.py">get_tag_statistics</a>(\*\*<a href="src/Deasy_Labs/types/metadata_get_tag_statistics_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/metadata_get_tag_statistics_response.py">MetadataGetTagStatisticsResponse</a></code>
- <code title="post /metadata/get_unique_tags">client.metadata.<a href="./src/Deasy_Labs/resources/metadata/metadata.py">get_unique_tags</a>(\*\*<a href="src/Deasy_Labs/types/metadata_get_unique_tags_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/metadata_get_unique_tags_response.py">MetadataGetUniqueTagsResponse</a></code>
- <code title="post /metadata/standardization_suggest">client.metadata.<a href="./src/Deasy_Labs/resources/metadata/metadata.py">suggest_standardization</a>(\*\*<a href="src/Deasy_Labs/types/metadata_suggest_standardization_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/metadata_suggest_standardization_response.py">MetadataSuggestStandardizationResponse</a></code>

## File

Types:

```python
from Deasy_Labs.types.metadata import FileListResponse
```

Methods:

- <code title="post /metadata/file/list">client.metadata.file.<a href="./src/Deasy_Labs/resources/metadata/file.py">list</a>(\*\*<a href="src/Deasy_Labs/types/metadata/file_list_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/metadata/file_list_response.py">FileListResponse</a></code>

## Chunk

Types:

```python
from Deasy_Labs.types.metadata import ChunkListResponse
```

Methods:

- <code title="post /metadata/chunk/list">client.metadata.chunk.<a href="./src/Deasy_Labs/resources/metadata/chunk.py">list</a>(\*\*<a href="src/Deasy_Labs/types/metadata/chunk_list_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/metadata/chunk_list_response.py">ChunkListResponse</a></code>

## Standardize

Types:

```python
from Deasy_Labs.types.metadata import (
    StandardizeListResponse,
    StandardizeGetTagDistributionResponse,
    StandardizeInsertResponse,
)
```

Methods:

- <code title="post /metadata/standardize/list">client.metadata.standardize.<a href="./src/Deasy_Labs/resources/metadata/standardize.py">list</a>(\*\*<a href="src/Deasy_Labs/types/metadata/standardize_list_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/metadata/standardize_list_response.py">object</a></code>
- <code title="post /metadata/standardize/tag_distribution">client.metadata.standardize.<a href="./src/Deasy_Labs/resources/metadata/standardize.py">get_tag_distribution</a>(\*\*<a href="src/Deasy_Labs/types/metadata/standardize_get_tag_distribution_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/metadata/standardize_get_tag_distribution_response.py">StandardizeGetTagDistributionResponse</a></code>
- <code title="post /metadata/standardize/insert">client.metadata.standardize.<a href="./src/Deasy_Labs/resources/metadata/standardize.py">insert</a>(\*\*<a href="src/Deasy_Labs/types/metadata/standardize_insert_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/metadata/standardize_insert_response.py">object</a></code>

# Usecase

Types:

```python
from Deasy_Labs.types import (
    Condition,
    UsecaseCreateResponse,
    UsecaseListResponse,
    UsecaseDeleteResponse,
    UsecaseCheckSyncResponse,
    UsecaseGetFileCountResponse,
    UsecaseGetFilesResponse,
    UsecaseGetMetricsResponse,
    UsecaseGetTagVdbDistributionResponse,
)
```

Methods:

- <code title="post /usecase/create">client.usecase.<a href="./src/Deasy_Labs/resources/usecase/usecase.py">create</a>(\*\*<a href="src/Deasy_Labs/types/usecase_create_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/usecase_create_response.py">UsecaseCreateResponse</a></code>
- <code title="get /usecase/list">client.usecase.<a href="./src/Deasy_Labs/resources/usecase/usecase.py">list</a>() -> <a href="./src/Deasy_Labs/types/usecase_list_response.py">UsecaseListResponse</a></code>
- <code title="delete /usecase/delete">client.usecase.<a href="./src/Deasy_Labs/resources/usecase/usecase.py">delete</a>(\*\*<a href="src/Deasy_Labs/types/usecase_delete_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/usecase_delete_response.py">UsecaseDeleteResponse</a></code>
- <code title="post /usecase/sync_score">client.usecase.<a href="./src/Deasy_Labs/resources/usecase/usecase.py">check_sync</a>(\*\*<a href="src/Deasy_Labs/types/usecase_check_sync_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/usecase_check_sync_response.py">UsecaseCheckSyncResponse</a></code>
- <code title="post /usecase/file_count">client.usecase.<a href="./src/Deasy_Labs/resources/usecase/usecase.py">get_file_count</a>(\*\*<a href="src/Deasy_Labs/types/usecase_get_file_count_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/usecase_get_file_count_response.py">UsecaseGetFileCountResponse</a></code>
- <code title="post /usecase/files">client.usecase.<a href="./src/Deasy_Labs/resources/usecase/usecase.py">get_files</a>(\*\*<a href="src/Deasy_Labs/types/usecase_get_files_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/usecase_get_files_response.py">UsecaseGetFilesResponse</a></code>
- <code title="post /usecase/metrics">client.usecase.<a href="./src/Deasy_Labs/resources/usecase/usecase.py">get_metrics</a>(\*\*<a href="src/Deasy_Labs/types/usecase_get_metrics_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/usecase_get_metrics_response.py">UsecaseGetMetricsResponse</a></code>
- <code title="post /usecase/tag_vdb_distribution">client.usecase.<a href="./src/Deasy_Labs/resources/usecase/usecase.py">get_tag_vdb_distribution</a>(\*\*<a href="src/Deasy_Labs/types/usecase_get_tag_vdb_distribution_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/usecase_get_tag_vdb_distribution_response.py">UsecaseGetTagVdbDistributionResponse</a></code>

## Export

Types:

```python
from Deasy_Labs.types.usecase import ExportMetadataResponse, ExportToVdbResponse
```

Methods:

- <code title="post /usecase/export/metadata">client.usecase.export.<a href="./src/Deasy_Labs/resources/usecase/export.py">metadata</a>(\*\*<a href="src/Deasy_Labs/types/usecase/export_metadata_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/usecase/export_metadata_response.py">object</a></code>
- <code title="post /usecase/export/vdb">client.usecase.export.<a href="./src/Deasy_Labs/resources/usecase/export.py">to_vdb</a>(\*\*<a href="src/Deasy_Labs/types/usecase/export_to_vdb_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/usecase/export_to_vdb_response.py">ExportToVdbResponse</a></code>

# Graph

Types:

```python
from Deasy_Labs.types import GraphListResponse, GraphDeleteResponse, GraphCreateOrUpdateResponse
```

Methods:

- <code title="post /graph/list">client.graph.<a href="./src/Deasy_Labs/resources/graph.py">list</a>(\*\*<a href="src/Deasy_Labs/types/graph_list_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/graph_list_response.py">GraphListResponse</a></code>
- <code title="delete /graph/delete">client.graph.<a href="./src/Deasy_Labs/resources/graph.py">delete</a>(\*\*<a href="src/Deasy_Labs/types/graph_delete_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/graph_delete_response.py">GraphDeleteResponse</a></code>
- <code title="post /graph/upsert">client.graph.<a href="./src/Deasy_Labs/resources/graph.py">create_or_update</a>(\*\*<a href="src/Deasy_Labs/types/graph_create_or_update_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/graph_create_or_update_response.py">GraphCreateOrUpdateResponse</a></code>

# Ocr

Types:

```python
from Deasy_Labs.types import OcrGetSyncStatsResponse, OcrIngestResponse
```

Methods:

- <code title="post /ocr/sync_stats">client.ocr.<a href="./src/Deasy_Labs/resources/ocr.py">get_sync_stats</a>(\*\*<a href="src/Deasy_Labs/types/ocr_get_sync_stats_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/ocr_get_sync_stats_response.py">object</a></code>
- <code title="post /ocr/ingest">client.ocr.<a href="./src/Deasy_Labs/resources/ocr.py">ingest</a>(\*\*<a href="src/Deasy_Labs/types/ocr_ingest_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/ocr_ingest_response.py">object</a></code>

# ProgressTracker

Types:

```python
from Deasy_Labs.types import (
    ProgressTrackerAbortProgressTrackerResponse,
    ProgressTrackerDeleteProgressTrackersResponse,
    ProgressTrackerListProgressTrackersResponse,
    ProgressTrackerRetrieveTaskStatusResponse,
)
```

Methods:

- <code title="put /progress_tracker/abort_progress_tracker/{tracker_id}">client.progress_tracker.<a href="./src/Deasy_Labs/resources/progress_tracker.py">abort_progress_tracker</a>(tracker_id) -> <a href="./src/Deasy_Labs/types/progress_tracker_abort_progress_tracker_response.py">object</a></code>
- <code title="post /progress_tracker/delete_progress_trackers">client.progress_tracker.<a href="./src/Deasy_Labs/resources/progress_tracker.py">delete_progress_trackers</a>(\*\*<a href="src/Deasy_Labs/types/progress_tracker_delete_progress_trackers_params.py">params</a>) -> <a href="./src/Deasy_Labs/types/progress_tracker_delete_progress_trackers_response.py">ProgressTrackerDeleteProgressTrackersResponse</a></code>
- <code title="get /progress_tracker/get_progress_trackers">client.progress_tracker.<a href="./src/Deasy_Labs/resources/progress_tracker.py">list_progress_trackers</a>() -> <a href="./src/Deasy_Labs/types/progress_tracker_list_progress_trackers_response.py">ProgressTrackerListProgressTrackersResponse</a></code>
- <code title="get /progress_tracker/task_status/{job_id}">client.progress_tracker.<a href="./src/Deasy_Labs/resources/progress_tracker.py">retrieve_task_status</a>(job_id) -> <a href="./src/Deasy_Labs/types/progress_tracker_retrieve_task_status_response.py">ProgressTrackerRetrieveTaskStatusResponse</a></code>

# Health

Types:

```python
from Deasy_Labs.types import HealthCheckResponse
```

Methods:

- <code title="get /health">client.health.<a href="./src/Deasy_Labs/resources/health.py">check</a>() -> <a href="./src/Deasy_Labs/types/health_check_response.py">object</a></code>
