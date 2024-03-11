from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .......models.artifact import Artifact
    from .......models.base_resource_list import BaseResourceList
    from .......models.error import Error
    from .......models.order_by_field import OrderByField
    from .......models.sort_order import SortOrder

class ArtifactsRequestBuilder(BaseRequestBuilder):
    """
    The REST endpoint/path used to list and create zero or more `Artifact` entities for a `ModelVersion`.  This path contains a `GET` and `POST` operation to perform the list and create tasks, respectively.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new ArtifactsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/model_registry/v1alpha2/model_versions/{modelversionId}/artifacts{?externalID*,name*,nextPageToken*,orderBy*,pageSize*,sortOrder*}", path_parameters)
    
    async def get(self,request_configuration: Optional[ArtifactsRequestBuilderGetRequestConfiguration] = None) -> Optional[BaseResourceList]:
        """
        List all artifacts associated with the `ModelVersion`
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[BaseResourceList]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .......models.error import Error

        error_mapping: Dict[str, ParsableFactory] = {
            "401": Error,
            "404": Error,
            "500": Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.base_resource_list import BaseResourceList

        return await self.request_adapter.send_async(request_info, BaseResourceList, error_mapping)
    
    async def post(self,body: Optional[Artifact] = None, request_configuration: Optional[ArtifactsRequestBuilderPostRequestConfiguration] = None) -> Optional[Artifact]:
        """
        Creates a new instance of an Artifact if needed and associates it with `ModelVersion`.
        param body: A metadata Artifact Entity.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Artifact]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .......models.error import Error

        error_mapping: Dict[str, ParsableFactory] = {
            "400": Error,
            "401": Error,
            "404": Error,
            "500": Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.artifact import Artifact

        return await self.request_adapter.send_async(request_info, Artifact, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[ArtifactsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        List all artifacts associated with the `ModelVersion`
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: Optional[Artifact] = None, request_configuration: Optional[ArtifactsRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Creates a new instance of an Artifact if needed and associates it with `ModelVersion`.
        param body: A metadata Artifact Entity.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.POST
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> ArtifactsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ArtifactsRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return ArtifactsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class ArtifactsRequestBuilderGetQueryParameters():
        """
        List all artifacts associated with the `ModelVersion`
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "external_i_d":
                return "externalID"
            if original_name == "next_page_token":
                return "nextPageToken"
            if original_name == "order_by":
                return "orderBy"
            if original_name == "page_size":
                return "pageSize"
            if original_name == "sort_order":
                return "sortOrder"
            if original_name == "name":
                return "name"
            return original_name
        
        # External ID of entity to search.
        external_i_d: Optional[str] = None

        # Name of entity to search.
        name: Optional[str] = None

        # Token to use to retrieve next page of results.
        next_page_token: Optional[str] = None

        # Specifies the order by criteria for listing entities.
        order_by: Optional[OrderByField] = None

        # Number of entities in each page.
        page_size: Optional[str] = None

        # Specifies the sort order for listing entities, defaults to ASC.
        sort_order: Optional[SortOrder] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class ArtifactsRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[ArtifactsRequestBuilder.ArtifactsRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class ArtifactsRequestBuilderPostRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

