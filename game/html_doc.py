class Tag(object):

    def __init__(self, name, contents):
        self.start_tag = f'<{name}>'
        self.end_tag = f'</{name}>'
        self.contents = contents

    def __str__(self):
        return f"{self.start_tag}{self.contents}{self.end_tag}"

    def display(self, file=None):
        print(self, file=file)


class DocType(Tag):

    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd"', '')
        self.end_tag = ''  # DOCTYPE doesn't have an endtag


class Head(Tag):
    def __init__(self, title=None):
        super().__init__('head', '')
        self._title_tag = Tag('title', title)
        self.contents = str(self._title_tag)


class Body(Tag):

    def __init__(self):
        super().__init__('body', '') # body contents will be built up separately
        self._body_contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._body_contents.append(new_tag)

    def display(self, file=None):
        for tag in self._body_contents:
            self.contents += str(tag)

        super().display(file=file)


class HtmlDoc(object):

    def __init__(self, doc_type, head, body):
        self._doc_type = doc_type
        self._head = head
        self._body = body

    def add_body_tag(self, name, contents):
        self._body.add_tag(name, contents)

    def add_head_tag(self, name, contents):
        self._head.add_tag(name, contents)

    def display(self, file=None):
        self._doc_type.display(file=file)
        print('<html>', file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print('</html>', file=file)


if __name__ == "__main__":
    # my_page = HtmlDoc()
    # my_page.add_head_tag('title', "Document Title")
    # my_page.add_body_tag('h1', 'Main heading')
    # my_page.add_body_tag('h2', 'sub-heading')
    # my_page.add_body_tag('p', 'This is a paragraph that will appear on the page')
    #
    # with open('test.html', 'w') as test_doc:
    #     my_page.display(file=test_doc)
    new_body = Body()
    new_body.add_tag('h1', 'Aggregation')
    new_body.add_tag('p', 'Unlike <strong>composition</strong>, aggredation uses existing instances of objects to '
                          'build up another object.')
    new_body.add_tag('p', "The composed object doesn't actually own the objects that it;s composted of - if it's "
                          "destroyed those objects continue to exist.")
    
    new_docType = DocType()
    new_header = Head('Aggregation document')
    my_page = HtmlDoc(new_docType, new_header, new_body)

    with open('test3.html', 'w') as test_doc:
        my_page.display(file=test_doc)
