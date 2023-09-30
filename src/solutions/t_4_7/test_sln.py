from .sln import get_build_order


def test_returns_dependency_projects_before_depending_projects():
    assert get_build_order(
        projects=["a", "b", "c", "d", "e", "f"],
        dependencies=[("a", "d"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c")],
    ) == ["e", "f", "b", "a", "d", "c"]
