def markdown_to_blocks(markdown):
    return [x.lstrip("\n") for x in markdown.strip().split("\n\n") if x != ""]
