resource "google_cloud_run_service" "backend" {
  name     = "olivine-backend"
  location = "asia-south1"

  template {
    spec {
      containers {
        image = "gcr.io/your-project/olivine-backend"
      }
    }
  }
}
