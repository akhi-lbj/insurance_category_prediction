# Insurance Premium Prediction API

A production-grade REST API built with **FastAPI** to predict insurance premium categories. This project leverages machine learning to provide accurate premium estimations based on user demographics, health metrics (calculated dynamically), and lifestyle factors.

## 🚀 Features

- **Real-time Predictions**: Instant assessment of insurance premium categories.
- **Dynamic Feature Engineering**: Automatically calculates BMI, Age Group, City Tier, and Lifestyle Risk using Pydantic's `@computed_field`.
- **Structured Validation**: Robust input validation and normalized data handling.
- **Detailed Insights**: Returns the predicted category, confidence level, and class-wise probabilities.
- **Health Check Endpoint**: Built-in monitoring for API and model status.

## 🛠️ Tech Stack

- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Data Validation**: [Pydantic v2](https://docs.pydantic.dev/)
- **Machine Learning**: [Scikit-learn](https://scikit-learn.org/)
- **Data Manipulation**: [Pandas](https://pandas.pydata.org/)
- **Backend Architecture**: Modular Python structure with clear separation of concerns.

## 📁 Project Structure

```text
insurance-premium-project/
├── main.py                 # API entry point and route definitions
├── model/
│   ├── model.pkl           # Pre-trained ML model (Pickle format)
│   └── predict.py          # Prediction logic and wrapper
├── schema/
│   ├── user_input.py       # Input validation & feature engineering logic
│   └── prediction_response.py # Output data structure
├── config/
│   └── city_tier.py        # City-to-tier mapping configuration
├── requirements.txt        # Project dependencies
└── pyproject.toml          # Development configuration
```

## 📋 API Endpoints

### 1. Home
- **URL**: `/`
- **Method**: `GET`
- **Description**: Returns a welcome message.

### 2. Health Check
- **URL**: `/health`
- **Method**: `GET`
- **Description**: Checks if the API is running and the model is loaded correctly.

### 3. Predict Premium
- **URL**: `/predict`
- **Method**: `POST`
- **Payload**:
  ```json
  {
    "age": 30,
    "weight": 75.0,
    "height": 1.75,
    "income_lpa": 12.5,
    "smoker": false,
    "city": "Mumbai",
    "occupation": "private_job"
  }
  ```
- **Response**:
  ```json
  {
    "response": {
      "predicted_category": "Standard",
      "confidence": 0.8521,
      "class_probabilities": {
        "Low": 0.1,
        "Standard": 0.8521,
        "High": 0.0479
      }
    }
  }
  ```

## ⚙️ How it Works

1. **Input Validation**: When a request is received, Pydantic validates the input fields (age, weight, height, etc.).
2. **Automated Feature Engineering**:
   - `bmi`: Calculated as $weight / height^2$.
   - `age_group`: Categorized into *young, adult, middle_aged, senior*.
   - `lifestyle_risk`: Determined via a combination of smoking status and BMI.
   - `city_tier`: Resolved based on the city name against a pre-configured list.
3. **ML Inference**: The processed features are passed to a pre-trained Scikit-learn model (`model.pkl`).
4. **Response Generation**: The API returns the most likely category along with the model's confidence and full probability distribution.

## 👨‍💻 Installation & Running

### 🐳 Docker (Recommended)

The official Docker image is available on [Docker Hub](https://hub.docker.com/repository/docker/akhilbaburaj204/insurance-premium-project/general).

The easiest way to run the application is using Docker:

1. **Using pre-built image from Docker Hub**:
   ```bash
   docker pull akhilbaburaj204/insurance-premium-project
   docker run -p 8000:8000 akhilbaburaj204/insurance-premium-project
   ```

2. **Or build from source**:
   ```bash
   git clone https://github.com/akhi-lbj/insurance-premium-project.git
   cd insurance-premium-project
   docker build -t insurance-premium-api .
   docker run -p 8000:8000 insurance-premium-api
   ```

3. **Run in detached mode (background)**:
   ```bash
   docker run -d -p 8000:8000 --name insurance-api akhilbaburaj204/insurance-premium-project
   ```

The API will be available at `http://localhost:8000`.

### 💻 Local Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd insurance-premium-project
   ```

2. **Set up virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the API**:
   ```bash
   uvicorn main:app --reload
   ```
   The API will be available at `http://127.0.0.1:8000`.


