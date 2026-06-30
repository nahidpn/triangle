"""API endpoint tests"""
import pytest
from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

class TestHealthCheck:
    def test_health_endpoint(self):
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert "version" in data
        assert "timestamp" in data
        assert "model_loaded" in data

class TestRoot:
    def test_root_endpoint(self):
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert "version" in data
        assert "docs" in data

class TestImageDetection:
    def test_image_detection_missing_file(self):
        response = client.post("/api/v1/detect/image")
        assert response.status_code == 422

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
