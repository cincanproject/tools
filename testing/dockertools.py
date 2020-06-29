import pathlib
from typing import Optional
from cincan.frontend import ToolImage


def tool_with_file(
    file: str,
    use_tag: Optional[bool] = True,
    image: Optional[str] = None,
    pull: Optional[bool] = False,
) -> ToolImage:
    path = pathlib.Path(file).parent
    name = path.name
    tag = None
    if use_tag:
        tag = "test_{}".format(name)
        # Tag parameter overrides other
        image = None
        pull = False
    return ToolImage(name=name, path=str(path), tag=tag, image=image, pull=pull)
