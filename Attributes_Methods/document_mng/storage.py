from AttributesMethods.document_mng_03.topic import Topic
from AttributesMethods.document_mng_03.category import Category
from AttributesMethods.document_mng_03.document import Document

class Storage:

    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        curr_cat = [c for c in self.categories if c.id == category_id][0]
        curr_cat.name = new_name

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        curr_topic = [t for t in self.topics if t.id == topic_id][0]
        curr_topic.edit_topic(new_topic, new_storage_folder)

    def edit_document(self, document_id, new_file_name):
        curr_document = [d for d in self.documents if d.id == document_id][0]
        curr_document.edit(new_file_name)

    def delete_category(self, category_id):
        self.categories.remove([c for c in self.categories if c.id == category_id][0])

    def delete_topic(self, topic_id):
        self.topics.remove([c for c in self.topics if c.id == topic_id][0])

    def delete_document(self, document_id):
        self.documents.remove([d for d in self.documents if d.id == document_id])

    def get_document(self, document_id):
        return [d for d in self.documents if d.id == document_id][0]

    def __repr__(self):
        return "\n".join(repr(d) for d in self.documents)


c1 = Category(1, "work")
t1 = Topic(1, "daily tasks", "C:\\work_documents")
d1 = Document(1, 1, 1, "finilize project")
d2 = Document.from_instances(2, 1, 2, "Soccer")
d1.add_tag("urgent")
d1.add_tag("work")

storage = Storage()
storage.add_category(c1)
storage.add_topic(t1)
storage.add_document(d1)
storage.add_document(d2)
print(c1)
print(t1)
print(storage.get_document(1))
print(storage)
