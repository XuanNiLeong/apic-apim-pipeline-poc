# Automate deployment and registration of API to APIM and API Center

This is a respository with sample pipeline showing how to automate deployment and registration of API to APIM and API Center. 

## Steps to set this up:
1. Pre-requisite. Make sure you have an instance of APIM and APIC provisioned. 

2. Create a Microsoft Entra ID service principal to access both APIM and APIC, which will be used to add credentials to the workflow to authenticate with Azure. 

    ```bash
    #! /bin/bash
    apiCenter=<api-center-name>
    resourceGroup=<resource-group-name>
    spName=<service-principal-name>

    apicResourceId=$(az apic show --name $apiCenter --resource-group $resourceGroup --query "id" --output tsv)

    az ad sp create-for-rbac --name $spName --role contributor \
                                --scopes $apicResourceId \
                                --json-auth
    ```

    Copy the JSON output and add the service principal as a GitHub secret. 

    For more information: 
    - https://learn.microsoft.com/en-gb/azure/api-center/register-apis-github-actions?tabs=bash#set-up-a-service-principal-secret
    - https://learn.microsoft.com/en-gb/azure/app-service/deploy-github-actions?tabs=userlevel%2Caspnetcore#generate-deployment-credentials

3. Grant permissions to APIC to import deployments from APIM. 

    ```properties
    1. Turn on System Assigned Managed Identity for your APIC instance. 
    2. Grant the 'API Management Service Reader Role' to your APIM instance and assign it to your APIC Managed Identity. 
    ```

    For more information: https://www.youtube.com/watch?v=SuGkhuBUV5k 

4. Clone this repository, create an `.env` file with these environment variables:
    
    ```properties
    RESOURCE_GROUP: #your resource group name
    APIC_SERVICE_NAME: #name of your apic instance
    APIM_SERVICE_NAME: #name of your apim instance 
    SPECIFICATION_FILE_PATH: ./APIs/catstore-api/catstore.yaml #change this to your API file location you want to register
    API_ID: catstore #change this to your API url suffix you want 
    LIFECYCLE_STAGE: development #Accepted values: deprecated, design, development, preview, production, retired, testing
    DEFINITION_ID: openapi #change this to your API definition id you want to register
    ```

5. Make a pull request to trigger the workflow. Once the pull request is approved and merged into the main branch, the workflow will be triggered. 

6. Verify deployments in APIM and APIC. 