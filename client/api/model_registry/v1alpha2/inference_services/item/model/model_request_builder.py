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
    from .......models.error import Error
    from .......models.registered_model import RegisteredModel

class ModelRequestBuilder(BaseRequestBuilder):
    """
    The REST endpoint/path used to list the `RegisteredModel` entity for an `InferenceService`.  This path contains a `GET` operation to perform the get task.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new ModelRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/model_registry/v1alpha2/inference_services/{inferenceserviceId}/model", path_parameters)
    
    async def get(self,request_configuration: Optional[ModelRequestBuilderGetRequestConfiguration] = None) -> Optional[RegisteredModel]:
        """
        Gets the `RegisteredModel` entity for the `InferenceService`.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[RegisteredModel]
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
        from .......models.registered_model import RegisteredModel

        return await self.request_adapter.send_async(request_info, RegisteredModel, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[ModelRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Gets the `RegisteredModel` entity for the `InferenceService`.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> ModelRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ModelRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return ModelRequestBuilder(self.request_adapter, raw_url)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class ModelRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

