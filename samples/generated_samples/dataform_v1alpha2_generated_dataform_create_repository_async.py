# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Generated code. DO NOT EDIT!
#
# Snippet for CreateRepository
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-dataform


# [START dataform_v1alpha2_generated_Dataform_CreateRepository_async]
from google.cloud import dataform_v1alpha2


async def sample_create_repository():
    # Create a client
    client = dataform_v1alpha2.DataformAsyncClient()

    # Initialize request argument(s)
    request = dataform_v1alpha2.CreateRepositoryRequest(
        parent="parent_value",
        repository_id="repository_id_value",
    )

    # Make the request
    response = await client.create_repository(request=request)

    # Handle the response
    print(response)

# [END dataform_v1alpha2_generated_Dataform_CreateRepository_async]