# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.usecase import export_to_vdb_params, export_metadata_params
from ...types.usecase.export_to_vdb_response import ExportToVdbResponse

__all__ = ["ExportResource", "AsyncExportResource"]


class ExportResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#accessing-raw-response-data-eg-headers
        """
        return ExportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#with_streaming_response
        """
        return ExportResourceWithStreamingResponse(self)

    def metadata(
        self,
        *,
        vector_db_config: object,
        export_both_levels: bool | NotGiven = NOT_GIVEN,
        export_chunk_level: bool | NotGiven = NOT_GIVEN,
        export_file_level: bool | NotGiven = NOT_GIVEN,
        export_format: Optional[Literal["json", "csv"]] | NotGiven = NOT_GIVEN,
        selected_metadata_fields: Optional[List[str]] | NotGiven = NOT_GIVEN,
        usecase_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Export file-level/chunk-level metadata for a use case

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/usecase/export/metadata",
            body=maybe_transform(
                {
                    "vector_db_config": vector_db_config,
                    "export_both_levels": export_both_levels,
                    "export_chunk_level": export_chunk_level,
                    "export_file_level": export_file_level,
                    "export_format": export_format,
                    "selected_metadata_fields": selected_metadata_fields,
                    "usecase_id": usecase_id,
                },
                export_metadata_params.ExportMetadataParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def to_vdb(
        self,
        *,
        target_vector_db_config: object,
        export_level: Literal["file", "chunk", "both"] | NotGiven = NOT_GIVEN,
        export_tags: Iterable[object] | NotGiven = NOT_GIVEN,
        ori_vector_db_config: Optional[object] | NotGiven = NOT_GIVEN,
        usecase_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExportToVdbResponse:
        """
        Export metadata for a use case to a target vector database

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/usecase/export/vdb",
            body=maybe_transform(
                {
                    "target_vector_db_config": target_vector_db_config,
                    "export_level": export_level,
                    "export_tags": export_tags,
                    "ori_vector_db_config": ori_vector_db_config,
                    "usecase_id": usecase_id,
                },
                export_to_vdb_params.ExportToVdbParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExportToVdbResponse,
        )


class AsyncExportResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/Deasy-Labs-python#with_streaming_response
        """
        return AsyncExportResourceWithStreamingResponse(self)

    async def metadata(
        self,
        *,
        vector_db_config: object,
        export_both_levels: bool | NotGiven = NOT_GIVEN,
        export_chunk_level: bool | NotGiven = NOT_GIVEN,
        export_file_level: bool | NotGiven = NOT_GIVEN,
        export_format: Optional[Literal["json", "csv"]] | NotGiven = NOT_GIVEN,
        selected_metadata_fields: Optional[List[str]] | NotGiven = NOT_GIVEN,
        usecase_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Export file-level/chunk-level metadata for a use case

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/usecase/export/metadata",
            body=await async_maybe_transform(
                {
                    "vector_db_config": vector_db_config,
                    "export_both_levels": export_both_levels,
                    "export_chunk_level": export_chunk_level,
                    "export_file_level": export_file_level,
                    "export_format": export_format,
                    "selected_metadata_fields": selected_metadata_fields,
                    "usecase_id": usecase_id,
                },
                export_metadata_params.ExportMetadataParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def to_vdb(
        self,
        *,
        target_vector_db_config: object,
        export_level: Literal["file", "chunk", "both"] | NotGiven = NOT_GIVEN,
        export_tags: Iterable[object] | NotGiven = NOT_GIVEN,
        ori_vector_db_config: Optional[object] | NotGiven = NOT_GIVEN,
        usecase_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExportToVdbResponse:
        """
        Export metadata for a use case to a target vector database

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/usecase/export/vdb",
            body=await async_maybe_transform(
                {
                    "target_vector_db_config": target_vector_db_config,
                    "export_level": export_level,
                    "export_tags": export_tags,
                    "ori_vector_db_config": ori_vector_db_config,
                    "usecase_id": usecase_id,
                },
                export_to_vdb_params.ExportToVdbParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExportToVdbResponse,
        )


class ExportResourceWithRawResponse:
    def __init__(self, export: ExportResource) -> None:
        self._export = export

        self.metadata = to_raw_response_wrapper(
            export.metadata,
        )
        self.to_vdb = to_raw_response_wrapper(
            export.to_vdb,
        )


class AsyncExportResourceWithRawResponse:
    def __init__(self, export: AsyncExportResource) -> None:
        self._export = export

        self.metadata = async_to_raw_response_wrapper(
            export.metadata,
        )
        self.to_vdb = async_to_raw_response_wrapper(
            export.to_vdb,
        )


class ExportResourceWithStreamingResponse:
    def __init__(self, export: ExportResource) -> None:
        self._export = export

        self.metadata = to_streamed_response_wrapper(
            export.metadata,
        )
        self.to_vdb = to_streamed_response_wrapper(
            export.to_vdb,
        )


class AsyncExportResourceWithStreamingResponse:
    def __init__(self, export: AsyncExportResource) -> None:
        self._export = export

        self.metadata = async_to_streamed_response_wrapper(
            export.metadata,
        )
        self.to_vdb = async_to_streamed_response_wrapper(
            export.to_vdb,
        )
