def abs_path_from_project(relative_path: str):
    import superjob_project.utils
    from pathlib import Path

    return (
        Path(superjob_project.utils.__file__)
            .parent.parent.parent.joinpath(relative_path)
            .absolute()
            .__str__()
    )
