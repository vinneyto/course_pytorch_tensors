"""Проверка структуры курса, не требующая решённых заданий."""

from __future__ import annotations

import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    themes = sorted(path for path in ROOT.glob("[0-9][0-9]_*") if path.is_dir())
    assert themes, "Не найдены каталоги тем"
    for theme in themes:
        exercises = sorted(path for path in theme.glob("[0-9][0-9]_*") if path.is_dir())
        assert exercises, f"В теме {theme.name} нет заданий"
        for exercise in exercises:
            expected = (
                exercise / "README.md",
                exercise / "task.py",
                exercise / "test_task.py",
            )
            missing = [path.name for path in expected if not path.is_file()]
            assert not missing, f"{exercise.relative_to(ROOT)}: отсутствуют {missing}"
            readme = expected[0].read_text(encoding="utf-8")
            assert "## Задание" in readme or theme.name < "09_", (
                f"{exercise.relative_to(ROOT)}: в README нет раздела задания"
            )
            assert "https://docs.pytorch.org/" in readme, (
                f"{exercise.relative_to(ROOT)}: нет ссылки на документацию PyTorch"
            )
            for source in expected[1:]:
                ast.parse(source.read_text(encoding="utf-8"), filename=str(source))
    print(
        f"Курс корректен: {len(themes)} тем, {sum(len(list(t.glob('[0-9][0-9]_*'))) for t in themes)} заданий"
    )


if __name__ == "__main__":
    main()
