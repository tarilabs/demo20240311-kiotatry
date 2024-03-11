import asyncio
from kiota_abstractions.authentication.anonymous_authentication_provider import (
    AnonymousAuthenticationProvider)
from kiota_http.httpx_request_adapter import HttpxRequestAdapter
from client.posts_client import PostsClient
from client.models.registered_model_create import RegisteredModelCreate

# jump to source code:
from client.models.registered_model import RegisteredModel
from client.models.base_resource_list import BaseResourceList

async def main():
    auth_provider = AnonymousAuthenticationProvider()
    request_adapter = HttpxRequestAdapter(auth_provider, base_url="http://localhost:8080")
    client = PostsClient(request_adapter)

    all_posts: BaseResourceList = await client.api.model_registry.v1alpha2.registered_models.get()
    print(f"Retrieved {len(all_posts.items)} registered_models.")
    print(all_posts)
    # TODO: problem1, OpenAPI operationId `getRegisteredModels`, on 200 returns "#/components/responses/RegisteredModelListResponse",
    # but here `all_posts` from .get() is of type: BaseResourceList(ModelVersionList)
    # looks like I'm missing all the variation of ~ List<RegisteredModel>, List<ModelArtifact>, etc.
    # (while model_version_list.py is generated, looks there is no equivalence of model_artifact_list.py, registered_model_list.py, etc)
    # see also: https://editor.swagger.io/?url=https://raw.githubusercontent.com/kubeflow/model-registry/main/api/openapi/model-registry.yaml#:~:text=GET-,/api/model_registry/v1alpha2/registered_models,-List%20All%20RegisteredModels

    new_reg_model = RegisteredModelCreate(name="mnist2")
    new_reg_model.description = "lorem ipsum"
    registered_model: RegisteredModel = await client.api.model_registry.v1alpha2.registered_models.post(new_reg_model)
    print(f"Created new post with ID: {registered_model}")
    # TODO: problem2, OpenAPI operationId `createRegisteredModel`, on 200 returns "#/components/responses/RegisteredModelResponse"
    # but here `registered_model` from .post() is of type: RegisteredModel
    # and client.models.registered_model.RegisteredModel is "empty", missing of any attributes.
    # see also: https://editor.swagger.io/?url=https://raw.githubusercontent.com/kubeflow/model-registry/main/api/openapi/model-registry.yaml#:~:text=POST-,/api/model_registry/v1alpha2/registered_models,-Create%20a%20RegisteredModel


asyncio.run(main())