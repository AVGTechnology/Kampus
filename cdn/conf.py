import os

AWS_ACCESS_KEY_ID = 'FMAGECPBUNCWXWAIIVOD'
AWS_SECRET_ACCESS_KEY = 'N1MX6oStDkTXglMLGBMXRf7CjzayFEJ+ihaVsGJX/OA'
AWS_STORAGE_BUCKET_NAME = 'kampusstorage'
AWS_S3_ENDPOINT_URL = 'fra1.digitaloceanspaces.com'
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
}
AWS_LOCATION = f"https://{AWS_STORAGE_BUCKET_NAME}.fra1.digitaloceanspaces.com"

DEFAULT_FILE_STORAGE = "cdn.backends.MediaRootS3Boto3Storage"
STATICFILES_STORAGE = "cdn.backends.StaticRootS3Boto3Storage"
