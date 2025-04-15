import os

def create_dir(path):
    """Create a directory if it doesn't already exist."""
    os.makedirs(path, exist_ok=True)
    print(f"Created directory: {path}")

def create_file(path):
    """Create an empty file (or overwrite if it already exists)."""
    # Ensure the parent directory exists
    parent_dir = os.path.dirname(path)
    if parent_dir and not os.path.exists(parent_dir):
        os.makedirs(parent_dir, exist_ok=True)
    with open(path, "w") as f:
        pass
    print(f"Created file: {path}")

# List of directories to create (relative to the current folder)
directories = [
    "airflow/dags",
    "airflow/plugins",
    "dbt/analysis",
    "dbt/data/seeds",
    "dbt/macros",
    "dbt/models/staging",
    "dbt/models/marts",
    "dbt/models/forecasts",
    "src/bundesbank_api",
    "src/data_processing",
    "docker",
    "tests"
]

# List of file paths to create (relative to the current folder)
files = [
    "airflow/dags/fetch_bundesbank_data_dag.py",    # DAG script
    "airflow/plugins/custom_operators.py",           # Custom operators
    "airflow/requirements.txt",                      # Airflow-specific dependencies
    "airflow/README.md",                             # README for Airflow
    "dbt/dbt_project.yml",                           # dbt project config
    "dbt/packages.yml",                              # Optional: dbt packages config
    "dbt/models/staging/stg_bundesbank_data.sql",    # Staging SQL model
    "dbt/models/marts/interest_rates.sql",           # Fact table: interest rates
    "dbt/models/marts/forecast_results.sql",         # Fact table: forecast outputs
    "dbt/models/forecasts/forecast_model_output.sql",# Forecast model output model
    "src/bundesbank_api/fetch_data.py",              # API fetch script
    "src/bundesbank_api/sdmx_parser.py",             # SDMX parser utility
    "src/bundesbank_api/common.py",                  # Common functionality
    "src/data_processing/transform_data.py",         # Data transformation script
    "src/data_processing/forecast.py",               # Forecasting script
    "src/requirements.txt",                          # Python libraries for src scripts
    "docker/Dockerfile",                             # Dockerfile for containerization
    "docker/docker-compose.yml",                     # Docker Compose file
    "tests/test_fetch_data.py",                      # Unit/integration test script
    ".gitignore",                                    # Git ignore file
    "README.md"                                      # Overall project documentation
]

# Create directories
for d in directories:
    create_dir(d)

# Create files
for f in files:
    create_file(f)

print("Folder structure created successfully in the current directory!")
