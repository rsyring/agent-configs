#!/usr/bin/env python3
# [MISE] description="Update conditional-instructions sections in ~/projects"

from dataclasses import dataclass
from pathlib import Path
import re


SECTION_TITLE = 'Conditional Instructions Index'
SECTION_RE = re.compile(
    rf'^#{{1,2}} {re.escape(SECTION_TITLE)}(?:\r?\n|\Z).*?(?=^#{{1,2}}\s|\Z)',
    re.MULTILINE | re.DOTALL,
)


@dataclass(frozen=True)
class SectionUpdater:
    source_fpath: Path
    projects_dpath: Path

    def project_dpaths(self) -> list[Path]:
        project_dpaths = []

        for project_dpath in sorted(self.projects_dpath.iterdir()):
            if not project_dpath.is_dir():
                continue

            project_dpaths.append(project_dpath)
            if (project_dpath / '.git').exists():
                continue

            for nested_dpath, dirnames, filenames in project_dpath.walk():
                if '.git' not in dirnames and '.git' not in filenames:
                    continue

                dirnames.clear()
                project_dpaths.append(nested_dpath)

        return sorted(project_dpaths)

    def section(self, content: str, fpath: Path) -> str:
        matches = SECTION_RE.findall(content)
        if len(matches) != 1:
            raise ValueError(f'Expected one {SECTION_TITLE!r} section in {fpath}')
        return matches[0]

    def update(self) -> list[Path]:
        current_section = self.section(self.source_fpath.read_text(), self.source_fpath)
        changed_fpaths = []

        for project_dpath in self.project_dpaths():
            for filename in ('AGENTS.md', 'AGENTS.local.md'):
                fpath = project_dpath / filename
                if not fpath.is_file():
                    continue

                content = fpath.read_text()
                matches = SECTION_RE.findall(content)
                if not matches or matches == [current_section]:
                    continue
                if len(matches) != 1:
                    raise ValueError(f'Expected at most one {SECTION_TITLE!r} section in {fpath}')

                fpath.write_text(SECTION_RE.sub(lambda _: current_section, content))
                changed_fpaths.append(fpath)

        return changed_fpaths


def main() -> None:
    project_dpath = Path(__file__).resolve().parent.parent
    updater = SectionUpdater(
        source_fpath=project_dpath / 'AGENTS.md',
        projects_dpath=Path.home() / 'projects',
    )
    changed_fpaths = updater.update()
    if not changed_fpaths:
        print('All conditional-instructions sections are current.')
        return

    for fpath in changed_fpaths:
        print(f'Updated {fpath}')


if __name__ == '__main__':
    main()
