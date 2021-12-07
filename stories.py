"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, title, words, text):
        """Create story with words and template text."""
        self.title = title
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text

story1 = Story("Once Upon a Time", ["place", "noun", "verb", "adjective", "plural_noun"], 
        """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}.""")
story2 = Story("Party Invite!", ["name", "theme", "place", "time", "verb", "animal"], 
        """{name} is having a {theme} party! It's going to be at {place}. 
        Please make sure to show up at {time} or else you will be required to {verb}
        with a {animal}.""")
story3 = Story("New Company", ["company_name", "new_invention", "group_of_people", "problem_to_solve"],
        """My company, {company_name}, is developing {new_invention}
        to help {group_of_people} {problem_to_solve} with {secret sauce}!""")
story4 = Story("Letter from Camp", ["family_member", "camp_name", "activity", "adjective", "plural_noun", "noun", "your_name"], 
        """Dear {family_member}, Here I am at Camp {camp_name}! 
        I am having a {adjective} time. My favorite thing to do so far
        has been {activity}. I even saw a {noun}! I miss {plural_noun} though.
        See you soon! Love, {your_name}""")

stories = {story.title: story for story in [story1, story2, story3, story4]}
