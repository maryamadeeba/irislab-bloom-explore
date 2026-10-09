"""IrisLab API. Reads iris_data.csv on every request so notebook edits appear live.
Run: python iris_dashboard_server.py, then open http://127.0.0.1:5000
"""
from pathlib import Path
import pandas as pd
from flask import Flask, jsonify, send_from_directory
from sklearn.datasets import load_iris

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "iris_data.csv"
app = Flask(__name__, static_folder=None)
FEATURES = ["sepal length (cm)", "sepal width (cm)", "petal length (cm)", "petal width (cm)"]


def get_iris_frame():
    # Re-read the CSV for every API request: changes saved by the notebook are live.
    if DATA_FILE.exists():
        df = pd.read_csv(DATA_FILE)
    else:
        iris = load_iris(as_frame=True)
        df = iris.frame.copy()
        df["species"] = df["target"].map({0: "setosa", 1: "versicolor", 2: "virginica"})
        df = df.drop(columns=["target"])
    if "target" in df.columns and "species" not in df.columns:
        df["species"] = df["target"].map({0: "setosa", 1: "versicolor", 2: "virginica"})
        df = df.drop(columns=["target"])
    missing = [c for c in FEATURES + ["species"] if c not in df.columns]
    if missing:
        raise ValueError("Dataset is missing required columns: " + ", ".join(missing))
    df = df[FEATURES + ["species"]].copy()
    for col in FEATURES:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df["species"] = df["species"].astype("string").str.lower().str.strip()
    return df


@app.get("/")
def index():
    return send_from_directory(BASE_DIR, "irislab_frontend_connected.html")


@app.get("/api/dataset")
def dataset():
    try:
        df = get_iris_frame()
        features = [c for c in df.columns if c != "species"]
        records = df.where(pd.notna(df), None).to_dict(orient="records")
        summary = {
            "samples": int(len(df)),
            "species_count": int(df["species"].nunique(dropna=True)),
            "feature_count": len(features),
            "missing_values": int(df.isna().sum().sum()),
            "species_distribution": {str(k): int(v) for k, v in df["species"].value_counts().to_dict().items()},
            "features": features,
            "source": DATA_FILE.name if DATA_FILE.exists() else "scikit-learn fallback"
        }
        return jsonify({"summary": summary, "records": records})
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500


@app.get("/api/health")
def health():
    return jsonify({"status": "ok", "data_file": str(DATA_FILE), "csv_exists": DATA_FILE.exists()})


if __name__ == "__main__":
    print("IrisLab dashboard: http://127.0.0.1:5000")
    print(f"Live CSV source: {DATA_FILE}")
    print("Save/rerun the notebook export cell to update the dashboard.")
    app.run(host="127.0.0.1", port=5000, debug=False)
