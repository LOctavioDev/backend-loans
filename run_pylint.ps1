Get-ChildItem -Recurse -Filter "*.py" | Where-Object {
    $_.FullName -notmatch "venv|__pycache__|.ruff_cache"
} | ForEach-Object {
    pylint $_.FullName
}
