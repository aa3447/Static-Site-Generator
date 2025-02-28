class BlockNode:
    def __init__(self):
        pass

    def markdown_to_blocks(markdown):
        single_line_blocks = markdown.split("\n\n")
        removed_whitepace_from_blocks = map(lambda block: block.strip(), single_line_blocks)
        filtered_empty_blocks = list(filter(lambda block: block != "", removed_whitepace_from_blocks))
        return filtered_empty_blocks