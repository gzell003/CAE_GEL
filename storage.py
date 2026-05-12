from pathlib import Path


def ensure_tmp_directory(path: Path) -> None:
    try:
        path.mkdir(parents=True, exist_ok=True)

    except OSError as error:
        raise RuntimeError(
            f"No se pudo crear directorio temporal: {error}"
        ) from error
