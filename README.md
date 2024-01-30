# Publish Release Note

This script automatically updates a Confluence page with release information by prepending a message to the page.
The release message includes service name, image tag, current time and a build URL.

## Usage

The script can be run with the following command:

```shell
python main.py \
    --page-id PAGE_ID \
    --title TITLE \
    --service-name SERVICE_NAME \
    --image-tag IMAGE_TAG \
    --build-url BUILD_URL \
    --url CONFLUENCE_URL \
    --username USERNAME \
    --password PASSWORD
```

All parameters can either be provided as command line arguments or as environment variables. The latter is useful when running the script within a CI/CD pipeline.
If provided, command line arguments override the corresponding environment variables.
The parameters are explained as follows:

- `--page-id`: The ID of the Confluence page to be updated.
- `--title`: The new title of the Confluence page.
- `--service-name`: The name of the service for the release.
- `--image-tag`: The image tag for the release.
- `--build-url`: The URL to the detailed information of the build.
- `--url`: The Confluence server URL. Can be provided as an environment variable CONFLUENCE_URL instead.
- `--username`: The Confluence username for authentication. Can be provided as an environment variable CONFLUENCE_USERNAME instead.
- `--password`: The Confluence password for authentication. Can be provided as an environment variable CONFLUENCE_PASSWORD instead.


## Run Container

```shell
docker run -e CONFLUENCE_URL=your_url \
  -e CONFLUENCE_USERNAME=your_username \
  -e CONFLUENCE_PASSWORD=your_password \
  ghcr.io/tcl-plus/publish-release-note:latest \
  --page-id PAGE_ID \
  --title TITLE \
  --service-name SERVICE_NAME \
  --image-tag IMAGE_TAG \
  --build-url BUILD_URL \
```
