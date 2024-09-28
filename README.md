# az_functions_poc1 - Blob Storage Integration with Azure Functions and CI/CD Pipeline
##Overview

This project demonstrates a serverless solution using Azure Functions to download data from an external API and store it in Azure Blob Storage. The function uses Azure Key Vault to securely retrieve sensitive information, such as the storage account key. The project is also integrated with Azure Pipelines to ensure continuous integration and delivery (CI/CD). The pipeline automates testing, packaging, and artifact publishing.

The purpose of the project is to provide a scalable, secure, and automated way to ingest external data into Azure storage for future processing or analysis.
## Tech Stack

    Azure Functions: Serverless compute service used to run the function triggered by HTTP requests.
    Azure Blob Storage: Scalable object storage for saving the downloaded data.
    Azure Key Vault: Securely stores and manages sensitive information, such as connection strings and secrets.
    Azure Pipelines: Continuous integration and delivery tool for automating testing and deployment.
    Python: Main programming language for writing the Azure Function.
    Azure SDKs: Libraries for interacting with Azure services (e.g., Blob Storage, Key Vault, etc.).
    PyTest: Framework used for running unit tests.

## Functions

    Download Data from API:
        The function periodically fetches data from an external API, in this case, a CSV file.
        It uses the requests library to handle HTTP GET requests.

    Secure Storage Access:
        The function retrieves the storage account key from Azure Key Vault using DefaultAzureCredential.
        This ensures that no sensitive data, such as keys or connection strings, are hardcoded in the function.

    Blob Storage Interaction:
        Once the data is fetched from the API, it is uploaded to Azure Blob Storage.
        The function checks if the storage container exists, creates it if not, and uploads the data.

    HTTP Trigger:
        The function is triggered by an HTTP request, which means it can be called on-demand.
        This provides flexibility in how often and when the function is executed.

## CI/CD Integration

The project uses Azure Pipelines to automate the build, test, and deployment process. This ensures that the code is always tested before being deployed, providing a robust and reliable solution.
CI/CD Features:

    Automatic Trigger: The pipeline is triggered on each push or pull request to the master branch, ensuring that changes are automatically tested and deployed.
    Python Version Management: The pipeline specifies the Python version (3.11) for consistency across environments.
    Dependency Installation: The pipeline installs all the necessary dependencies from the requirements.txt file.
    Unit Testing: The pipeline runs unit tests using PyTest and publishes the results in JUnit XML format.
    Artifact Archiving: After a successful build and test run, the build artifacts are archived and published for deployment.
