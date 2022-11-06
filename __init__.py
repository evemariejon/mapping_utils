def connect_to_drive():
  # Mount the google drive
  from google.colab import drive
  # Force remount if files are changed
  drive.mount('/content/drive', force_remount=True)
