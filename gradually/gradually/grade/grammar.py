import language_check

def grammar(essay):
    tool = language_check.LanguageTool('en-US')

    matches = tool.check(essay)

    return matches