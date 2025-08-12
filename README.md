# Generative Prompt Engineering
The Generative Prompt Engineering tool is a portable Python package that can be used to iterate rapidly over experimental prompts when installed in any Python environment, including local, notebook or pipeline.

The package implements Google Cloud Platform Vertex AI generative models and services using the Python [genai](https://googleapis.github.io/python-genai/) SDK, and the Python [mcp](https://modelcontextprotocol.io/) SDK.

The package uses the  Astral ```uv --package``` template and implements essential package configuration, dependencies, versioning, pre-commit checks, and unit tests.

## Getting Started
In order to effectively manage cross-platform requirements between developers, environments and pipelines, this package uses Astral [uv](https://docs.astral.sh/uv/getting-started/). This is a powerful cross-platform Python package manager that does the right things, and is very easy to learn.

1. Install git, make and [uv](https://docs.astral.sh/uv/getting-started/installation/) in your environment.
2. Clone the [generative-prompt-engineering](https://github.com/kpeder/generative-prompt-engineering.git) repository.
3. Configure a GCP project with the Vertex AI API, and [authenticate](https://cloud.google.com/docs/authentication/provide-credentials-adc) with application default credentials using gcloud. You may need to set your [quota](https://cloud.google.com/docs/quotas/set-quota-project#set-project-credentials) project as well.
4. Test the package, for example: ```uv run pytest -v --cov --location us-central1 --project-id your-gcp-project```

## Contributing
Contributions are welcome. Established conventions should be followed for code structure, doc strings and unit tests.

Pre-commit checks and unit tests must pass.
