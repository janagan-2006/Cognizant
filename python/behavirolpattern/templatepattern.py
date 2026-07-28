from abc import ABC, abstractmethod

class Report(ABC):

    def generate(self):

        self.fetch_data()

        self.process_data()

        self.export()

    @abstractmethod
    def fetch_data(self):
        pass

    @abstractmethod
    def export(self):
        pass

    def process_data(self):
        print("Processing")

class PDFReport(Report):

    def fetch_data(self):
        print("Fetch from DB")

    def export(self):
        print("Export PDF")

report = PDFReport()

report.generate()

# chain of responsibility - > request Before go to the controller it is validated by so many classes 
# Mediator -> Objects communicate through a central mediator. example below
# User A
# User B
# User C
#    ↓
# Chat Server