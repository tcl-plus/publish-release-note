import argparse
import json
import os
from atlassian import Confluence
from datetime import datetime, timezone


def get_release_message(service_name, image_tag, build_url):
    current_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S %Z")
    return f'<h4>{current_time}&nbsp;&nbsp;&nbsp;&nbsp;{service_name}&nbsp;&nbsp;&nbsp;&nbsp;{image_tag}&nbsp;&nbsp;&nbsp;&nbsp;<a href="{build_url}">详情</a></h4>'


def add_release_info(page_id, title, service_name, image_tag, build_url, conf_url, conf_username, conf_password):
    confluence = Confluence(url=conf_url, username=conf_username, password=conf_password)
    prepend_body = get_release_message(service_name, image_tag, build_url)
    response = confluence.prepend_page(page_id=page_id, title=title, prepend_body=prepend_body)
    page_url = response['_link']['base'] + response['_link']['webui']
    print(f"Publish Release Note to: {page_url}")


def main():
    # 创建解析器并设置参数
    parser = argparse.ArgumentParser(
        description="Update a Confluence page with release information by prepending a message to the page")
    parser.add_argument("--page-id", help="Page ID to update", required=True)
    parser.add_argument("--title", help="Page title to update", required=True)
    parser.add_argument("--service-name", help="Service name for the release", required=True)
    parser.add_argument("--image-tag", help="Image tag for the release", required=True)
    parser.add_argument("--build-url", help="Build URL for the release", required=True)
    parser.add_argument("--url", help="Confluence URL", default=os.environ.get("CONFLUENCE_URL", None))
    parser.add_argument("--username", help="Confluence username", default=os.environ.get("CONFLUENCE_USERNAME", None))
    parser.add_argument("--password", help="Confluence password", default=os.environ.get("CONFLUENCE_PASSWORD", None))

    # 解析参数
    args = parser.parse_args()

    # 调用函数添加release信息
    add_release_info(
        args.page_id,
        args.title,
        args.service_name,
        args.image_tag,
        args.build_url,
        args.url,
        args.username,
        args.password
    )


if __name__ == "__main__":
    main()
