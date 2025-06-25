from abc import ABC, abstractmethod

class Format:
    def render(selfself, title: str, content: str):
        pass

class PDFFormat(Format):
    def render(self, title, content):
        print(f"[PDF] {title.upper()} --- {content[:30]}...\n")

class EPUBFormat(Format):
    def render(self, title, content):
        print(f"[EPUB] *** {title} ***\n {content[:50]}...\n")

class MOBIFormat(Format):
    def render(self, title, content):
        print(f"[MOBI] *** <<{title}>>\n {content[:40]}...\n")

class EBook:
    def __init__(self, title: str, content: str, format: Format):
        self.title = title
        self.content = content
        self.format = format

    def display(self):
        self.format.render(self.title, self.content)

class FantasyEBook(EBook):
    def display(self):
        print("Fantasy Book Loaded:")
        super().display()

class ScienceEBook(EBook):
    def display(self):
        print("Science Book Loaded:")
        super().display()

pdf = PDFFormat()
epub = EPUBFormat()
mobi = MOBIFormat()

fantasy = FantasyEBook("Alice in Wonderland", "Follow young Alice as she tumbles down a rabbit hole into a magical world filled with curious creatures, puzzling riddles, and whimsical adventures.", pdf)
science = ScienceEBook("On the Origin of Species", "On the Origin of Species by Charles Darwin is a groundbreaking work that laid the foundation for the modern theory of evolution.", mobi)
short_story = FantasyEBook("The Last Question", "Spanning billions of years, the story follows a recurring question about entropy and the possibility of reversing the inevitable heat death of the cosmos.", epub)

fantasy.display()
science.display()
short_story.display()