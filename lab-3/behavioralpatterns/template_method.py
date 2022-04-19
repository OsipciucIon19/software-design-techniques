from abc import ABC, abstractmethod


class ResearchGuideline(ABC):
    def template_method(self):
        self.request_letter()
        self.complete_information()
        self.apply()
        self.get_documents()

    def request_letter(self):
        pass

    def complete_information(self):
        pass

    @abstractmethod
    def apply(self):
        pass

    def get_documents(self):
        pass


class TechnicalUniversityOfMoldova(ResearchGuideline):
    def complete_information(self):
        print(" - Completing personal information for Technical University of Moldova")

    def apply(self):
        print(" - Applying for Technical University of Moldova")


class StateUniversityOfMoldova(ResearchGuideline):
    def request_letter(self):
        print(" - Requesting a letter for State University of Moldova")

    def apply(self):
        print(" - Applying for State University of Moldova")

    def get_documents(self):
        print(" - Getting documents for State University of Moldova")


def client_call(research_guideline: ResearchGuideline):
    research_guideline.template_method()


if __name__ == '__main__':
    print("\nTechnical University of Moldova:")
    client_call(TechnicalUniversityOfMoldova())

    print("\nState University of Moldova:")
    client_call(StateUniversityOfMoldova())
