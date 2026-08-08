#!/usr/bin/env python3
# [MISE] description="Generate the local conditional-instructions index"
# [MISE] sources=["conditional-instructions.yaml"]
# [MISE] outputs=["conditional-instructions-local.yaml"]

from pathlib import Path
import re
from urllib.parse import urlsplit


URL_LINE_RE = re.compile(
    r'^(?P<indent>\s*)url:\s*(?P<url>\S+)(?P<suffix>\s*(?:#.*)?)$',
    re.MULTILINE,
)


def local_path(url: str) -> str:
    parsed_url = urlsplit(url)
    if parsed_url.scheme != 'https' or parsed_url.netloc != 'raw.githubusercontent.com':
        raise ValueError(f'Cannot convert non-GitHub file reference: {url}')

    parts = parsed_url.path.removeprefix('/').split('/')
    if len(parts) < 4:
        raise ValueError(f'Cannot determine repository and file path: {url}')

    repository = parts[1]
    ref_parts = parts[2:]
    file_parts = ref_parts[3:] if ref_parts[:2] == ['refs', 'heads'] else ref_parts[1:]
    if not file_parts:
        raise ValueError(f'Cannot determine file path: {url}')

    return f'~/projects/{repository}/{"/".join(file_parts)}'


def main() -> None:
    project_dpath = Path(__file__).resolve().parent.parent
    source_fpath = project_dpath / 'conditional-instructions.yaml'
    output_fpath = project_dpath / 'conditional-instructions-local.yaml'
    source = source_fpath.read_text()

    reference_count = 0

    def replace_reference(match: re.Match[str]) -> str:
        nonlocal reference_count
        reference_count += 1
        return (
            f'{match.group("indent")}path: {local_path(match.group("url"))}{match.group("suffix")}'
        )

    output = URL_LINE_RE.sub(replace_reference, source)
    if not reference_count:
        raise ValueError(f'No file references found in {source_fpath}')

    output_fpath.write_text(output)


if __name__ == '__main__':
    main()
