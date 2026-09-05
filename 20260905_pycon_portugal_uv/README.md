# Fast Python Development With uv

## Links

 - Install uv: https://docs.astral.sh/uv/getting-started/installation/
 - uv docs: https://docs.astral.sh/uv/
 - uv cheatsheet (web): https://mathspp.com/blog/uv-cheatsheet
 - uv cheatsheet (PDF): https://mathspp.gumroad.com/l/cheatsheet-uv

## Useful during the workshop

Configure TestPyPI in `pyproject.toml`:

```toml
[[tool.uv.index]]
name = "testpypi"
url = "https://test.pypi.org/simple/"
publish-url = "https://test.pypi.org/legacy/"
explicit = true
```

Publish _to TestPyPI_:

```bash
% uv publish --index testpypi
```

Install _from TestPyPI_:

```bash
% uv add <package-name> --index https://test.pypi.org/simple/
```
