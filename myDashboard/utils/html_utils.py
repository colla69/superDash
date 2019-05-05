
def existinglink(link, caption):
    if link != "":
        return """
                <p><a href="{{ """+link+""" }}" target="_blank">
                    """+caption+"""
                </a></p>
        """