
def existinglink(link, caption):
    if not link is None:
        return """
                <p><a href=" """+link+""" " target="_blank">
                    """+caption+"""
                </a></p>
        """